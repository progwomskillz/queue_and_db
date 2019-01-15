import json

import pika

from models import User
from infrastructure.db import EngineBuilder, SessionBuilder
from services import DBService, EmailService
from commands import WriteToDbCommand, SendEmailCommand
from invoker import Invoker


class RabbitWrapper:
    def __init__(self, environment_manager):
        self.environment_manager = environment_manager

        self.host = self.environment_manager.get_var_from_env('RABBIT_HOST')
        self.queue = self.environment_manager.get_var_from_env('RABBIT_QUEUE')

    def start_consuming(self):
        self.__connect()
        self.channel.basic_consume(self.__callback, queue=self.queue)
        self.channel.start_consuming()

    def send_message(self, message):
        self.__connect()
        body = json.dumps(message)
        self.channel.basic_publish(exchange='', routing_key=self.queue,
                                   body=body)
        self.connection.close()

    def __connect(self):
        connection_params = pika.ConnectionParameters(host=self.host)
        self.connection = pika.BlockingConnection(connection_params)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

    def __callback(self, ch, method, properties, body):
        user_dict = json.loads(body)
        user_object = User(**user_dict)

        engine_builder = EngineBuilder(self.environment_manager)
        engine = engine_builder.build()
        session_builder = SessionBuilder(engine)
        session = session_builder.build()

        db_service = DBService(session, user_object)
        write_to_db_command = WriteToDbCommand(db_service)

        message = {
            'from': 'Man <man@example.com>',
            'to': 'admin@example.com',
            'subject': 'Success',
            'text': 'Write successfully!'
        }
        email_service = EmailService(self.environment_manager, message)
        send_email_command = SendEmailCommand(email_service)

        commands = [write_to_db_command, send_email_command]

        invoker = Invoker(commands)

        if invoker.execute_commands():
            print('Success')
        else:
            print('Error')

        session.close()
        engine.dispose()

        ch.basic_ack(delivery_tag=method.delivery_tag)

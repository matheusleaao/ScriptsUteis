# Realizar a análise de uma fila RABBITMQ e retorna a quantidade de mensagens numa fila 
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>

#!/usr/bin/env python

import pika

#Conexao
credentials      = pika.PlainCredentials('', '') #...(user,pass)
parameters       = pika.ConnectionParameters('', 5672, '/', credentials)
connection       = pika.BlockingConnection(parameters)
channel          = connection.channel()

print("Connection opened! :D\n")

queueName        = "hello" 

declarationQueue = channel.queue_declare(queueName, 
                                        passive=False,
                                        durable=True,
                                        exclusive=False,
                                        auto_delete=False,
                                        arguments=None,)
counter          = declarationQueue.method.message_count

print('A fila "'+str(queueName)+'" possui: '+str(counter)+'  mensagens\n')

connection.close()

print ("Connection closed! :D")

#!/usr/bin/env python

import pika

#Conexao


connection = pika.BlockingConnection(pika.ConnectionParameters(host='', port=""))
channel = connection.channel()

print "Connection opened! :D"


queue = ""

q = channel.queue_declare(queue, 
                          passive=False,
                          durable=True,
                          exclusive=False,
                          auto_delete=False,
                          arguments=None,)

contador = q.method.message_count

print 'A fila %s possui: %s  mensagens'%(queue , contador)

connection.close()
print "Connection closed! :D"

#!/bin/bash

ENDPOINT='cache-redis-001.nrpz0w.0001.use1.cache.amazonaws.com'
PORT='6379'
#CMD="sed -i '/OK/d' /usr/lib/zabbix/externalscripts/resultado.txt"

STATUS_redis=$(redis-cli -c -h $ENDPOINT -p $PORT < /usr/lib/zabbix/externalscripts/redis_keyContent.txt > /usr/lib/zabbix/externalscripts/resultado_KeyContent.txt ; sudo sed -i '1d' /usr/lib/zabbix/externalscripts/resultado_KeyContent.txt ; grep -q '[^[:space:]]' /usr/lib/zabbix/externalscripts/resultado_KeyContent.txt && echo "1" || echo "0")
if [ "$STATUS_redis" == "1" ]; then
        echo 1
else
        echo 0
fi

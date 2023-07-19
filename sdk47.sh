#!/bin/sh

scp SDK-Dashboard/Python/* root@192.168.10.47:/root/superset/sdk/

ssh root@192.168.10.47 "pm2 restart 2"
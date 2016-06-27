#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import sys
TIMEOUT = 5
def ping(ip,port,timeout=TIMEOUT):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = (str(ip),int(port))
        status = s.connect_ex(address)
        s.settimeout(timeout)
        if status == 0:
            print "the %s:%d is running..." %(ip,int(port))
        else:
            print "the %s:%d is down..." %(ip,int(port))
    except Exception,e:
        print e
if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print "请参考如下格式使用： ./check_tcpport.py  IP PORT "
        sys.exit(1)
    ip = sys.argv[1]
    port = sys.argv[2]
    try:
        timeout = sys.argv[3]
    except IndexError,e:
        timeout = TIMEOUT
    ping(ip,port,timeout)
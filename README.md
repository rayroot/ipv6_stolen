##  ipv6_stolen

This is just a trick or tool for stolen a ipv6 address from pd( prefix delegation) . 

For example, if you have a modem from your ISP, and have an ipv6 prefix by dhcp prefix delegation, the device that connected the modem can  get an ipv6 address, but if you have second router，the device that connected the second router maybe can’t get ipv6 address. 

ipv6_stolen provides an solution by NDP spoof and add some host routes，make the given ipv6 address be config in the remote device.  

### for example in home network

![ipv6](https://github.com/rayroot/ipv6_stolen/blob/master/ipv6%20stolen.jpg)


if you use this little tool, the scapy python module should be install. 

````
./ipv6-stolen.py -h 
The usage is: 
./ipv6_stolen.py -u <uplink dev> -t <target ipv6 address>
or: 
./ipv6_stolen.py --uplink=<uplinl dev> --target=<target ipv6 address>

````



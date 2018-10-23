#!/usr/bin/env python3
#Author: James DuDasko

ipchk = input('Apply an IP address: ') #prompt user for input

if ipchk == '192.168.70.1': #if any data is provided, this will test true
   print('Looks like the IP address of the Gateway was set: ' + ipchk)
elif ipchk:
   print('Looks like the IP address was set: ' + ipchk)
else: #if no data is provided
   print('You did not provide input.') 

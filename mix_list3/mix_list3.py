#!/usr/bin/env python3
#Author: James DuDasko

list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1[1])

#insert data into list
list1.extend(['juniper'])
print(list1)

#append list
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print(list1[4])
print(list1[4][0])

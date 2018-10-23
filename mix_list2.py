#!/usr/bin/env python3
#Author: James DuDasko

proto = ['ssh', 'http', 'https' ]
protoa = ['ssh', 'http', 'https' ]

#print statements
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)
proto.pop(1)
print(proto) # pop a value and print
protoa.insert(2, 'sctp')
print(protoa)  # insert value and print
proto.count('http')
print(proto) # count occurence and pring

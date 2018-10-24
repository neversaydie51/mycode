#!/usr/bin/env python3
#Author: James DuDasko
#parse keystone.common.wsgi and return failed attempts
loginfail = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')

keystone_file_lines = keystone_file.readlines()

#Loop will search for string and output number of occurances
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
print('The number of failed log in attempts is ' + str(loginfail))

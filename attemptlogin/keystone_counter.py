#!/usr/bin/env python3
#Author: James DuDasko
#parse keystone.common.wsgi and return failed attempts
loginfail = 0
loginsuccess = 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')

keystone_file_lines = keystone_file.readlines()

#Loop will search for string and output number of occurances
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
print('The number of failed log in attempts is ' + str(loginfail))

#Loop will search for successful logins
for i in range(len(keystone_file_lines)):
    if "GET http://controller:5000/v3/users/63dee1ed626b4040bcd43b3492997a8c/projects" in keystone_file_lines[i]:
        loginsuccess += 1
print('The number of successful log in attempts is ' + str(loginsuccess))


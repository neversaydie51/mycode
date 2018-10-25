#!/usr/bin/env python3
#Author: James DuDasko

outFile = open('admin.rc', 'a')

#Prompt user for OS_Auth_URL
print('What is the OS_AUTH_URL?')
osAuth = input()
print('export OS_AUTH_URL = ' + osAuth, file = outFile)

#Output OS_ID_API_VERSION
print('export OS_IDENTITY_API_VERSION = 3', file = outFile)

#Prompt user for OS_PROJECT_NAME
print('What is the OS_PROJECT_NAME?')
osPROJ = input()
print('export OS_PROJECT_NAME = ' + osPROJ, file = outFile)

#Prompt user for OS_PROJECT_DOMAIN_NAME
print('What is the OS_PROJECT_DOMAIN_NAME?')
osPROJDOM = input()
print('export OS_PROJECT_DOMAIN_NAME = ' + osPROJDOM, file = outFile)

#Prompt user for OS_USERNAME
print('What is the OS_USERNAME?')
osUSER = input()
print('export OS_USERNAME = ' + osUSER, file = outFile)

#Prompt user for OS_USERNAME_DOMAIN_NAME
print('What is the OS_USERNAME_DOMAIN_NAME?')
osUSERDOM = input()
print('export OS_USERNAME_DOMAIN_NAME = ' + osUSERDOM, file = outFile)

#Prompt user for OS_PASSWORD
print('What is the OS_PASSWORD?')
osPASS = input()
print('export OS_PASSWORD = ' + osPASS, file = outFile)

outFile.close()


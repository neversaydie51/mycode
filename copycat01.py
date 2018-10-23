#!/usr/bin/env python3
#Author: James DuDasko
#File manipulation
# The following line will create the directory if it does not exist already

import shutil
import os

#Enable script to start in outlined directory
os.chdir('/home/student/mycode/')

#Copy folder and move to another directory
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

#Backup directory
shutil.copytree('5g_research/', '5g_research_backup/')

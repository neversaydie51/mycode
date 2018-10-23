#!/usr/bin/env python3
#Author: James DuDasko
#File and Folder manipulation. Renaming and moving.

import shutil
import os

xname = input('Waht is the new name for kerrigan.obj? ')

#Enable script to start in outlined directory
os.chdir('/home/student/mycode/')

#Move file to new directory
shutil.move('raynor.obj', 'ceph_storage/')

#Rename file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

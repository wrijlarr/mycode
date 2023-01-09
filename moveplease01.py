#!/usr/bin/env python3

# import shutil and os

import shutil
import os

def main():
    """call at runtime"""
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompt user for new name of file
    xname = input('What is the new name for kerrigan.obj? ') #collect user input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' #move kerrigan.obj to ceph_storage 
                                                             #with new name


main() #call main function

#!/usr/bin/env python3

#allow for higher level file manipulation
import shutil

import os


def main():

    #force python to start in home user directory
    os.chdir('/home/student/mycode/')

    #move file from source to destination, will overwrite a file if one
    #with the same name is already in that location
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompt for a new name before moving a file
    xname = input('What is the new name for kerrigan.obj? ')

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()


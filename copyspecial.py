#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Sarah Beverton"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    files = os.listdir(dirname)
    special_pattern = re.compile(r'__\w+__')
    for filename in files:
        if special_pattern.findall(filename):
            result.append(os.path.abspath(filename))
    return result


def copy_to(path_list, dest_dir):
    """Given a list of file paths, copies those files into the given directory"""
    shutil.copy()
    return


def zip_to(path_list, dest_zip):
    """Given a list of file paths, zip those files up into the given zip path"""
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    '''need to tell it to print a list of abs paths if no args present (print whatever is
    returned from the get_special_paths function'''
    '''if --todir dir is present, copy the files to the given directory, creating directory if necessary (use shutil for copying)'''
    '''if --tozip zipfile is present, zip to file and also print command saying that - use subprocess for this - if there is an error, exit and display error code and message'''
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='directory to look in', nargs='+')
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    dir_to_use = ns.from_dir

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    dirname = args[0]
    
    if dir_to_use:
        special_paths = get_special_paths(dirname)
        print('\n'.join(special_paths))

if __name__ == "__main__":
    main(sys.argv[1:])

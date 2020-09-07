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
    abs_dirname = os.path.abspath(dirname)
    result = []
    files = os.listdir(abs_dirname)
    special_pattern = re.compile(r'__\w+__')
    for filename in files:
        if special_pattern.findall(filename):
            result.append(os.path.join(abs_dirname, filename))
    return result


def copy_to(path_list, dest_dir):
    """Given a list of file paths, copies the files into the given directory"""
    abs_dest_dir = os.path.abspath(dest_dir)
    if not os.path.exists(abs_dest_dir):
        os.makedirs(abs_dest_dir)
    for path in path_list:
        shutil.copy(path, abs_dest_dir)


def zip_to(path_list, dest_zip):
    """Given a list of file paths, zip those files into the given zip path"""
    abs_dest_zip = os.path.abspath(dest_zip)
    try:
        zip_run = 'zip -j ' + abs_dest_zip + ' ' + ' '.join(path_list)
        subprocess.run(zip_run, shell=True)
    except subprocess.CalledProcessError as err:
        print(err.cmd)
        print(err.output)


def main(args):
    """Main driver code for copyspecial."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to look in',
                        nargs='+', type=str)
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    dir_to_use = ns.from_dir

    if dir_to_use:
        special_paths = get_special_paths(''.join(dir_to_use))
        print('\n'.join(special_paths))
        if ns.todir:
            copy_to(special_paths, ns.todir)
        if ns.tozip:
            zip_to(special_paths, ns.tozip)


if __name__ == "__main__":
    main(sys.argv[1:])

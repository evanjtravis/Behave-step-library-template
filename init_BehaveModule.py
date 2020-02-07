#!/usr/bin/env python3

import shutil
import os
import sys

DIR = os.path.abspath(os.path.dirname(__file__))


def main(args):
    """"""
    mod_name = args[1]
    shutil.copytree(os.path.join(DIR,"BehaveModule_template_tree"), os.path.join(DIR, "BehaveModule"))

    template_module_path = os.path.join(DIR,"BehaveModule_template_tree", "sdg", "test", "behave", 10*"X")
    new_module_path = os.path.join(DIR, "BehaveModule", "sdg", "test", "behave", mod_name)
    
    print(new_module_path)
    shutil.copytree(template_module_path, new_module_path)
    shutil.rmtree(os.path.join(DIR, "BehaveModule", "sdg", "test", "behave", 10*"X"))
    
    text = ""
    for dirname, dirs, files in os.walk(os.path.join(DIR, "BehaveModule")):
        for fname in files:
            fpath = os.path.join(dirname, fname)
            with open(fpath, 'r') as fh:
                text = fh.read()
            text = text.replace(10*"X", mod_name)
            with open(fpath, 'w') as fh:
                fh.write(text)



if __name__ == "__main__":
    main(sys.argv)

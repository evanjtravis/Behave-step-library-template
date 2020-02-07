import os
import sys
import unittest

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

#   Begin setup.

MODNAME = "XXXXXXXXXX"

def find_test_suite():
    test_loader = unittest.defaultTestLoader
    suite = test_loader.discover('test', pattern='*.py')
    return suite


def main(argv):
    #   Standard output should be line-buffered.
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1)

    setup(
        author='Software Development Group @ Technology Services @ UIUC',
        author_email='scrum-team-d@lists.illinois.edu',
        description='',
        license='University of Illinois at Urbana-Champaign',
        long_description='',
        name=f'sdg-test-behave-{MODNAME}',
        packages=find_packages(exclude=["*tests"]),
        install_requires=[
            'addict',
            'behave',
            'deepdiff',
            'sdg-test-behave-core', # tech-services pip
            'utaw',
        ],
        package_data={
        },
        test_suite=f'sdg.test.behave.{MODNAME}.tests',
        url=f'https://github.com/techservicesillinois/test-behave-{MODNAME}/',
        version=os.environ.get('DRONE_TAG', '0.0')
    )


if __name__ == '__main__':
    sys.exit(main(sys.argv))

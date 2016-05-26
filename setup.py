import os
from setuptools import setup
from subprocess import call
from setuptools import Command
from distutils.command.build_ext import build_ext as _build_ext
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


class build_frontend(Command):
    """ A command class to run `setup.sh` """
    description = 'build front-end JavaScript and CSS'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print __file__
        call(['sh', './setup.sh'],
                cwd=os.path.dirname(os.path.abspath(__file__)))


class build_ext(_build_ext):
    """ A build_ext subclass that adds build_frontend """
    def run(self):
        self.run_command('build_frontend')
        _build_ext.run(self)


class bdist_egg(_bdist_egg):
    """ A bdist_egg subclass that runs build_frontend """
    def run(self):
        self.run_command('build_frontend')
        _bdist_egg.run(self)


class bdist_wheel(_bdist_wheel):
    """ A bdist_wheel subclass that runs build_frontend """
    def run(self):
        self.run_command('build_frontend')
        _bdist_wheel.run(self)

setup(
    name='complaintdatabase',
    version='1.2.1',
    author='CFPB',
    author_email='tech@cfpb.gov',
    maintainer='cfpb',
    maintainer_email='tech@cfpb.gov',
    packages=['complaint_common','complaint','complaintdatabase'],
    include_package_data=True,
    description=u'CCDB Landing Pages',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.md'),
    zip_safe=False,
    cmdclass={
        'build_frontend': build_frontend,
        'build_ext': build_ext,
        'bdist_egg': bdist_egg,
        'bdist_wheel': bdist_wheel,
    },
)

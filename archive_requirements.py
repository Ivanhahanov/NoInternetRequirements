import subprocess
import os
import argparse
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--create", help="create .tar with dependencies",
                    action="store_true")
parser.add_argument("-i", "--install", help="install dependencies from .tar",
                    action="store_true")
parser.add_argument("-d", "--directory", help="directory name",
                    default='dependencies')
parser.add_argument("-r", "--requirements", help="requirements.txt path",
                    default='.')
parser.add_argument("-a", "--archive", help="requirements.txt path",
                    default='dependencies.tar.gz')
args = parser.parse_args()

directory_name = args.directory
requirements_file = os.path.join(args.requirements, 'requirements.txt')


def download():
    subprocess.call(['pip', 'download', '-r', requirements_file, '-d', directory_name])


def install(package_name):
    subprocess.call(['pip', 'install', package_name, '-f', './', '--no-index'])


def archive():
    with tarfile.open(args.archive, "w:gz") as tar:
        for file in os.listdir(args.directory):
            tar.add(os.path.join(directory_name, file))


def unpack():
    with tarfile.open(args.archive, "r:gz") as tar:
        tar.extractall()


if args.create:
    print("Collecting dependencies to archive")
    download()
    print("Archiving .whl files")
    archive()
elif args.install:
    print("Unpacking archive")
    unpack()
    print("Install requirements from whl")
    for filename in os.listdir(directory_name):
        install(os.path.join(directory_name, filename))

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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar)


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

# NoInternetRequirements

Simple console python app for archive dependencies and install them without internet

## How to use

### Options

```
usage: archive_requirements.py [-h] [-c] [-i] [-d DIRECTORY] [-r REQUIREMENTS] [-a ARCHIVE]

optional arguments:
  -h, --help            show this help message and exit
  -c, --create          create .tar with dependencies
  -i, --install         install dependencies from .tar
  -d DIRECTORY, --directory DIRECTORY
                        directory name
  -r REQUIREMENTS, --requirements REQUIREMENTS
                        requirements.txt path
  -a ARCHIVE, --archive ARCHIVE
                        requirements.txt path

```

### Create an archive with .whl

First, you need to create requirements.txt with necessary requirements

For example:

```
pip freeze > requirements.txt
```

Then run script with `-c` option

```
app@app:~$ python3 archive_requirements.py -c
Collecting dependencies to archive
Collecting flask
  File was already downloaded /home/ivan/Documents/PT/Requirements/dependencies/Flask-1.1.2-py2.py3-none-any.whl
Collecting requests
  File was already downloaded /home/ivan/Documents/PT/Requirements/dependencies/requests-2.25.1-py2.py3-none-any.whl
...
```

### Install dependencies from archive

For install dependencies from archive use `-i` option

```
app@app:~$ python3 archive_requirements.py -i
chardet-4.0.0-py2.py3-none-any.whl
Defaulting to user installation because normal site-packages is not writeable
Looking in links: ./
Processing ./dependencies/chardet-4.0.0-py2.py3-none-any.whl
Installing collected packages: chardet
Successfully installed chardet-4.0.0
...
```
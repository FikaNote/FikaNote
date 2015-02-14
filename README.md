# FikaNote
ShowNote service.

[![Code Health](https://landscape.io/github/gmkou/FikaNote/master/landscape.svg?style=flat)](https://landscape.io/github/gmkou/FikaNote/master)
[![Build Status](https://travis-ci.org/gmkou/FikaNote.svg?branch=master)](https://travis-ci.org/gmkou/FikaNote)

# Requirement

- Python 2.7.x
    - Python 2.7.8 is recommended

# Setup

## Setup environments

### Mac OS X

1. Install [homebrew].
2. Run `brew install pyenv` .
3. To build python, install formula
    - `bash brew install readline; bash link readline`
    - See https://github.com/yyuu/pyenv/wiki/Common-build-problems .
4. Run `pyenv install 2.7.8` to build and install Python.
5. Run `pyenv global 2.7.8` to switch current version.
6. Setup `virtualenv`. See https://virtualenv.pypa.io/en/latest/installation.html .
    - `pip` way is recommended
7. To build psycopg2, run `brew install libpqxx`

### Ubuntu 14.04

1. Setup `pyenv`. See https://github.com/yyuu/pyenv-installer .
2. To build Python , install apt packages needed.
   - `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm` .
   - See https://github.com/yyuu/pyenv/wiki/Common-build-problems .
3. Run `pyenv install 2.7.8` to build and install Python.
4. Run `pyenv global 2.7.8` to switch current version.
5. Setup `virtualenv`. See https://virtualenv.pypa.io/en/latest/installation.html .
    - `pip` way is recommended
6. To build psycopg2, run `sudo apt-get install libpq-dev`

### Cloning repository and create venv

1. Do `git clone` for this repository.
2. Enter `FikaNote`.
3. Run `virtualenv venv` to create new environment.

# Usage

## [honcho] way

Run following command.

```
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt --allow-all-external
(venv)$ pip install honcho
(venv)$ honcho start web
```

## [foreman] way

Run following command.

([foreman] must be installed).

```
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt --allow-all-external
(venv)$ foreman start web
```

And goto `http://localhost:5000`.

# ToDo
- [X] Create mockup
- [ ] add shownote
- [ ] edit shownote
- [X] add agenda
- [X] add agenda by AJAX
- [ ] edit agenda
- [ ] delete agenda / move to shownote
- [X] Create mockup of create shownote
- [X] Solve CSRF protection error
- [X] Fix date display
- [X] Add Google Analytics
- [X] Show attendee name.
- [ ] Add Person page. (/person/<person_name>)
- [ ] Track link click. (/link/<id_url_in_agenda>)
- [ ] Add database backup script.

[homebrew]:http://brew.sh/
[honcho]:https://github.com/nickstenning/honcho
[foreman]:https://rubygems.org/gems/foreman

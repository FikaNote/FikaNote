# FikaNote
ShowNote service.

[![Code Health](https://landscape.io/github/gmkou/FikaNote/master/landscape.svg?style=flat)](https://landscape.io/github/gmkou/FikaNote/master)
[![Build Status](https://travis-ci.org/gmkou/FikaNote.svg?branch=master)](https://travis-ci.org/gmkou/FikaNote)

# Usage

Run following command.

```
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt --allow-all-external
(venv)$ foreman start web
```

And goto `http://localhost:5000`.

# Test

Run following command.

```
$ python manage.py test
```

# ToDo
- [ ] edit shownote
- [ ] edit agenda
- [ ] Add Login function(github)
- [ ] Add Person page. (/person/<person_name>)
- [ ] Track link click. (/link/<id_url_in_agenda>)
- [ ] Add database backup script.
- [ ] Add API.
- [ ] Realtime update/reflect agenda by several browser window.
		use pushpin.org?

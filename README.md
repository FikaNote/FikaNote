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

# ToDo
- [X] Create mockup
- [X] add shownote
- [ ] edit shownote
- [X] add agenda
- [X] add agenda by AJAX
- [ ] edit agenda
- [X] delete agenda / move to shownote
- [X] Create mockup of create shownote
- [X] Solve CSRF protection error
- [X] Fix date display
- [X] Add Google Analytics
- [X] Show attendee name.
- [ ] Add Login function(github)
- [ ] Add Person page. (/person/<person_name>)
- [ ] Track link click. (/link/<id_url_in_agenda>)
- [ ] Add database backup script.
- [X] Add Feed function
- [ ] Add API.
- [ ] Realtime update/reflect agenda by several browser window. 

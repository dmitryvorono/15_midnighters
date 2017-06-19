# Night Owls Detector

This project detect owl in [DEVMAN.org](https://devman.org). Owl is attempt sending after 24:00

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Also, you can add some fresh proxies in proxies.txt

# How to Launch

```bash
$ python seek_dev_nighters.py
```
Script output list owls:

```bash
[   {   'timestamp': 1497640519.740881,
        'timezone': 'Asia/Yekaterinburg',
        'username': 'СергейАнатольевич'}]
[   {   'timestamp': 1497290621.950979,
        'timezone': 'Asia/Almaty',
        'username': 'KhorinVitaly'},
    {   'timestamp': 1497286926.0,
        'timezone': 'Asia/Krasnoyarsk',
        'username': 'galbator1x'}]
[   {   'timestamp': 1497043194.0,
        'timezone': 'Europe/Moscow',
        'username': 'vgrishkin'}]
[   {   'timestamp': 1496871342.0,
        'timezone': 'Europe/Moscow',
        'username': 'СергейИванов'}]
[   {   'timestamp': 1496784501.0,
        'timezone': 'Europe/Moscow',
        'username': 'alexander.i.kamenev'},
    {   'timestamp': 1496783548.160922,
        'timezone': 'Europe/Moscow',
        'username': 'АннаБурденко'}]
[   {   'timestamp': 1496610542.0,
        'timezone': 'Europe/Moscow',
        'username': 'KonstantinNaumov'},
    {   'timestamp': 1496440149.0,
        'timezone': 'Europe/Moscow',
        'username': 'alexander.i.kamenev'},
    {   'timestamp': 1496427376.283521,
        'timezone': 'Asia/Almaty',
        'username': 'KhorinVitaly'}]
[   {   'timestamp': 1496342321.0,
        'timezone': 'Asia/Almaty',
        'username': 'KhorinVitaly'}]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

# bluetooth-bed-occupancy-sensor

A raspberry pi positioned under my bed that polls the bluetooth signal strength of my Xiaomi Mi Band.

# Prerequisites

A raspberry pi with:

- git installed
- python3 installed
- python3-pip installed

# Setup

Clone this repo to your pi

```
$ git clone https://github.com/KReusen/bluetooth-bed-occupancy-sensor.git
```

Open the folder, create a virtual environment, activate it
and install the requirements

```
$ cd bluetooth-bed-occupancy-sensor
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

Install bluepy from source

```
$ sudo apt-get install git build-essential libglib2.0-dev
$ cd src
$ git clone https://github.com/IanHarvey/bluepy.git
$ cd bluepy
$ python setup.py build
$ sudo python setup.py install
```

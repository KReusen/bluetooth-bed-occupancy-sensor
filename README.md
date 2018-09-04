# bluetooth-bed-occupancy-sensor

A raspberry pi positioned under my bed that polls the bluetooth signal strength of my Xiaomi Mi Band.

# Prerequisites

A raspberry pi with:

- git installed
- python3 installed
- python3-pip installed

# Setup

Install a helper for bluepy

```
$ sudo apt-get install libglib2.0-dev
```

Clone this repo to your pi

```
$ git clone git@github.com:KReusen/bluetooth-bed-occupancy-sensor.git
```

Open the folder, create a virtual environment, activate it
and install the requirements

```
$ cd bluetooth-bed-occupancy-sensor
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

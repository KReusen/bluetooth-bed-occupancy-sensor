# bluetooth-bed-occupancy-sensor

A raspberry pi positioned under my bed that polls the bluetooth signal strength of my Xiaomi Mi Band and compares it to a predefined threshold. Every 30 seconds the script will publish a message to a mqtt topic updating the state, ie:

```
{
    "bed_occupied": true
}
```

In my setup this mqtt message is then picked up by Home Assistant where I use it in a Anti-Snooze feature I built.

# Prerequisites

A raspberry pi with:

- git installed
- python3.6+ installed (see https://www.scivision.co/compile-install-python-beta-raspberry-pi/ )
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
$ git clone https://github.com/IanHarvey/bluepy.git
$ cd bluepy
$ python setup.py build
$ sudo python setup.py install
```

Move bluepy module to correct place and clean up the rest

```
$ mv bluepy/bluepy/ src/bluepy/
$ sudo rm -rf bluepy/
```

Make bluepy executable with root privileges by any user:

```
$ sudo setcap 'cap_net_raw,cap_net_admin+eip' src/bluepy/bluepy-helper
```

[Optional] Add your rollbar token to `~/.bashrc` to be able to log errors

```
export ROLLBAR_TOKEN=abcdefgh
```

# Run

```
$ cd src
$ python main.py aa:a1:bb:11:22:22
```

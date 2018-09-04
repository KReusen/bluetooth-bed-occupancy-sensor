import os
from bluepy.btle import Scanner, DefaultDelegate


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
mac = os.environ.get('MAC_TO_TRACK')


for dev in devices:
    if dev.addr == mac:
        print(dev.rssi)

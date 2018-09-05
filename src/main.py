import os
import click
from scanner import BLEScanner


@click.command()
@click.argument('mac_address')
def scan(mac_address: str):
    ble_scanner = BLEScanner()
    rssi = ble_scanner.get_rssi_for_mac(mac_address)
    print(rssi)


if __name__ == "__main__":
    scan()

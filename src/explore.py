""" Scans continuously for a mac address and prints it's distance to the console """

import os
import click

from scanner import BLEScanner
from occupancy_service import OccupancyService
from mqtt_service import MQTTService


@click.command()
@click.argument('mac_address')
@click.argument('scan_timeout', type=float)
def explore(mac_address: str, scan_timeout: float) -> None:
    scanner = BLEScanner(scan_timeout)

    while True:
        distance = scanner.get_distance_for_mac(mac_address)
        print(distance)


if __name__ == "__main__":
    explore()

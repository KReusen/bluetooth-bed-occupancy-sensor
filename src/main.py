import os
import rollbar
import click

from scanner import BLEScanner
from occupancy_service import OccupancyService
from mqtt_service import MQTTService

rollbar_token = os.environ.get('ROLLBAR_TOKEN')
if rollbar_token is not None:
    rollbar.init(rollbar_token)


@click.command()
@click.argument('mac_address')
@click.argument('threshold', type=int)
@click.argument('mqtt_address')
@click.argument('mqtt_topic')
def report_bed_occupancy(mac_address: str, threshold: int, mqtt_address: str, mqtt_topic: str) -> None:
    scanner = BLEScanner(timeout=10.0)
    occupancy_service = OccupancyService(threshold=threshold)
    mqtt_service = MQTTService(address=mqtt_address, topic=mqtt_topic)

    while True:
        distance = scanner.get_average_distance_for_mac(
            mac_address=mac_address,
            measurements=3
        )
        occupied = occupancy_service.in_range(distance=distance)
        mqtt_service.publish({
            "bed_occupied": occupied
        })


if __name__ == "__main__":
    report_bed_occupancy()

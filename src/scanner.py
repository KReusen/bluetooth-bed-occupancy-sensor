from typing import List, Optional
from bluepy.btle import Scanner, DefaultDelegate, ScanEntry


class BLEScanner():
    def __init__(self, timeout: float = 10.0):
        self.scanner = Scanner().withDelegate(DefaultDelegate())
        self.timeout = timeout

    def _scan_devices(self) -> List[ScanEntry]:
        return self.scanner.scan(self.timeout)

    def get_rssis(self) -> dict:
        """ Returns the strength of the scanned devices signals as seen by 
        this device. Ranges from 0 (close) to -100 (far)
        """
        devices = self._scan_devices()
        return {dev.addr: dev.rssi for dev in devices}

    def get_distance_for_mac(self, mac_address: str) -> Optional[int]:
        """ Returns a rssi transformed to a positive integer"
        """
        devices = self._scan_devices()
        rssis = {dev.addr: dev.rssi for dev in devices}
        return abs(rssis.get(mac_address))

    def get_average_distance_for_mac(self, mac_address: str, measurements: int = 3) -> Optional[int]:
        rssis = []
        for _ in range(measurements):
            rssi = self.get_distance_for_mac(mac_address)
            rssis.append(rssi)

        numerical_rssis = [r for r in rssis if isinstance(r, int)]
        if not numerical_rssis:
            return None

        return round(sum(numerical_rssis) / len(numerical_rssis))

class OccupancyService():
    def __init__(self, threshold: int):
        self.threshold = threshold

    def in_range(self, distance: int) -> bool:
        if distance > self.threshold:
            return False
        return True

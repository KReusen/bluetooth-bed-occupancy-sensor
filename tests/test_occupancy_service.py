from occupancy_service import OccupancyService


class TestOccupancyService:
    def test_in_range_further_than_threshold(self):
        occupancy_service = OccupancyService(threshold=50)
        distance = 60
        in_range = occupancy_service.in_range(distance)
        assert in_range == False

    def test_in_range_closer_than_threshold(self):
        occupancy_service = OccupancyService(threshold=50)
        distance = 40
        in_range = occupancy_service.in_range(distance)
        assert in_range == True

    def test_in_range_equal_to_threshold(self):
        occupancy_service = OccupancyService(threshold=50)
        distance = 50
        in_range = occupancy_service.in_range(distance)
        assert in_range == True

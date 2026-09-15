class Vehicle:
    def __init__(self, number, vehicle_type):
        self.number = number
        self.vehicle_type = vehicle_type


class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def park(self, vehicle):
        if self.vehicle is None and self.spot_type == vehicle.vehicle_type:
            self.vehicle = vehicle
            return True
        return False

    def remove(self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle


class ParkingLot:
    def __init__(self):
        self.spots = [
            ParkingSpot(1, "car"),
            ParkingSpot(2, "car"),
            ParkingSpot(3, "bike")
        ]

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.park(vehicle):
                print(f"{vehicle.number} parked at spot {spot.spot_id}")
                return True
        print(f"{vehicle.number} could not be parked")
        return False

    def remove_vehicle(self, spot_id):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                return spot.remove()
        return None


# Example usage
car1 = Vehicle("KA-01-1234", "car")
car2 = Vehicle("KA-02-5678", "bike")
parking_lot = ParkingLot()
parking_lot.park_vehicle(car1)
parking_lot.park_vehicle(car2)

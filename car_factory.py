from car import Car
from engine.engine import Engine
from battery.battery import Battery

class CarFactory(Car, Engine, Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        pass
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        pass
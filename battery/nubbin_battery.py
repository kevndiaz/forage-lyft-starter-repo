from battery.battery import Battery

class NubbinBattery():
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        
    def needs_service(self):
        pass
from datetime import date, datetime 

class CustomDate(date):

    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    def serialize(self) -> str: 
        return (f'{self.day}/{self.month}/{self.year}')

    def deserialize(self) -> date:
        pass 
from House import House

class Vile(House):
    def __init__(self, address, size, rooms, yard):
        super().__init__(size, rooms)
        self.address = address
        self.yard = yard
        
    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False
  
    def __str__(self):
        if(self.yard=='T'):
            return '{}에 위치해 있는 {}개의 방이 있고 마당이 있는 {}평의 주택입니다.'.format(self.address, self.rooms, self.size)
        else:
            return '{}에 위치해 있는 {}개의 방이 있고 마당은 없는 {}평의 주택입니다.'.format(self.address, self.rooms, self.size)
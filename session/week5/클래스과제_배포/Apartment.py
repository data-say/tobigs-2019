from House import House

class Apartment(House):
    def __init__(self, dong_ho, size, rooms):
        super().__init__(size, rooms)
        self.dong_ho = dong_ho
        
    def __lt__(self, other):
        if self.size < other.size:
            return True
        else:
            return False
        
    def __eq__(self, other):
        if self.size == other.size:
            return True
        else:
            return False
        
    def __str__(self):
        return '{}동 {}호의 {}개의 방이 있는 {}평의 아파트입니다.'.format(self.dong_ho.split('-')[0], 
                                                         self.dong_ho.split('-')[1], self.rooms, self.size)
        
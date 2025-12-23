from incomplete import Transportation

class Taxi(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)

    def find_cost(self):
        return 40*self.distance

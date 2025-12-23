from incomplete import Transportation

class Train( Transportation ):

   def __init__( self, start, end, distance, stations ):
        Transportation.__init__( self, start, end, distance)
        self.stations = stations

   def find_cost( self ):
      return (self.stations) * 5
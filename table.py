""" In this file, we determine the tables of the project by using classes. 
First, the Seat, to know if the seat is free and what is the name of his occupant if there's one
Second, the Table, to know how many seats are available and allow to assign people to a table"""


class Seat :
    #we define attributes and their types
    def __init__(self, free : bool, occupant : str) :
        self.free = free
        self.occupant = occupant
    def __str__(self):
        return "The seast is {self.free} and it is not free there's {self.occupant}in it".format(self=self)
    #we see if the seat is available and put somebody on it if free
    def set_occupant(self, name : str) :
        if self.free == True :
            self.occupant = name
            return self.free == False
    #forget about this one!
    def remove_occupant(self) :
        if self.free != True :
            return self.free == True



class Table :
    #we define the attributes and their types
    def __init__(self, capacity : int, seats):
        self.capacity = capacity
        self.seats = seats
        seats = []
        for seat in capacity :
            self.seats.append(seat)

    #to see if a seat is available in the table
    def has_free_spot(self) :
        if len(self.seats) > 0 :
            return True
        else :
            return False
    
    def assign_seat(self,name) :
        if self.has_free_spot(True) :
            self.seats.

    

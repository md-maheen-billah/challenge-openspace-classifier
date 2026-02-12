class Seat:
    """
    This class is that of a single seat in a table

    Attributes:
        __free (bool): Whether the seat is free or not
        __occupant (bool): Name of the person on the seat
    """
    def __init__(self):
        """
        Constructor for Seat
        """
        self.__free = True #setting as True by default
        self.__occupant = None #setting as None by default

    @property
    def free(self):
        """
        bool: Returns True when seat is Free
        """
        return self.__free
    
        
    @property
    def occupant(self):
        """
        str\None: Returns the name if seat is taken, else returns None.
        """
        return self.__occupant
    
        
    def set_occupant(self,name):
        """
        This method sets a person to the seat

        name (str): Name of the person to be set on the seat
        """
        if self.__free:
            if isinstance(name, str):  #if true we will set someone to the seat
                self.__occupant = name
                self.__free = False #we will also ahve to make sure we set that particular seat to false after assigning a person
            else:
                raise ValueError("Name must be string")
        else:
            print("Seat is occupied") #we will print this incase the seat is occupied

    def remove_occupant(self):
        """
        This method removes a person from the seat
        """
        if not self.__free: #if a seat is not free, that means someone is on it, that way we can remove the person
            name = self.__occupant
            self.__occupant = None
            self.__free = True #again we made sure to set the availibity of the seat to true
            return name
        else:
            print("There is no one to remove from seat")
            return None
        
    def __str__(self):
        """
        Returns the status of the seat in string
        """
        if self.__free:
            return "Seat is free"
        else:
            return f"Seat is occupied by {self.__occupant}"
    







class Table:
    def __init__(self):
        self.capacity = 4
        self.seats = []             
        for _ in range(self.capacity):
            self.seats.append(Seat())

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False
            
    def assign_seat(self,name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return
        print("No seat available")

    def left_capacity(self):
        count = 0
        for seat in self.seats:
            if seat.free:
                count += 1
        return count
    
    def __str__(self):
        print_seat = []
        for seat in self.seats:
            if seat.free:
                print_seat.append("Free")
            else:
                print_seat.append(seat.occupant)
        return f"{print_seat[0]} | {print_seat[1]} | {print_seat[2]} | {print_seat[3]}"
    


        

class Seat:
    def __init__(self,free,occupant):
        self.__free = True
        self.__occupant = None

    @property
    def free(self):
        return self.__free
    
        
    @property
    def occupant(self):
        return self.__occupant
    
        
    def set_occupant(self,name):
        if self.__free:
            if isinstance(name, str):
                self.__occupant = name
                self.__free = False
            else:
                raise ValueError("Name must be string")
        else:
            print("Seat is occupied")

    def remove_occupant(self):
        if not self.__free:
            name = self.__occupant
            self.__occupant = None
            self.__free = False
            return name
        else:
            print("There is no one to remove from seat")
            return None
        
    def __str__(self):
        if self.__free:
            return "Seat is free"
        else:
            return f"Seat is occupied by {self.__occupant}"
    
class Table:
    def __init__(self):
        self.capacity = 4
        self.seats = [Seat(), Seat(), Seat(), Seat()]

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
            else:
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

        

import random #we imported this so we can use to randomize the people in the list
import csv
from utils.table import Table #had to import the class Table from table.py so can we can use it for objects inside class Openspace

class Openspace:
    """
    This class is the openspace where the 6 tables with 4 seats each will exist

    Attributes:
        number_of_tables (int): Total tables in the open space set as 6 by default.
        tables (list of Table): List containing Table objects.
    """
    def __init__(self):
        """
        Constructor for Openspace
        """
        self.number_of_tables = 6 #set 6 as default
        self.tables = []             
        for _ in range(self.number_of_tables): #using loop to append 6 Table objects inside the list self.tables
            self.tables.append(Table())

    def organize(self,names):
        """
        This method randomly sits people across different tables.
        We made use of a library named random to shuffle the names inside the list names.
        """
        random.shuffle(names)

        index = 0 
        for table in self.tables: #here we looped through each table to check for the seats
            for seat in table.seats: #here we looped through each seat on a table to set and set a person
                if index < len(names): 
                    seat.set_occupant(names[index]) #after randomizing the name list we make everyone seat on the table ony by one from position 0  to 23
                    index += 1
                else:
                    return
    
    def display(self):
        """
        This method display all the tables along with the people seating on them.
        """
        count = 1
        for table in self.tables:
            print_seat = []
            for seat in table.seats:
                if seat.free:
                    print_seat.append("Free") #incase no one is seating on it, we are denoting as a Free seat
                else:
                    print_seat.append(seat.occupant)
            print(f"Table {count}: {print_seat[0]} | {print_seat[1]} | {print_seat[2]} | {print_seat[3]}")
            count += 1

    def store(self, filename):
        """
        This method is used to store the data we genrated after randomly assigning everyone a seat, therefore the seating
        order and saving it in a .csv file
        """
        data = [] 
        table_number = 1 #we start by assigning table numbers
        for table in self.tables:
            row = []
            for seat in table.seats:
                if seat.free:
                    row.append("")  # empty string for free seat
                else:
                    row.append(seat.occupant)
            data.append(["Table" + str(table_number)] + row)
            table_number += 1

        dataframe = pd.DataFrame(data, columns=["Table", "Seat 1", "Seat 2", "Seat 3", "Seat 4"])

        dataframe.to_csv(filename, index=False)

        print("Stored as an excel file-> " + filename)

    def store(self, output_filename): 
        """
        This method is used to store the data we genrated after randomly assigning everyone a seat, therefore the seating
        order and saving it in a .csv file
        """
        with open(output_filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            table_no = 1
            for table in self.tables:
                seated_names = ["Table "+str(table_no)]
                for seat in table.seats:
                    seated_names.append(seat.occupant) 
                writer.writerow(seated_names)
                table_no += 1


        
    

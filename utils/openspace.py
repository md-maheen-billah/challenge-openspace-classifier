import random
import pandas as pd
from table import Table

class Openspace:
    def __init__(self):
        self.number_of_tables = 6
        self.tables = []             
        for _ in range(self.number_of_tables):
            self.tables.append(Table())

    def organize(self,names):
        random.shuffle(names)

        index = 0
        for table in self.tables:
            for seat in table.seats:
                if index < len(names):
                    seat.set_occupant(names[index])
                    index += 1
                else:
                    return
    
    def display(self):
        count = 1
        for table in self.tables:
            print_seat = []
            for seat in table.seats:
                if seat.free:
                    print_seat.append("Free")
                else:
                    print_seat.append(seat.occupant)
            print(f"Table {count}: {print_seat[0]} | {print_seat[1]} | {print_seat[2]} | {print_seat[3]}")
            count += 1

    def store(self, filename="output.csv"):
        data = []
        table_number = 1
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
    
names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah",
    "Sophia", "Oliver", "Isabella", "Lucas", "Mia", "Mason",
    "Amelia", "Ethan", "Harper", "Logan", "Evelyn", "James",
    "Abigail", "Benjamin", "Charlotte", "Alexander", "Ella", "Henry"
]
          
org = Openspace()
org.organize(names)
org.store()

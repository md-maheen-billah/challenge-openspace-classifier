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
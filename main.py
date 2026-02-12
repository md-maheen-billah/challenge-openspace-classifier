from utils.openspace import Openspace
from utils import file_utils

input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

# creates a list that contains all the colleagues names
names = file_utils.read_names_from_csv(input_filepath)

 # create an OpenSpace()
open_space = Openspace()

# assign a colleague randomly to a table
open_space.organize(names)

 # save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()

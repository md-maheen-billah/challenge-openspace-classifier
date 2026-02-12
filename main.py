from utils.openspace import Openspace
from utils import file_utils
input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

names = file_utils.read_names_from_csv(input_filepath)

open_space = Openspace()

open_space.organize(names)

open_space.store(output_filename)

open_space.display()

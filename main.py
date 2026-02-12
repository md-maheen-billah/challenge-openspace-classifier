from utils.openspace import Openspace
from utils import file_utils
input_filepath = "new_colleagues.csv"

names = file_utils.read_names_from_csv(input_filepath)

open_space = Openspace()

open_space.organize(names)

open_space.store()

open_space.display()

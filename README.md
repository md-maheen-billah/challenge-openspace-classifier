# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

As part of my training at BeCode, I developed this project to practice object-oriented programming concepts in Python.

The scenario simulates a company working in an open space office with six tables of four seats each. To encourage collaboration and help colleagues get to know each other better, the seating arrangement is randomized daily.

Each time the script runs, it assigns everyone to a new seat, demonstrating the use of classes, objects, encapsulation, and file handling in a practical, real-world inspired example

![coworking_img](https://i.ibb.co/KjdCZVHy/Chat-GPT-Image-Feb-12-2026-04-38-30-PM.png)


## 💡 OOP Concepts Used

This project demonstrates several key OOP principles:

Classes and Objects – Seat, Table, and Openspace classes were created to model real-world entities.

Encapsulation – Private attributes (e.g., __free, __occupant) are used to protect internal state.

Abstraction – Methods such as set_occupant(), left_capacity(), organize(), and store() hide internal implementation details.

Composition – An Openspace contains multiple Table objects, and each Table contains multiple Seat objects.

Special Methods – __str__() is implemented for readable object representation.


## 📦 Libraries Used

The project uses the following Python libraries:

 - random – To shuffle the list of names and create randomized seating.
 - pandas – To read input files (CSV/Excel) and store the seating arrangement as a CSV file.
 - csv (optional alternative) – For handling CSV file operations.


## 📦 Repo structure

```
.
├── utils/
│   ├── file_utils.py
│   ├── openspace.py
│   └── table.py
├── main.py
├── new_colleagues.csv
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/md-maheen-billah/challenge-openspace-classifier.git
    cd challenge-openspace-classifier
    pip install pandas
    python main.py
    ```

2. In order to run the script, execute the `main.py` file from your terminal:

    ```bash
    python main.py
    ```
    

3. The script requires input file, and organizes colleagues to random seat assignments. The resulting seating plan is displayed in the console and also saved to an "output.csv" file in the root directory. 

```python
input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

# Creates a list that contains all the colleagues names
names = file_utils.read_names_from_csv(input_filepath)

# create an OpenSpace()
open_space = OpenSpace()

# assign a colleague randomly to a table
open_space.organize(names)

# save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()
```
## ⏱️ Timeline

This project took 5 hours for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/md-maheen-billah/).


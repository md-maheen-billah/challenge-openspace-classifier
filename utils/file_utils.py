import pandas as pd #imported so that we can take all the names inside the excel file and put it inside a list

def read_names_from_csv(file_path):
    """
    Reads names from a CSV or Excel file and putsthem as a inside a list of strings.

    How it works:
        - Attempts to read the file as a CSV first.
        - If CSV reading fails, attempts to read the file as an Excel file.
        - Extracts values from the first column.
        - Removes leading/trailing whitespace from each name.
        - Ignores empty or blank entries.
    """

    try:
        dataframe = pd.read_csv(file_path, header=None) #for csv
    except:
        dataframe = pd.read_excel(file_path, header=None) #for excel
    

    raw_names = dataframe[0].tolist()
    
    names = []
    for name in raw_names:
        clean_name = str(name).strip()
        if clean_name != "":
            names.append(clean_name)

    return names
    

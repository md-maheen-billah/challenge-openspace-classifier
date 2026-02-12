import pandas as pd

def read_names_from_csv(file_path):

    try:
        dataframe = pd.read_csv(file_path, header=None)
    except:
        dataframe = pd.read_excel(file_path, header=None)
    

    raw_names = dataframe[0].tolist()
    
    names = []
    for name in raw_names:
        clean_name = str(name).strip()
        if clean_name != "":
            names.append(clean_name)

    return names
    

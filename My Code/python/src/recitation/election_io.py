import csv

def process_electoral_votes(file_path):
    print(file_path)
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            state = row[0]
            votes = row[1]
            print(row)
            
            
def process_polling_data(file_path):
    """
    Takes in file path with polling data and returns a dictionary mapping states to results of candidate 1.
    """
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            state = row[0]
            
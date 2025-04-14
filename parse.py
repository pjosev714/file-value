import csv


def parse_file(file_path):
    """
    Parses a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    with open(file_path, 'r') as file:
        store = csv.DictReader(file)
        for row in store:
            print(row['color'], row['fruit'])
    

if __name__ == "__main__":
    # Example usage
    file_path = 'key-value.csv'
    parse_file(file_path)
    # Output: color fruit
    #         red apple
    #         yellow banana
    #         green grape
    #         blue blueberry
import csv


def parse_file_to_dict(file_path):
    """
    Parses a CSV file into a dictionary and returns the key-value pairs.
    """
    with open(file_path, 'r') as file:
        store = csv.reader(file)
        dict_store = dict(store)
    
        return dict_store

if __name__ == "__main__":
    # Example usage
    fruit_file = 'key-value.csv'
    #parse_file_to_dict("key-value.csv")
    parse_file_to_dict(fruit_file)
    # Output: color fruit
    #         red apple
    #         yellow banana
    #         green grape
    #         blue blueberry


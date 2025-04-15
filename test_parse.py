from parse import parse_file_to_dict  


def test_parse_file_to_dict():
    file_path = 'key-value.csv'
    expected = {'color': 'fruit', 'green': 'papaya', 'yellow': 'banana', 'orange': 'orange'}
    response = parse_file_to_dict(file_path) 
    assert response, expected
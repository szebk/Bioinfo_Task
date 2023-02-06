def read_tsv(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip().split("\t"))
    return data

def extract_last_column(data):
    last_column = [row[-1] for row in data]
    return last_column

def remove_header(data):
    header = data[0]
    data.remove(header)
    return data

def sort_values(data):
    return sorted(data)

def print_values(data):
    for value in data:
        print(value)

if __name__ == '__main__':
    file_name = "expmat.tsv"
    data = read_tsv(file_name)
    last_column = extract_last_column(data)
    data = remove_header(data)
    last_column = sort_values(last_column)
    print_values(last_column)

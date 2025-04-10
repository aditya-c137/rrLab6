with open(data_path + 'labels.txt', 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)

for line in lines:
    # read image
    
    for i in range(5):
        #read image
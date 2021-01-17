def swapFileData():
    file1 = input("Which file would you like to swap: ")
    file2 = input("Which file would you llike to swap: ")
    with open(file1, 'r') as a: 
        data_a = a.read()
    with open(file2, 'r') as a: 
        data_b = a.read()
    with open(file1,'w') as a: 
        a.write(data_b)
    with open(file2,'w') as a: 
        a.write(data_a)
swapFileData()

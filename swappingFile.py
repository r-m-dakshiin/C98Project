


def swapFileData():
    file1name = input("Enter file name 1 : ")
    file2name = input("Enter file name 2 : ")
    
    
    file1 = open('sample1.txt', 'r')
    data_a = file1.read()


    file2 = open('sample2.txt', 'r')
    data_b = file2.read()


    file1.close()
    file2.close()


    file1 = open('sample1.txt', 'w')
    file1.write(data_b)


    file2 = open('sample2.txt', 'w')
    file2.write(data_a)

    print(file1name + " text : " + data_a)
    print(file2name + " text : " + data_b)
    
    file1.close()
    file2.close()

swapFileData()
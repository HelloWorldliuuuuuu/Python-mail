import csv

file ='staff_data.csv'

print(file)
to_addr =  ''

with open(file, "r") as csv_file:
    read = csv.reader(csv_file)
    # read对象，是一个列表的格式
    # read对象的一个迭代器，可以通过next()取出其中的元素
    next(read)
    # 也可以通过for循环取出所有元素
    for line in read:
        to_addr1 =line[0]
        to_addr2 =line[1]
        print (line[1])
         

my_list = [1,2,3,4,5]

my_file = open("file.txt","w")

for items in my_list:
    my_file.write(str(items) + '\n')
my_file.close()
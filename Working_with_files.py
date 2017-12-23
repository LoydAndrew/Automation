my_list = [1,2,3,4,5]

my_file = open("file.txt","w")
print("Writing list of 5 items")

for items in my_list:
    my_file.write(str(items) + '\n')
my_file.close()
print("Reading one_line")

my_file_new = open("file.txt","r")
print (str(my_file_new.readline()))
my_file_new.close()

print('with as construction reading all file')
with open('file.txt','r') as f: #with as doesn't need to close file
    print(str(f.read()))

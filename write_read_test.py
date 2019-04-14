#from sys import argv

#file_name,write_test = argv

write_test = open("write_test.txt",'w')
write_test.write("가나다라마바")
write_test.close()

read_test = open("write_test.txt",'r')
print(read_test.read())
read_test.close()

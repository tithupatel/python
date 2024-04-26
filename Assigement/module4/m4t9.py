#Write a python program to find the longest words.

path = "C:\\Users\\Lenovoṇ\\OneDrive\\Desktop\\python\\python23\\Assigement\\module4\\Module – 4 (Advance python programming)\\file.txt"

f = open(path,'r')
s = f.read()

lst = s.split()

print(s)
print("\nLongest Word in a File is :",max(lst,key=len))

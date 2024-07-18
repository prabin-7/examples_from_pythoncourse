
with open('D:/dev/Python/module4/my.txt','r') as file1:
    print(file1.name)
    # file1.mode
    FileContent = file1.readlines(6) # reads each line if the req quota toches even 1 character of the line
#the \n character is counted in by the len fxn but not counted by the readlines() fxn
#  readline() vs readlines()
# readline(39) - prints the 39 characters from the first line or the no of lines looped
# readlies(39) - prints the line touching the 39 th characters
# when th total no characters in the line are 71 then while using readlines(39) it will print the next line 
# as well because the index for the counting starts from 0 in python but the len fxn starts from 1   

    # FileContent
    # print(FileContent)



# count the no of character printed
count_characters = 0 
for line in FileContent:
    element = []
    element = line 
    print(line)
    print(type(line),'this is loop')
    c2 = len(element)
    count_characters += c2
print(count_characters) 

#print the content of the loop
print(type(FileContent))
print(FileContent)
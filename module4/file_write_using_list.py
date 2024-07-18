lines = ['This is line 1\n','This is line 2\n','This is line 3\n','This is line 4\n','This is line 5\n',]
with open('D:/dev/Python/module4/created_file.txt','w') as file2:
    for line in lines:
        file2.write(line) 
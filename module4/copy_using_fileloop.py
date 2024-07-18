with open('D:/dev/Python/module4/my.txt','r') as file1:
    with open('D:/dev/Python/module4/copied_file.txt','w') as file2:
              for line in file1:
                     file2.write(line)

import pandas as pd
with open('D:/dev/Python/module4/my.txt','r') as file1:
    print(file1.name,file1.mode)
    # file1.mode
    FileContent = file1.read()
    FileContent
    # print(FileContent)
print(type(FileContent))
file1.closed




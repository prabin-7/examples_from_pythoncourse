  
'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    with open(currentMem,'r+') as active:
        with open(exMem,"a+") as ex:
            list_1 = active.readlines()
            # print (list)
            header = list_1[0]
            del list_1[0]
            print (list_1)
            inactive = []
            for member in list_1:
                if 'no' in member:
                    inactive.append(member)
            active.seek(0)
            active.write(header)
            for mem in list_1:
                if mem in inactive:
                    ex.write(mem)
                else:
                    active.write(mem)
            active.truncate()       #need truncate as the file is opened in r+ mode
    
    pass # Remove this line when done implementation


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
    
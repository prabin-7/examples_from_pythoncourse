count = 1
while count < 5:
 print(count)
 count += 1


dates = [1982,1993,1887,1778,1998,1993,1985,2000]

i=0
year = dates[0]
while(year!= 2000):
 print(year)
 i=i+1
 year=dates[i]

print('it took ', i ,'iterations to get out of the loop.')
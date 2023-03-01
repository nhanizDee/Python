#Nhan Nguyen
#Date; Feb 27, 2023
#Nested loop print


#declare

character = '*'
size = 7

#making the condition to check for the size of the expection table with row and column
for row in range(size):                            #row equal 7
    for col in range(size, row, -1):               #col in the table have 7 row is akso equal 7, with column decrase
        print(character, end='')                   #print the charactor and using end='' to jump to next row
    print()                                        #print the rest
        
    

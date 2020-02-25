#------------------------------------------#
"""
Title      : <CDInventory.py
Description: Use of dictionaries, functionality to load and delete data
Change log : Eliana Arias-Dotson, 
Created on Sat Feb 22 04:18:52 2020
Edited on Sun Feb 23 04:10:03 2020
Edited on Mon Feb 24 11:24:03 2020
"""
#------------------------------------------#
# Used later as as suggestion
import os.path
# Declare variable

strChoice = '' # User input
lstTbl = [] # list of lists to hold data
dicRow = {} # list of data row
strFileName = 'CDInventory.txt'  # data storage file # this is a comma separated
objFile = None  # file object
headerRow = ['ID (Integer)','CD Title (String)', 'Artist Name (String)']

# Get user Input
print('\n\n')
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        #Exit the program if the user chooses so
        print('\nGood-bye')
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        print('You current inventory list:')
        print("{:20}{:20}{:20}".format(*headerRow))
        print('==========================================')
        if os.path.exists("CDInventory.txt"):
            with open('CDInventory.txt', 'r') as f:
                # Since not saving the raw list, but saving as comma separated
                # We split on comma and remove trailing newline characters.
                CDInv = [list(map(str, line.strip().split(','))) for line in f]
                #Loop through it and display each element formatted.
                for cd in CDInv:
                    print("{:20}{:20}{:20}".format(*cd))
                    print('==========================================')
                             
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        intID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID': intID, 'Artist': strTitle, 'Title:':strArtist}
        lstTbl.append(dicRow)    
        
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        # First we'll print our header row and format the output
        print("{:20}{:20}{:20}".format(*headerRow))
        # Then we loop through the inventory
        for cd in lstTbl:
        # The print out each cd, each field has a length of 20, and the int id is left justified
             print('{:20}{:20}{:20}'.format(*cd.values()) )  

    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print("Current Inventory")
        print("{:20}{:20}{:20}".format(*headerRow))
        for cd in lstTbl:
             print('{:20}{:20}{:20}'.format(*cd.values()) ) 
        #Ask option on what to remove from Current inventory
        #Option 1:
#        IdtoDel=''
#        IdtoDel= int(input('Remove entry with this ID:')) 
#        delete = [value for value in lstTbl if value == IdtoDel] 
#        for value in delete: del lstTbl[value]
#        print(lstTbl)
        #Option 2:
        delete = [] 
        IdtoDelete=int(input('Remove entry with this ID:')) 
        for key, val in dicRow.items(): 
            if val == IdtoDelete: 
                delete.append(key) 
        for i in delete: 
            del dicRow[i] 
      # Modified Dictionary      
        print(dicRow)       
#        EntrytoDel=0
#        for cd in lstTbl:
#            if IdtoDel in cd.values():
#                lstTbl.remove(EntrytoDel)
#                print("Entry has been removed")
    elif strChoice == 's':
        # Save the data to a text file CDInventory_Assig05.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')


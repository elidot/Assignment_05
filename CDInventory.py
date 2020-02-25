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
        objFile=open(strFileName,'r')
        for row in objFile:
            oldcd=row.strip('\n').split(',')
            dicRow = {'ID': int(oldcd[0]), 'Artist': oldcd[1], 'Title:':oldcd[2]}
            lstTbl.append(dicRow)
        objFile.close() 
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        intID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID': intID, 'artist': strTitle, 'title:':strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print("Current Inventory")
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')  
        #Ask option on what to remove from Current inventory
        IdtoDel=''
        IdtoDel= int(input('Remove entry with this ID:')) 
        EntrytoDel=0
        for cd in lstTbl:
            if IdtoDel in cd.values():
                lstTbl.remove(EntrytoDel)
                print("Entry has been removed")
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

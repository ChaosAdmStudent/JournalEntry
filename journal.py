'''

This program deals with making journals! 
Things it can do: 

$ Allow users to create/delete journal entries referenced by the date.
$ Allow users to edit a particular day's entries referenced by the date 
$ Makes files that are categorized under folders on the basis of months ( Jan, Feb etc) 
 
'''

import datetime 
import os

current =   datetime.datetime.now() 

def multilines():
    buffer = []
    print('Starting inputting your journal entry!') 
    print('When you are done, simply press type \".\" in the next immediate line') 
    while True:
        print("> ",end="") 
        line = input() 
        if line == ".":
            break 
        buffer.append(line)
        
    return '\n'.join(buffer)

class Diary: 

    def check_entry_existence(self):
        try: 
            self.entry = open(self.filepath)
        except:
            return False
        else:
            self.entry.close()
            return True
    
    def __init__(self, date, month):
        self.date = date
        self.month = month
        self.filepath = f"C:/Users/lakshya/Documents/My_Workspace/Milestone Projects/Final Capstone Projects/Journal_Entries/{datetime.date.today()}"
    
    def add_entry(self):
        self.entry = open(self.filepath, 'w')
        paragraph = multilines()
        
        self.entry.write(paragraph) 
        self.entry.close()
    
    def read_entry(self):
        self.entry = open(self.filepath)
        self.entry.seek(0)
        
        for line in self.entry:
            print(line)
    
        self.entry.close()
    def edit_entry(self):
        self.entry = open(self.filepath,'a+')
        paragraph = multilines()
        self.entry.write('\n') 
        self.entry.write(paragraph)
        self.entry.close()
    
    def remove_entry(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
            print("Deleted today's entry!")
        else:
            print('Entry does not exist!')

if __name__ == '__main__':
    print('Welcome to my journal entry program!') 
    print('The program arranges all the entries in files!') 
    print('Choose from the following in my Command Line: ')
    print('\t1: Add ')
    print('\t2: Edit')
    print('\t3: Read')
    print('\t4: Delete') 
    print('\t5: Exit')  
    
    while(True):
        option = ''
        while (option.lower()!='add' and option.lower()!='edit' and option.lower()!='read' and option.lower()!='delete' and option.lower()!='exit'):
            print('Please choose from one of the 5 operations available to this program!')
            option = input('> ')
        page = Diary(str(current.day),str(current.month)) 

        if option.lower() == 'add': 
            if page.check_entry_existence() == True: 
                print('The journal entry for today has already been made! Try editing/reading instead!')
            else:
                page.add_entry() 
        if option.lower() == 'edit': 
            if page.check_entry_existence() == True: 
                page.edit_entry() 
            else:
                print('No entry has been created today to edit!')

        if option.lower() == 'read': 
            if page.check_entry_existence() == True:
                page.read_entry()
            else:
                print('No entry has been made to read!')

        if option.lower() == 'delete':
            page.remove_entry() 
        if option.lower() == 'exit': 
            break
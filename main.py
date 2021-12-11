# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import fileinput
import csv

'''
def create_dictionary(filename):
    my_data = pandas.DataFrame.from_csv(filename, sep='\t', index_col=False)
    # Here you can delete the dataframe columns you don't want!
    #del my_data['B']
    #del my_data['D']
    # ...
    # Now you transform the DataFrame to a list of dictionaries
    list_of_dicts = [item for item in my_data.T.to_dict().values()]
    return list_of_dicts

def parse_menu():
    # Parse a tab deliminated file to get the menu name and the price
    '''

def print_names(names):
    for i in range(len(names)-1):
        print('[%d] %s' % ((i+1), names[i]))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('I am here to help you split your bills')
    menu_len = len(list(csv.reader(open('menu.txt', 'r'), delimiter='\t')))
    name_len = len(list(csv.reader(open('names.txt', 'r'), delimiter='\t')))
    f1 = open('menu.txt', 'r')
    f2 = open('names.txt', 'r')
    menu2 = [0] * menu_len
    name = [0] * name_len
    i = 0
    for line in f1.readlines():
        menu = line.split()
        menu2[i] = menu
        i += 1
    f1.close()

    for line in f2.readlines():
        name[i] = line
    f2.close()

    # Assign dishes
    for j in range(len(menu2)):
        # Prompt assign message
        print('Assign (%s, $ %s) to?' % (menu2[j][0], menu2[j][1]))
        print_names(name)








# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import fileinput
import csv


def print_names(names):
    for i in range(len(names)):
        print('[%d] %s' % ((i + 1), names[i]))

def parse_cent(price_string):
    total = price_string.split('.')
    dollar = total[0]
    cents = total[1]
    total_cents = int(dollar) * 100 + int(cents)
    return total_cents

def tax(price, rate):
    rate = float(rate / 100)
    return price * rate

def tip(price, rate):
    rate = rate / 100
    return price * rate

def calculate(billings, tax, tip):
    for i in range(len(billings)):
        billings[i] = billings[i]*(1+tax+tip)
        print(billings[i])
    return billings

if __name__ == '__main__':
    print('I am here to help you split your bills')
    menu_len = len(list(csv.reader(open('menu.txt', 'r'), delimiter='\t')))
    name_len = len(list(csv.reader(open('names.txt', 'r'), delimiter='\t')))
    f1 = open('menu.txt', 'r')
    f2 = open('names.txt', 'r')
    menu2 = [0] * menu_len
    name = [0] * name_len
    billings = [0] * name_len

    i = 0
    for line in f1.readlines():
        menu = line.split()
        menu2[i] = menu
        i += 1
    f1.close()

    i = 0
    for line in f2.readlines():
        name[i] = line
        name[i] = name[i].rstrip('\n')
        i += 1
    f2.close()

    # Assign dishes
    for j in range(len(menu2) - 1):
        # Prompt assign message
        print('Assign (%s, $ %s) to?' % (menu2[j][0], menu2[j][1]))
        print_names(name)
        index = input("Enter their index: ")

        curr_tab = billings[int(index) - 1]
        price_cent = parse_cent(menu2[j][1])
        # Parse price to cents
        new_tab = curr_tab + price_cent
        billings[int(index) - 1] = new_tab

        # Print Confirmed Billing
        print('Assigned %s, $ %s to %s' % (menu2[j][0], menu2[j][1], name[int(index)-1]))

    tax_rate = int(input('What is the tax rate? '))
    tip_rate = int(input('What is the tip rate? '))

    # Sum all
    for j in range(len(billings)):
        billings[j] = billings[j] + int(tax(int(billings[j]), tax_rate)) + int(tip(int(billings[j]), tip_rate))

    # Print Billings
    for j in range(len(billings)):
        billings[j] = billings[j] / 100
        print('%s owes $%1.2f' %(name[j], billings[j]))




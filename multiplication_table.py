# Multiplication table creator  # Создатель таблицы умножения
# (Custom numbers)              # (пользовательские числа)
# [ENG] version                 # Английская версия

import pandas as pd                        # Creating DataFrame(table)
import matplotlib.pyplot as plt            # Displaying the table (graphically)
import warnings                            # Turning off warnings

from ITTC import iterating_through_table_cells as ittc  # Own module


def quicksort(array):
    """Quick sorting of the list."""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def get_count():
    """Getting and checking the number of numbers in the list."""
    count = input('Enter the number of numbers(natural number): ')
    if count.isdigit() is False or float(count) % 1 != 0 or float(count) < 1:
        print('You entered incorrect data.Try again.')
        count = get_count()
    return int(count)


def get_numbers(quantity):
    """Getting and checking each number in the list."""
    nmbrs = []
    print('\nEnter the numbers one at a time(a rational number)'
          '\n(invalid values will not be taken into account):')
    for keep in range(quantity):
        number = input()
        if number.replace('.', '').isdigit() is False:
            pass
        else:
            nmbrs.append(float(number))
    if not nmbrs:
        print("You didn't enter the correct numbers.Try again.")
        return get_numbers(quantity)
    return nmbrs


def sort_flag(numbers_list):
    """Setting a list sorting condition."""
    flag = input('Sort the entered numbers?'
                 '(0-no, 1-ascending, 2-descending): ')
    if flag == '0':
        pass
    elif flag == '1':
        numbers_list = quicksort(numbers_list)
    elif flag == '2':
        numbers_list = quicksort(numbers_list)
        numbers_list = numbers_list[::-1]
    else:
        print('\nEnter the correct response.')
        sort_flag(numbers_list)
    return numbers_list


def get_int(my_numbers):
    """Converts numbers without a decimal part in the list to the Int type."""
    for i in my_numbers:
        if i % 1 == 0:
            ind = my_numbers.index(i)
            i = int(i)
            my_numbers[ind] = i
    return my_numbers


def set_cell_fontsize(item):
    """Changes the font size in the cell to match the text size."""
    text = item.get_text()  # Text(0, 0, 'x')     x - cell value
    text = str(text)        # 'Text(0, 0, 'x')'
    text = text[12:-2]      # x     (str)
    lenght = len(text)
    item.set_fontsize(20-lenght)


print('\n---Creating a multiplication table---\n')

# Performing functions sequentially.

count_numbers = get_count()

numbers = get_numbers(count_numbers)

numbers = sort_flag(numbers)

numbers = get_int(numbers)

# Creating (generating) two dictionaries and combining them into one in
# order to get a dictionary in which the first key & value pair will create
# the first column of the table with multipliable numbers (value = numbers).

# Creating a dictionary that defines the DataFrame of multiplied numbers.
mydict = {str(num):
          [str(int(i*num)) if (i*num) % 1 == 0 else i*num for i in numbers]
          for num in numbers}

# Creating a dictionary that defines a column (Series) of multipliable numbers.
pydict = {'x': [str(int(q)) if q % 1 == 0 else q for q in numbers]}

# Combining them into a single dictionary that defines the entire
# DataFrame of the table.
for k, v in mydict.items():
    pydict[k] = v

# Creating DataFrame.
data = pd.DataFrame(pydict,
                    index=[str(i) if i % 1 == 0 else i for i in numbers])

warnings.filterwarnings('ignore')  # Turning off warnings

# Creating an instance of the figure class and configuring its parameters.
param = len(numbers)
fig = plt.figure(figsize=(param+1, param+1), dpi=int(80 - param*2))

ax = fig.add_subplot()
fig.set(facecolor='yellow')

# Creating the table itself and configuring its parameters.
the_table = plt.table(cellText=data.values,    # Contents of table cells
                      colLabels=data.columns,  # Names of table columns
                      loc='center',            # The alignment of the table
                                               # in the window
                      cellLoc='center')        # Align text inside cells

the_table.scale(1, 5)                          # Table size

# Changing the colors of some (extreme) table cell.
cell = the_table[0, 0]
cell.set_color('blue')
for i in range(1, len(numbers)+1):
    obj = the_table[0, i]
    obj.set_color('green')
    objct = the_table[i, 0]
    objct.set_color('green')

# Setting a name for the matplotlib window.
man = plt.get_current_fig_manager()
man.canvas.set_window_title('Multiplication table')
# Hide the axes.
plt.axis('off')

# Change the fonts in each cell according to the length of the text in it.
the_table = ittc(the_table, set_cell_fontsize)

# The display of the table.
plt.show()

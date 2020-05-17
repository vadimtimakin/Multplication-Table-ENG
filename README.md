# Multplication-Table-ENG

Multiplication table creator (custom numbers).

Thanks to this program, you can build your multiplication table from any rational numbers. First you will need to specify the number of numbers, then enter the numbers one by one, and in the last step you will be able to sort your numbers (ascending, descending, not sorting). After that, the table will be displayed on the screen. There is an example below.

![alt text](https://cdn1.savepice.ru/uploads/2020/5/17/ea57612e5208f3ca97a798e4746bbf4d-full.jpg)

The program code is implemented in Python 3. Also, before launching, make sure that you have the pandas and matplotlib libraries installed.

In this repository, a file is allocated to a separate module ITTC.py, containing the iterating_through_table_cells function. This function allows you to iterate over all the cells in the table and perform any actions on them. It takes your table instance as input, as well as a function that will define actions on cells. This can be useful when you need to perform operations that are not exactly the same on each cell. For example, to set the font size depending on the length of the line in the cell itself; this is the purpose for which I used this function.

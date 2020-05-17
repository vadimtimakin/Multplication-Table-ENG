def iterating_through_table_cells(the_table, foo):  # ITTC
    """
    Iterates through all the cells of an object of the table class in matplotlib
    and performs actions on them contained in the foo argument function.
    """
    cells = the_table.get_celld()
    for cell in cells.keys():
        item = the_table.__getitem__(cell)
        foo(item)
    return the_table

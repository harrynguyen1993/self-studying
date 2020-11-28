import cProfile


def reverse_dic(my_dict):
    # Use to invert dictionaries that have unique values
    my_inverted_dict = dict(map(reversed, my_dict.items()))

    # Use to invert dictionaries that have unique values
    my_inverted_dict = {value: key for key, value in my_dict.items()}

    # Use to invert dictionaries that have non-unique values
    from collections import defaultdict
    my_inverted_dict = defaultdict(list)
    {my_inverted_dict[v].append(k) for k, v in my_dict.items()}

    # Use to invert dictionaries that have non-unique values
    my_inverted_dict = dict()
    for key, value in my_dict.items():
        my_inverted_dict.setdefault(value, list()).append(key)

    # Use to invert dictionaries that have lists of values
    my_dict = {value: key for key in my_inverted_dict for value in my_map[key]}


def plush_element_2_list():
    ethernet_devices = [1, [7], [2], [8374163], [84302738]]
    usb_devices = [1, [7], [1], [2314567], [0]]

    # The long way
    all_devices = [
        ethernet_devices[0] + usb_devices[0],
        ethernet_devices[1] + usb_devices[1],
        ethernet_devices[2] + usb_devices[2],
        ethernet_devices[3] + usb_devices[3],
        ethernet_devices[4] + usb_devices[4]
    ]

    # Some comprehension magic
    all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]

    # Let's use maps
    import operator
    all_devices = list(map(operator.add, ethernet_devices, usb_devices))

    # We can't forget our favorite computation library
    import numpy as np
    all_devices = np.add(ethernet_devices, usb_devices)


def check_file_is_existed():
    # Brute force with a try-except block (Python 3+)
    try:
        with open('/path/to/file', 'r') as fh:
            pass
    except FileNotFoundError:
        pass

    # Leverage the OS package (possible race condition)
    import os
    exists = os.path.isfile('/path/to/file')

    # Wrap the path in an object for enhanced functionality
    from pathlib import Path
    config = Path('/path/to/file')
    if config.is_file():
        pass


def convers_2_list_to_dic():
    column_names = ['id', 'color', 'style']
    column_values = [1, 'red', 'bold']

    # Convert two lists into a dictionary with zip and the dict constructor
    name_to_value_dict = dict(zip(column_names, column_values))

    # Convert two lists into a dictionary with a dictionary comprehension
    name_to_value_dict = {key: value for key, value in zip(column_names, column_values)}

    # Convert two lists into a dictionary with a loop
    name_value_tuples = zip(column_names, column_values)
    name_to_value_dict = {}
    for key, value in name_value_tuples:
        if key in name_to_value_dict:
            pass  # Insert logic for handling duplicate keys
        else:
            name_to_value_dict[key] = value


def check_list_is_empty():
    my_list = list()

    # Check if a list is empty by its length
    if len(my_list) == 0:
        pass  # the list is empty

    # Check if a list is empty by direct comparison (only works for lists)
    if my_list == []:
        pass  # the list is empty

    # Check if a list is empty by its type flexibility **preferred method**
    if not my_list:
        pass  # the list is empty


def clone_list():
    my_list = [27, 13, -11, 60, 39, 15]

    # Clone a list by brute force
    my_duplicate_list = [item for item in my_list]

    # Clone a list with a slice
    my_duplicate_list = my_list[:]

    # Clone a list with the list constructor
    my_duplicate_list = list(my_list)

    # Clone a list with the copy function (Python 3.3+)
    my_duplicate_list = my_list.copy()  # preferred method

    # Clone a list with the copy package
    import copy
    my_duplicate_list = copy.copy(my_list)
    my_deep_duplicate_list = copy.deepcopy(my_list)

    # Clone a list with multiplication?
    my_duplicate_list = my_list * 1  # do not do this


def check_performance_code():
    # Brute force solution
    import datetime
    start_time = datetime.datetime.now()
    [(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]
    # example snippet
    end_time = datetime.datetime.now()
    print(end_time - start_time)

    # timeit solution
    import timeit
    min(timeit.repeat("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]"))

    # cProfile solutionimport cProfile
    cProfile.run("[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]")


if __name__ == '__main__':
    print("Hello ")

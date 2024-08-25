
import numpy as np
from statsmodels.sandbox.regression.ols_anova_original import products

an_integer = 1

a_string = 'qwe'

a_list_of_integer = [1, 2, 3, 4]
a_list_of_things = ['a', 2, 'asd', a_string, an_integer]

a_list_of_lists = [a_list_of_integer, a_list_of_things]

print(a_list_of_lists[0])


a_dictionary = {'key_1': 'value_1',
                'key_2': 'value_2',
                'key_3': 'value_3'}

an_exemple_with_fruits = {'banana': 3,
                          'apples': 2,
                          'oranges': 123}

print(an_exemple_with_fruits['banana'])

print(' print the list items')
for i in a_list_of_integer:
    print(i)


print(' print the dictionary key-value pairs')
for i, j in a_dictionary.items():
    print(i, j)


factors = [1, 2, 3, 4.4]

def multiplicator(factors):
    """ Multiply

    Input
    -----
    factors : list of float numbers

    Output
    ------
    product : float number

    """
    product = 1
    for i in factors:
        # product = product * i
        product *= i

    return product



class Operation:
    def __init__(self, description, a_number, a_list):
        """ Initialization

        Input
        -----
        description : string

        a_number : a number of elements in the final elements method

        a_list: a list of anything

        """
        self.description = description
        self.a_number = a_number
        self.a_list = a_list

    def describer(self):
        """ Give info about the class """
        print(self.description)
        print(self.a_list)
        print(self.a_number)


my_operation_class_1 = Operation('First class', 16, [])

my_operation_class_2 = Operation('Second class', 2, [2])

my_operation_class_3 = Operation('Third class', 512, [1, 2])

# print(my_operation_class_1.a_list)
# print(my_operation_class_1.a_number)
# print(my_operation_class_1.description)

my_operation_class_1.describer()

a_string = 'BIg and SMALL'

print(a_string.lower())


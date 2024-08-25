"""Construct a CLASS that is able to make the 4 operations with 4 different functions:

your_class.add([])
your_class.subtract([])
your_class.multiply([])
your_class.divide([])

your_class.give_random() ---> the result of one of the previous function
"""

import numpy as np

class Easy_version:
    def __init__(self, list_of_numbers):
        """ Initialize the class

        Input
        -----
        list_of_number : list of float numbers
        operate : string, the operation to execute
        """

        self.list_of_numbers = list_of_numbers

    def summer(self):
        """ Summing

        Input
        -----
        factors : list of float numbers

        Output
        ------
        product : float number

        """
        summed = 1
        for i in self.list_of_numbers:
            # product = product * i
            summed *= i

        return summed

    def subtractor(self):
        """ Sub

        Input
        -----
        factors : list of float numbers

        Output
        ------
        result : float number

        """
        result = 1
        for i in self.list_of_numbers:
            # product = product * i
            result *= i

        return result

    def multiplicator(self):
        """ Multiply

        Input
        -----
        factors : list of float numbers

        Output
        ------
        product : float number

        """
        product = 1
        for i in self.list_of_numbers:
            # product = product * i
            product *= i

        return product

    def divider(self):
        """ DIvide

        Input
        -----
        factors : list of float numbers

        Output
        ------
        result : float number

        """
        result = 1
        for i in self.list_of_numbers:
            # product = product * i
            if i != 0:
                result /= i
            else:
                return None

        return result

    def give_random(self):
        mapping = {'sum': self.summer(),
                   'subtract': self.subtractor(),
                   'divide': self.divider(),
                   'multiply': self.multiplicator(),
                   }
        operate = np.random.choice(['sum', 'subtract', 'divide', 'multiply'])
        print(mapping[operate])


class My_fancy_version:
    def __init__(self, list_of_numbers, operate):
        """ Initialize the class

        Input
        -----
        list_of_number : list of float numbers
        operate : string, the operation to execute
        """

        self.list_of_numbers = list_of_numbers
        self.operate = operate

    def operation(self):
        """ Make an operation  """
        res = self.list_of_numbers[0]
        for i in self.list_of_numbers[1:]:
            if 'sum' in self.operate:
                res += i
            if 'sub' in self.operate:
                res -= i
            if 'mul' in self.operate:
                res *= i
            if 'div' in self.operate:
                if i != 0:
                    res /= i
                else:
                    None

        print(res)


lets_go_easy = Easy_version(list_of_numbers = [5, 4, 3, 2])

lets_go_easy.give_random()


lets_go_fancy = My_fancy_version(list_of_numbers = [5, 4, 3, 2],
                                 operate = np.random.choice(['sum', 'sub', 'div', 'mol']))

lets_go_fancy.operation()


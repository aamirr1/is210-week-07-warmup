#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Warm up task 1"""


def fibonacci(maxint):
    """This function called Fibonacci will print a max number.

    Args:
        maxint(int): This is will be used as a max (largest integer).
        
    Returns:
        numlist: Returns integer numbers.
        
    Examples:
        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
        """
    numlist = []
    num1, num2 = 0, 1
    count = maxint
    while num2 < count:
        numlist.append(num1)
        num1, num2 = num2, num1 + num2
        count += 1
        
    return numlist

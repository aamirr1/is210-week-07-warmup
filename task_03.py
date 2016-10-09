#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Worm-up task 3"""

import decimal


def lexicographics(to_analyze):
    """This function will calculate min, max and average numbers.

    Args:
        to_analyze(str): Arg will be used for calculation.
        
    Returns:
        A tuple with max, min and average of a list of words.
        
    Example:
        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    
    fulllist = to_analyze.split('\n')
    word = []
    for item in fulllist:
        exp = len(item.split())
        word.append(exp)
        
    return (max(word), min(word), sum(word)/decimal.Decimal(len(word)))

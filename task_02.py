#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Warm-up task 2"""


def bool_to_str(bval):
    """Find out if returned numbers are true or false.

    Args:
        bool_to_str(bool): Evaluates for truthiness or falsiness.
        
    Returns:
        Returns yes or no based on boolean values.
       
    Examples:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'
        >>> import task_02
        >>> task_02.bool_to_str('')
        'No'
    """
    
    mybool = ''
    if bval:
        mystring = 'Yes'
    else:
        mystring = 'No'
        
    return mystring

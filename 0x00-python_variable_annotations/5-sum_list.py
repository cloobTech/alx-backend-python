#!/usr/bin/env python3
''' module -- Task 5 '''
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' takes a list input_list of floats as argument and
    returns their sum as a float.'''
    return list(sum(input_list))

# -*- coding: utf-8 -*-

from ordering import merge_function

def test_merge():
    original_list = ['one', 'two', 'three']
    add_list = ['one', 'two', 'five', 'six']
    delete_list = ['two', 'five']
    result_list = ['three', 'six', 'one']
    assert merge_function(original_list, add_list, delete_list) == result_list

def test_upper_lower():
    assert merge_function(['one', 'Two'], [], []) == ['Two','one']

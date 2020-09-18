# -*- coding: utf-8 -*-

def merge_function(original_list, add_list, delete_list):
    unordered = set(original_list).union(add_list).difference(delete_list)
    reverse_alphabetical = sorted(unordered, key=str.lower, reverse=True)
    result_list = sorted(reverse_alphabetical, key=len, reverse=True)
    return result_list
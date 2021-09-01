from merge_sort import merge_sort
import numpy as np
import pytest


def test_always_true():
    assert True

def test_merge_sort_with_positives():
    array_pos = np.array(merge_sort([4784, 52, 3467, 45, 346, 2352,  1343]))
    array_pos_result = np.array([45, 52, 1343, 2352, 3467, 4784])
    assert all(a == b for a, b in zip(array_pos, array_pos_result))

def test_merge_sort_with_negatives():
    array_neg = np.array(merge_sort([15, 2, 4, 65, -75, 23, -2]))
    array_neg_result = np.array([-75, -2, 2, 4, 15, 23, 65])
    assert all(a == b for a, b in zip(array_neg, array_neg_result))

def test_merge_sort_with_dupes():
    array_dupes = np.array(merge_sort([6, 2, 3, 4, 2, 6]))
    array_dupes_result = np.array([2, 2, 3, 4, 6, 6])
    assert all(a == b for a, b in zip(array_dupes, array_dupes_result))

def test_merge_sort_one_element():
    array_one_elem = np.array(merge_sort([2]))
    array_one_elem_result = np.array([2])
    assert all(a == b for a, b in zip(array_one_elem, array_one_elem_result))

def test_empty_list():
    assert merge_sort([]) == []
import pytest
from hypothesis import given
import hypothesis.strategies as st
from sort_algo import bubble_sort, insert_sort


@given(st.lists(st.integers()))
def test_bubble_sort(xs):
    lists_ = list(xs)
    print(lists_)
    if len(xs) >= 2:
        sorted_list = bubble_sort(lists_)
        lists_.sort()
        assert sorted_list[0] == lists_[0]
        assert sorted_list[-1] == lists_[-1]


@given(st.lists(st.integers()))
def test_insert_sort(xs):
    print(xs)
    if len(xs) >= 2:
        sorted_list = insert_sort(xs)
        xs.sort()
        assert sorted_list[0] == xs[0]
        assert sorted_list[-1] == xs[-1]


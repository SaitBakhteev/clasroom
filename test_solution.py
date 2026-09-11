# test_solution.py
import pytest
from solution import func  # Импортируем функцию из файла студента

def test_func_positive():
    """Проверка на положительных числах."""
    assert func(2, 3) == 5
    assert func(1, 2) == 3

def test_func_negative():
    """Проверка на отрицательных числах."""
    assert func(-1, -1) == -2
    assert func(-5, 3) == -2

def test_func_zero():
    """Проверка с нулем."""
    assert func(0, 5) == 5
    assert func(0, 0) == 0

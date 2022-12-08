import pytest
from main import *


def test_costs():
    assert lista_costo() == [150, 1200, 300, 500, 829, 2750]

def test_total():
    assert total(lista_costo()) == 6361.0

def test_main():
    assert main() is None
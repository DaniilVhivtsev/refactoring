import sys
import pytest

from PIL import Image
from PIL import ImageChops


def test_4_1():
    """
    4 этап Работает ли модуль как консольное приложение
    в консоли модуль должен запускаться с помощью команды
        python filter.py in.jpg out.jpg 10 50
    где python - наш интерпретатор Python
        filter.py - файл модуля
        in.jpg - строка, имя входного файла
        out.jpg - строка, имя выходного файла
        10 - число, размер блока в пикселях
        50 - шаг изменения яркости пикселя
    """
    pass

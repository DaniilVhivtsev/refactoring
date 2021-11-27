from PIL import Image
from PIL import ImageChops


def test_1_1():
    """1 этап Верно без функций и параметров"""

    # импортируя модуль, мы как будто запускаем его выполнение
    import filter

    # в результате выполнения модуля должен сохраниться файл res.jpg
    result = Image.open("res.jpg")  # прочитаем его
    correct = Image.open("tests/out/1out.jpg")  # прочитаем файл верного результата
                                                # для тестирования на Windows - поменять путь на tests/outWin

    diff = ImageChops.difference(correct, result)  # сравним эти два файла
    assert not diff.getbbox()  # получим результат сравнения True или False

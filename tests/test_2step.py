from PIL import Image
from PIL import ImageChops

# импортируем метод из модуля для выполнения тестов
from filter import convert_image_to_mosaic


def test_2_1():
    """
    2 этап Функции + Параметры Аргументы по умолчанию
    gradations_count = 5 - количество градаций серого
    gradation_step = 255 // gradations_count = 51 , но по умолчанию 50 - шаг изменения яркости пикселя
    def convert_image(img_in="img2.jpg",
                      img_out="res.jpg",
                      block_size=10,
                      gradation_step=50):
        pass TODO реализовать функцию(-ии) в файле filter.py
    """
    # вызываем метод
    convert_image_to_mosaic()

    # после выполнения с аргументами по умолчанию метод должен возвращать изображение res.jpg
    result = Image.open("res.jpg")
    correct = Image.open("tests/out/1out.jpg")  # сравниваем с верным изображением по умолчанию
                                                # для тестирования на Windows - поменять путь на tests/outWin

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()


def test_2_2():
    """2 этап Тест 2"""
    convert_image_to_mosaic(img_in="img2.jpg",          # имя входного файла не меняется
                                   img_out="res2.jpg",  # имя результирующий файл второго теста
                                   block_size=15,       # сторона "пикселя" усредненного цвета
                                   gradation_step=63)   # шаг изменения яркости пикселей
                                                        # 255 // 63 = 4 градации серого

    result = Image.open("res2.jpg")
    correct = Image.open("tests/out/2out.jpg")

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()


def test_2_3():
    """2 этап Тест 3"""
    convert_image_to_mosaic(img_in="img2.jpg",
                                   img_out="res3.jpg",
                                   block_size=1,
                                   gradation_step=1)

    result = Image.open("res3.jpg")
    correct = Image.open("tests/out/3out.jpg")  # для тестирования на Windows - поменять путь на tests/outWin

    diff = ImageChops.difference(correct, result)
    assert not diff.getbbox()

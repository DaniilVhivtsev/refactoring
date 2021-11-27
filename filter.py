from PIL import Image
import numpy as np


def convert_image_to_mosaic(img_in="img2.jpg", img_out="res.jpg", block_size=10, gradation_step=50):
    img = Image.open(img_in)
    image_array = np.array(img)
    return Image.fromarray(convert_gray(block_size, gradation_step, image_array)).save(img_out)


def convert_gray(block_size, gradation_step, image_array):
    for x in range(0, len(image_array), block_size):
        for y in range(0, len(image_array[1]), block_size):
            ans = np.sum(image_array[x: x + block_size, y: y + block_size]) \
                  // (block_size ** 2 * 3)
            ans -= ans % gradation_step
            image_array[x: x + block_size, y: y + block_size] = np.full(3, ans)
            
    return image_array


convert_image_to_mosaic()

# # print("Введите метосположение исходного файла в полном формате: ")
# # source_file = input()
# print("Введите метосположение результативного файла в полном формате: ")
# result_file = input()
# image_array = array(Image.open(source_file))
# width = len(image_array)
# height = len(image_array[1])
# print("Введите размер ячейки: ")
# mosaic_size = int(input())
# print("Введите шаг градации серого: ")
# scale_step = int(input())
# convert_image_to_mosaic()

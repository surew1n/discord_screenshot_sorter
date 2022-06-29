from asyncore import read
from PIL import Image
from statistics import mode
import os
import imghdr
import shutil

input_folder_path = input('Enter the path of the folder you want to sort: ')

output_folder_name = 'Discord Screenshots'
output_folder_path = os.path.join(input_folder_path, output_folder_name)

output_folder_exists = False

screenshot_counter = 0

for filename in os.scandir(input_folder_path):
    if(filename.name == 'Discord Screenshots'):
        output_folder_exists = True

if (output_folder_exists == False):
    os.mkdir(output_folder_path)

for filename in os.scandir(input_folder_path):
    if(os.path.isfile(filename)):
        if (imghdr.what(filename) == 'png' or imghdr.what(filename) == 'jpeg'):
            img = Image.open(filename.path)
            img = img.convert('RGB')

            width, height = img.size

            pixels_list = []

            for x in range(0, width):
                for y in range(0, height):
                    #get r,g,b value of pixel
                    pixels_list.append(img.getpixel((x, y)))

            most_common = mode(pixels_list)

            if(most_common == (54, 57, 63)):
                screenshot_counter += 1
                print('Screenshots moved: ' + str(screenshot_counter))
                shutil.move(filename.path, output_folder_path)

input('Done, press any key to close . . .')
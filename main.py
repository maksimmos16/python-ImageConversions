# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from PIL import Image

DIRECTORY = 'Test'
FROM_EXTENSION = '.jpg'
TO_EXTENSION = '.png'
MAX_SIZE = (1024, 1024)


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            conversion(os.path.join(root, name))


def conversion(file):
    resize(file)
    name, extension = os.path.splitext(file)
    if extension == FROM_EXTENSION:
        im = Image.open(file)
        im.save(name + TO_EXTENSION)
        os.remove(file)


def resize(file):
    im = Image.open(file)
    im.thumbnail(MAX_SIZE, Image.ANTIALIAS)
    im.save(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    walk(DIRECTORY)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

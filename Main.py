import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
from skimage.exposure import histogram
from skimage import data, img_as_float
from skimage import exposure
from matplotlib import pyplot as plt
from skimage.io import imshow, imsave, imread


# save_current_parameters_to_file('D:\\Рабочий стол\\Project_settings.json')
settings = {
    'filepath': 'D:\\Рабочий стол\\forest.jpg',
    'left_contrast_border_value': 0,
    'right_contrast_border_value': 100
}


def read_parameters(filepath):
    json_data = json.load(open(filepath))
    for entry in json_data.keys():
        print(f'Red parameter " {entry}" with value = "{json_data[entry]}" ')
    return json_data


def save_current_parameters_to_file(filepath):
    json.dump(settings, open(filepath, 'w'))


json_settings_file = json.load(open('D:\\Рабочий стол\\Project_settings.json'))
image_filepath = json_settings_file['filepath']
contrast_left_border = json_settings_file['left_contrast_border_value']
contrast_right_border = json_settings_file['right_contrast_border_value']

#print(image_filepath)
#print(contrast_left_border)
#print(contrast_right_border)
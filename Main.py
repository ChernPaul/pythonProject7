import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
from skimage.exposure import histogram
from skimage import data, img_as_float
from skimage import exposure
from matplotlib import pyplot as plt
from skimage.io import imshow, imsave, imread, show

# save_current_parameters_to_file('D:\\Рабочий стол\\Project_settings.json')
settings = {
    'filepath': 'D:\\Рабочий стол\\forest.jpg',
    # MIN_VALUE = 0
    'left_contrast_border_value': 0,
    # MAX_VALUE = 100
    'right_contrast_border_value': 10

}


def create_histogram_plot(img_array):
    hist_red, bins_red = histogram(img_array[:, :, 2])
    hist_green, bins_green = histogram(img_array[:, :, 1])
    hist_blue, bins_blue = histogram(img_array[:, :, 0])

    plt.ylabel('Number of counts')
    plt.xlabel('Brightness')
    plt.title('Histogram of the brightness distribution for each channel')
    plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
    plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
    plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)
    plt.legend(['green', 'red', 'blue'])


def create_figure_of_union_plot(image1, image2, image3, image4):
    fig = plt.figure(figsize=(20, 10))
    fig.add_subplot(2, 4, 1)
    imshow(image1)
    fig.add_subplot(2, 4, 2)
    imshow(image2)
    fig.add_subplot(2, 4, 3)
    imshow(image3)
    fig.add_subplot(2, 4, 4)
    imshow(image4)
    fig.add_subplot(2, 4, 5)
    create_histogram_plot(image1)
    fig.add_subplot(2, 4, 6)
    create_histogram_plot(image2)
    fig.add_subplot(2, 4, 7)
    create_histogram_plot(image3)
    fig.add_subplot(2, 4, 8)
    create_histogram_plot(image4)
    return fig


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

image = imread(image_filepath)
left_border, right_border = np.percentile(image, (contrast_left_border, contrast_right_border))
image_rescale = exposure.rescale_intensity(image, in_range=(left_border, right_border))

image_equalized = exposure.equalize_hist(image)

# Adaptive Equalization
image_adapted_equalized = exposure.equalize_adapthist(image, clip_limit=0.03)

create_figure_of_union_plot(image, image_rescale, image_equalized, image_adapted_equalized)
show()

# print(image_filepath)
# print(contrast_left_border)
# print(contrast_right_border)

#!/usr/bin/python3

import os
import numpy as np
import requests
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt
import pandas

URL = 'https://www.researchgate.net/profile/Tao_Chen15/publication/3935609/figure/fig1/AS:394647298953219@1471102656485/8-bit-256-x-256-Grayscale-Lena-Image.png'

image_data = requests.get(URL).content

image_file_name = 'sample_image.jpg'

with open(image_file_name, 'wb') as image_file:
    image_file.write(image_data)

# read the file from local directory
image = skimage.io.imread(fname=os.path.join(os.getcwd(), image_file_name), as_gray=False)

# create the histogram
pixels_population, tonal = np.histogram(image, bins=256)

# Save the tonal values into a CSV
data_frame = pandas.DataFrame({'tonal': tonal[:-1], 'pixel_population': pixels_population})
data_frame.set_index('tonal', inplace=True)
data_frame.to_csv(os.path.join(os.getcwd(), 'histogram.csv'))

# Sort the values of the tonal highest to low
tonal[::-1].sort()






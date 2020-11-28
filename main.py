#!/usr/bin/python3

import os
import numpy as np
import requests
import skimage.io
import skimage.viewer

URL = 'https://www.researchgate.net/profile/Tao_Chen15/publication/3935609/figure/fig1/AS:394647298953219@1471102656485/8-bit-256-x-256-Grayscale-Lena-Image.png'

image_data = requests.get(URL).content

image_file_name = 'sample_image.jpg'

with open(image_file_name, 'wb') as image_file:
    image_file.write(image_data)

# read the file from local directory
image = skimage.io.imread(fname=os.path.join(os.getcwd(), image_file_name), as_gray=True)

# create the histogram
pixels_population, tonal = np.histogram(image, bins=256, range=(0, 1))

# Save the tonal values into a CSV
np.savetxt("histogram.csv", tonal, fmt='%10.5f', delimiter=",")

# Sort the values of the tonal highest to low
tonal[::-1].sort()



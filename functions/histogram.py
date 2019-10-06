import numpy as np
import matplotlib.pyplot as plt

def histogram_array_generator(image):
    histogram_array = {}
    for index in range(256):
        histogram_array[index] = 0
    for row in image:
        for element in row:
            histogram_array[element] += 1
    return histogram_array

def plot_histogram(array, channel):
    plt.figure(figsize=(18,8))
    plt.bar(array.keys(), array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title(channel)
    plt.show()

def histogram_generator(red_array, green_array, blue_array):
    plot_histogram(red_array, 'Red channel histogram')
    plot_histogram(green_array, 'Green channel histogram')
    plot_histogram(blue_array, 'Blue channel histogram')

def probability_distribution_generator(array, image_dimension):
    prob_dist_array = {}
    for index in range(256):
        prob_dist_array[index] = array[index]/image_dimension
    return prob_dist_array

def probability_distribution_histogram_generator(red_array, green_array, blue_array):
    plot_histogram(red_array, 'Red probability distribution histogram')
    plot_histogram(green_array, 'Green probability distribution histogram')
    plot_histogram(blue_array, 'Blue probability distribution histogram')
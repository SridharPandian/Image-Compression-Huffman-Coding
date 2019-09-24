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

def histogram_generator(red_array, green_array, blue_array):
    # plt.subplot(3,1,1)
    plt.figure(figsize=(18,8))
    plt.bar(red_array.keys(), red_array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title('Red channel histogram')
    plt.show()

    # plt.subplot(3,1,2)
    plt.figure(figsize=(18,8))
    plt.bar(green_array.keys(), green_array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title('Green channel histogram')
    plt.show()

    # plt.subplot(3,1,3)
    plt.figure(figsize=(18,8))
    plt.bar(blue_array.keys(), blue_array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title('Blue channel histogram')
    plt.show()

def probability_distribution_generator(array, image_dimension):
    prob_dist_array = {}
    for index in range(256):
        prob_dist_array[index] = array[index]/image_dimension
    return prob_dist_array

def probability_distribution_histogram_generator(red_array, green_array, blue_array):
    # plt.subplot(3,1,1)
    plt.figure(figsize=(18,8))
    plt.bar(red_array.keys(), red_array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title('Red probability distribution histogram')
    plt.show()

    # plt.subplot(3,1,2)
    plt.figure(figsize=(18,8))
    plt.bar(green_array.keys(), green_array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title('Green probability distribution histogram')
    plt.show()

    # plt.subplot(3,1,3)
    plt.figure(figsize=(18,8))
    plt.bar(blue_array.keys(), blue_array.values())
    plt.ylabel('Number of occurances')
    plt.xlabel('Pixel values')
    plt.title('Blue probability distribution histogram')
    plt.show()
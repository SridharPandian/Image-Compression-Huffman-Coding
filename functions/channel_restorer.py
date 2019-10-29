import numpy as np

def image_restorer(red_channel_image, green_channel_image, blue_channel_image):
    x_max, y_max = np.array(red_channel_image).shape
    
    restored_image = []
    
    for x in range(x_max):
        y_set = []
        for y in range(y_max):
            z_set = [red_channel_image[x][y], green_channel_image[x][y], blue_channel_image[x][y]]
            y_set.append(z_set)
        restored_image.append(y_set)
        
    return restored_image
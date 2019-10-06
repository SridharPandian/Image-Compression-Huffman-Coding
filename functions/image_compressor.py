# import numpy as np
def compressor(original_image, code):
    compress_image_array = []
    for pixel_row_index in range(original_image.shape[0]):
        pixel_row = []
        for pixel_column_index in range(original_image.shape[1]):
            pixel_row.append(str(code[original_image[pixel_row_index][pixel_column_index]]))
        compress_image_array.append(pixel_row)
    return compress_image_array
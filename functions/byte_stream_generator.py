def byte_stream (red_stream_image, green_stream_image, blue_stream_image, red_seperator, green_seperator):
    byte_stream = ""
    
    for stream_row_index in range(len(red_stream_image)):
        for stream_column_index in range(len(red_stream_image[0])):
            byte_stream += str(red_stream_image[stream_row_index][stream_column_index])
    
    byte_stream += red_seperator

    for stream_row_index in range(len(green_stream_image)):
        for stream_column_index in range(len(green_stream_image[0])):
            byte_stream += str(green_stream_image[stream_row_index][stream_column_index])
    
    byte_stream += green_seperator

    for stream_row_index in range(len(blue_stream_image)):
        for stream_column_index in range(len(blue_stream_image[0])):
            byte_stream += str(blue_stream_image[stream_row_index][stream_column_index])

    return byte_stream
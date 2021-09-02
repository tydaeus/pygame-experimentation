import image_loader



def get_test_surface():
    return image_loader.convert_color_array_to_surface(image_loader.convert_text_image_to_colorarray(image_loader.test_txt_image))
    # return convert_color_array_to_surface(test_image_src)
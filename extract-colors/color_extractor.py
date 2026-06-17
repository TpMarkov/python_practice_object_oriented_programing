import colorgram


def extract_colors(image_name):
    """
    Extract the 100 most prominent colors from an image.

    Args:
        image_name (str): Path to the image file.

    Returns:
        list[tuple]: A list of RGB tuples in the form (r, g, b).

    Example:
        colors = extract_colors("image.jpg")
        print(colors[0])
    """
    new_colors_list = []

    colors = colorgram.extract(image_name, 100)
    for color in colors:
        new_colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return new_colors_list

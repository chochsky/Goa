def get_size(width, height, depth):
    volume = width * height * depth
    surface_area = 2 * (width * height + height * depth + width * depth)
    return [surface_area, volume]

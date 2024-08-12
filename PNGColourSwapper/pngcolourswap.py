from PIL import Image


def colour_in_buffer_range(colour, target_colour, buffer):
    if len(colour) != len(target_colour):
        return False
    for i in range(len(colour)):
        if abs(colour[i] - target_colour[i]) > buffer:
            return False
    return True


def colour_swap(img_path, colour1, colour2, tolerance):
    img = Image.open(img_path)
    data = img.getdata()

    new_data = []
    for item in data:
        if colour_in_buffer_range(item[:3], colour1[:3], tolerance):    # Swap colour 1 with colour 2
            new_data.append(colour2 + item[3:])  # Preserve the alpha channel if it exists
        elif colour_in_buffer_range(item[:3], colour2[:3], tolerance):  # Swap colour 2 with colour 1
            new_data.append(colour1 + item[3:])
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save('output.png')

input_img = 'Career_Tree_v1.png'
colour1 = (0, 0, 0)
colour2 = (255, 255, 255)
tolerance = 100
colour_swap(input_img, colour1, colour2, tolerance)

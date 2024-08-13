from PIL import Image



def swap_colour_with_blur(current_colour, from_colour, to_colour, buffer):
    return tuple(to_colour[i] + buffer - (from_colour[i] - current_colour[i]) for i in range(3))


def colour_in_buffer_range(colour, target_colour, buffer):
    if len(colour) != len(target_colour):
        return False
    for i in range(len(colour)):
        if abs(target_colour[i] - colour[i]) > buffer:
            return False
    return True


def colour_swap(img_path, colour1, colour2, tolerance, blur_swap_tolerance):
    print('='*64)
    print(' '*25, 'Generating PNG')
    print('='*64)

    blur_swap_tolerance = blur_swap_tolerance + tolerance

    img = Image.open(img_path)
    data = img.getdata()

    new_data = []
    for pixel in data:
        # Check for direct swaps
        if colour_in_buffer_range(pixel[:3], colour1[:3], tolerance):
            new_data.append(colour2 + pixel[3:])
        elif colour_in_buffer_range(pixel[:3], colour2[:3], tolerance):
            new_data.append(colour1 + pixel[3:])

        # Check for blur swaps
        elif colour_in_buffer_range(pixel[:3], colour1[:3], blur_swap_tolerance):
            new_colour = swap_colour_with_blur(pixel[:3], colour1[:3], colour2[:3], blur_swap_tolerance)
            new_data.append(new_colour + pixel[3:])
        elif colour_in_buffer_range(pixel[:3], colour2[:3], blur_swap_tolerance):
            new_colour = swap_colour_with_blur(pixel[:3], colour2[:3], colour1[:3], blur_swap_tolerance)
            new_data.append(new_colour + pixel[3:])

        # Return original pixel if
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    img.save('output.png')


def askuser():
    input_img = input('Type a pdf directory: ')
    if input_img == '':
        input_img = 'input.png'
    colour1 = input('Type the rgb values seperated by , for colour1: ')
    colour2 = input('Type the rgb values seperated by , for colour2: ')
    if colour1 == '':
        colour1 = (255, 255, 255)
    else:
        colour1 = tuple(int(value) for value in colour1.split(','))
    if colour2 == '':
        colour2 = (0, 0, 0)
    else:
        colour2 = tuple(int(value) for value in colour2.split(','))
    print(colour1)
    print(colour2)
    total_buffer = 255
    tolerance = 0
    blur_swap_tolerance = 0
    while total_buffer > 255//2:
        print('Type the buffers you would like. Make sure they add up to no greater than 127.5')
        tolerance = input('Type the tolerance buffer: ')
        if tolerance == '':
            tolerance = 255//4
        else:
            tolerance = int(tolerance)
        blur_swap_tolerance = input('Type the blur buffer: ')
        if blur_swap_tolerance == '':
            blur_swap_tolerance = 255//4
        else:
            blur_swap_tolerance = int(tolerance)
        total_buffer = tolerance + blur_swap_tolerance
    colour_swap(input_img, colour1, colour2, tolerance, blur_swap_tolerance)

askuser()

#input_img = 'Career_Tree_v1.png'
#colour1 = (255, 255, 255)
#colour2 = (0, 0, 0)
#tolerance = 255//4
#blur_swap_tolerance = 255//4
#colour_swap(input_img, colour1, colour2, tolerance, blur_swap_tolerance)

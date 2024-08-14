from PIL import Image
import os



def swap_colour_with_blur(current_colour, from_colour, to_colour, buffer):
    return tuple(to_colour[i] + buffer - (from_colour[i] - current_colour[i]) for i in range(3))


def colour_in_buffer_range(colour, target_colour, buffer):
    if len(colour) != len(target_colour):
        return False
    for i in range(len(colour)):
        if abs(target_colour[i] - colour[i]) > buffer:
            return False
    return True


def colour_swap(input_img_list, output_directory, colour1, colour2, tolerance, blur_swap_tolerance):
    output_directory = output_directory.strip().split('/')[0]   # Remove any trailing /

    print('='*64)
    print(' '*25, 'Generating PNG')
    print('='*64)

    blur_swap_tolerance = blur_swap_tolerance + tolerance

    for img_path in input_img_list:
        print(img_path + ':')

        if not os.path.exists(img_path):
            print(' '*4 + img_path, 'does not exist. Continuing to next file')
            continue
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
        img.save(output_directory + '/' + img_path)

    print('='*64)
    print(' '*28, 'Finished')
    print('='*64)


def askuser():
    # Ask for the input pdf files
    input_img_string = input('Type one or more png directories separated by commas: ')
    if input_img_string == '':
        input_img_string = 'input.png'
        print('Defaulted to:', input_img_string)
    input_img_list = [item.strip() for item in input_img_string.split(',')]

    # Ask for the output directory where it will be stored
    output_directory = input('Type an output directory: ')
    if output_directory == '':
        output_directory = 'output'
        print('Defaulted to:', output_directory)
    else:
        output_directory = output_directory.split('/')[0].strip()  # Remove any trailing /
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Ask for the first colour that will be swapped with the second colour
    colour1 = input('Type the rgb values seperated by a comma for colour1: ')
    if colour1 == '':
        colour1 = (255, 255, 255)
        print('Defaulted to:', colour1)
    else:
        colour1 = tuple(int(value.strip()) for value in colour1.split(','))

    # Ask for the second colour that will be swapped with the first colour
    colour2 = input('Type the rgb values seperated by a comma for colour2: ')
    if colour2 == '':
        colour2 = (0, 0, 0)
        print('Defaulted to:', colour2)
    else:
        colour2 = tuple(int(value.strip()) for value in colour2.split(','))

    # Ask for the buffers, anything within the tolerance buffer will be swapped, anything within the blur tolerance will be swapped with respect to the original colour
    total_buffer = 255
    tolerance = 0
    blur_swap_tolerance = 0
    while total_buffer > 255//2:
        print('Type the buffers you would like. Make sure they add up to no greater than 127.5')
        tolerance = input('Type the tolerance buffer: ')
        if tolerance == '':
            tolerance = 255//4
            print('Defaulted to:', tolerance)
        else:
            tolerance = int(tolerance.strip())
        blur_swap_tolerance = input('Type the blur buffer: ')
        if blur_swap_tolerance == '':
            blur_swap_tolerance = 255//4
            print('Defaulted to:', blur_swap_tolerance)
        else:
            blur_swap_tolerance = int(blur_swap_tolerance.strip())
        total_buffer = tolerance + blur_swap_tolerance

    colour_swap(input_img_list, output_directory, colour1, colour2, tolerance, blur_swap_tolerance)

askuser()

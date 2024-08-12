from PIL import Image




def colourswap(img_path, colour1, colour2, tolerance):
    img = Image.open(img_path)
    data = img.getdata()

    new_data = []
    for item in data:
        if abs(colour1[0] - item[0]) <= tolerance and abs(colour1[1] - item[1]) <= tolerance and abs(colour1[2] - item[2]) <= tolerance:    # Swap colour 1 with colour 2
            new_data.append(colour2 + item[3:])  # Preserve the alpha channel if it exists
        elif abs(colour2[0] - item[0]) <= tolerance and abs(colour2[1] - item[1]) <= tolerance and abs(colour2[2] - item[2]) <= tolerance:  # Swap colour 2 with colour 1
            new_data.append(colour1 + item[3:])
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save('output.png')

input_img = 'Career_Tree_v1.png'
colour1 = (0, 0, 0)
colour2 = (255, 255, 255)
tolerance = 100
colourswap(input_img, colour1, colour2, tolerance)

from PIL import Image


def colourswap(img_path, colour1, colour2):
    img = Image.open(img_path)
    data = img.getdata()

    new_data = []
    for item in data:
        if item[:3] == colour1:
            new_data.append(colour2 + item[3:])  # Preserve the alpha channel if it exists
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save('output.png')

input_img = 'input.png'
col1 = (255, 0, 0)
col2 = (0, 255, 0)
colourswap(input_img, col1, col2)

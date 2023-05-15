from data import *


# Design Recipe
# 1) read a ppm file and get its header and pixels
# 2) read_file(fname: str)->(Header, list[str])
# 3) template of function
#   - open file
#   - read first line
#   - strip and split the second line to get its width and height for header
#   - gets the third line for max color
#   - read through each line and strip it
# 4) test case:
# 5)

def read_file(fname: str) -> (Header, list[str]):
    fil = open(fname, 'r')
    fil.readline()
    rd = fil.readline().strip().split()
    header = Header(int(rd[0]), int(rd[1]), int(fil.readline()))
    pixels = []
    for line in fil:
        pixels.append(line.strip())
    return header, pixels


# Design Recipe
# 1) goes through a list of strings and makes pixels
# 2) make_pixels(lst: list[str]) ->list[Pixel]
# 3) template of function
#   - make empty list
#   - make a try statement
#   - cycle through the lst of string and split it
#   - for each 3 values in the split list make a pixel object
#   - make an except statement that excepts the error IndexError
#   - if the error happens then cycle through the list in intervals of 3 and make pixel objects
# 4) test case:
# 5)

def make_pixels(lst: list[str]) -> list[Pixel]:
    pix_obj = []
    try:
        for line in lst:
            rgb = line.split()
            for x in range(0, len(rgb), 3):
                pix = Pixel(int(rgb[x]), int(rgb[x + 1]), int(rgb[x + 2]))
                pix_obj.append(pix)
        return pix_obj
    except IndexError:
        for x in range(0, len(lst), 3):
            pix = Pixel(int(lst[x]), int(lst[x + 1]), int(lst[x + 2]))
            pix_obj.append(pix)
    return pix_obj


# Design Recipe
# 1) takes each pixel, and it subtracts each pixel value from 255
# 2) negate(lst: list[Pixel])->list[Pixel]
# 3) template of function
#   - make empty list
#   - cycle through list of pixels
#   - for each pixel subtract its red value from 255
#   - for each pixel subtract its green value from 255
#   - for each pixel subtract its blue value from 255
#   - make the new values into a pixel and append into list
# 4) test case:
# 5)

def negate(lst: list[Pixel]) -> list[Pixel]:
    newp = []
    for x in lst:
        new_r = abs(255 - x.red)
        new_g = abs(255 - x.green)
        new_b = abs(255 - x.blue)
        pix = Pixel(new_r, new_g, new_b)
        newp.append(pix)
    return newp


# Design Recipe
# 1) applies high contrast on each pixel
# 2) high_contrast(lst: list[Pixel])->list[Pixel]
# 3) template of function
#   - make empty list
#   - cycle through list of pixels
#   - check each value of the pixel if it's greater than 127 then equal that value to 255
#   - if the current value isn't greater than 127 then equal it to 0
# 4) test case:
# 5)

def high_contrast(lst: list[Pixel]) -> list[Pixel]:
    p_list = []
    for x in lst:
        if x.red > 127:
            pix_r = 255
        else:
            pix_r = 0
        if x.green > 127:
            pix_g = 255
        else:
            pix_g = 0
        if x.blue > 127:
            pix_b = 255
        else:
            pix_b = 0
        pix = Pixel(pix_r, pix_g, pix_b)
        p_list.append(pix)
    return p_list


# Design Recipe
# 1) takes the pixels RGB value and makes a new pixel out of the average of the RGB values
# 2) gray_scale(lst: list[Pixel])->list[Pixel]
# 3) template of function
#   - makes and empty list
#   - cycle through the list of pixels
#   - get the total of the RGB values
#   - get the average of the three values
#   - make a new pixel with every RGB value being the calculated average
#   - append each pixel into the empty list
# 4) test case:
# 5)

def gray_scale(lst: list[Pixel]) -> list[Pixel]:
    p_lst = []
    for x in lst:
        total = x.red + x.green + x.blue
        avg = total // 3
        pix = Pixel(avg, avg, avg)
        p_lst.append(pix)
    return p_lst


# Design Recipe
# 1) removes a color from each pixel, meaning making that value 0
# 2) remove_color(lst: list[Pixel], color: str) -> list[Pixel]
# 3) template of function
#   - make empty list
#   - cycle through list of pixel objects
#   - depending on the color change it 0 and keep every other value the same
#   - append the new pixel into the empty list
# 4) test case:
# 5)

def remove_color(lst: list[Pixel], color: str) -> list[Pixel]:
    p_lst = []
    for x in lst:
        if color == "red":
            val_r = 0
            pix = Pixel(val_r, x.green, x.blue)
            p_lst.append(pix)
        elif color == "green":
            val_g = 0
            pix = Pixel(x.red, val_g, x.blue)
            p_lst.append(pix)
        elif color == "blue":
            val_b = 0
            pix = Pixel(x.red, x.green, val_b)
            p_lst.append(pix)
    return p_lst


# Design Recipe
# 1) shrinks an image file by 4
# 2) Shrink(image: Image)->(Header, list[Pixel])
# 3) template of function
#   - store the original height and width as a variable
#   - get the new width and height of the picture by dividing them by 2
#   - make new header with new width and height
#   - make empty list
#   - get the range of the new height and width
#   - get the average of red from the other 4 pixels in its quadrant
#   - get the average of green from the other 4 pixels in its quadrant
#   - get the average of blue from the other 4 pixels in its quadrant
#   - make new pixel with the average value for each RGB value
# 4) test case:
# 5)

def Shrink(image: Image) -> (Header, list[Pixel]):
    width1, height1 = image.header.width, image.header.height
    new_width, new_height = width1 // 2, height1 // 2
    new_header = Header(new_width, new_height, image.header.max_color)
    new_p = []
    for y in range(new_height):
        for x in range(new_width):
            x1, x2 = x * 2, x * 2 + 1
            y1, y2 = y * 2, y * 2 + 1
            avg_r = (image.pixels[y1 * width1 + x1].red +
                       image.pixels[y1 * width1 + x2].red +
                       image.pixels[y2 * width1 + x1].red +
                       image.pixels[y2 * width1 + x2].red) // 4
            avg_g = (image.pixels[y1 * width1 + x1].green +
                         image.pixels[y1 * width1 + x2].green +
                         image.pixels[y2 * width1 + x1].green +
                         image.pixels[y2 * width1 + x2].green) // 4
            avg_b = (image.pixels[y1 * width1 + x1].blue +
                        image.pixels[y1 * width1 + x2].blue +
                        image.pixels[y2 * width1 + x1].blue +
                        image.pixels[y2 * width1 + x2].blue) // 4
            pix = Pixel(avg_r, avg_g, avg_b)
            new_p.append(pix)
    return new_header, new_p


# Design Recipe
# 1) writes to a new file with the using header and pixel list
# 2) new_ppm(fname: str, p_lst: list[Pixel], header: Header)
# 3) template of function
#   - try to open the new file to write if not exit
#   - for the first line write P3
#   - second line is the header
#   - third line is the max color
#   - go through the list of pixels and in each line write its value separately
# 4) test case:
# 5)

def new_ppm(fname: str, p_lst: list[Pixel], header: Header):
    try:
        filo = open(fname, 'w')
    except FileNotFoundError:
        print("cannot open")
        exit()
    filo.write('P3\n')
    filo.write(f"{header.width} {header.height}\n")
    filo.write(f"{header.max_color}\n")
    for p in p_lst:
        filo.write(f"{p.red} {p.green} {p.blue}\n")
    filo.close()
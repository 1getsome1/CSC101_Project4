from image_modifier import *


def main():
    # Make user input a ppm file
    file_name = input("Name of ppm file: ")

    # Make user input the output file name for the newly formed ppm file
    out_file = input("Name of out file: ")

    # Make user input the modification
    mod = input("Name of modification(negate, high, gray, remove, shrink): ")

    # Read file function
    header, lst_str = read_file(file_name)

    # Run list through make pixels function
    lst_p = make_pixels(lst_str)

    # Check what functions will be preformed
    if mod == "negate":
        neg = negate(lst_p)
        new_ppm(out_file, neg, header)
    if mod == "high":
        high = high_contrast(lst_p)
        new_ppm(out_file, high, header)
    if mod == "gray":
        gray = gray_scale(lst_p)
        new_ppm(out_file, gray, header)
    if mod == "remove":
        color = input("Color which to remove(red, green, blue): ")
        if color == "Color which to remove(red, green, blue): red" or "Color which to remove(red, green, blue): green" \
                or "Color which to remove(red, green, blue): blue":
            remove = remove_color(lst_p, color)
            new_ppm(out_file, remove, header)
        else:
            print("Choose correct color!")
    if mod == "shrink":
        img = Image(header, lst_p)
        header2, shrink = Shrink(img)
        new_ppm(out_file, shrink, header2)


if __name__ == '__main__':
    main()

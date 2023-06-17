"""
File: stanCodoshop.py
Name: Yu-Tao Sun
A code that could remove unwanted items, and get a clean image
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    pixel_red = pixel.red
    pixel_green = pixel.green
    pixel_blue = pixel.blue
    dist = math.sqrt((pixel_red - red) ** 2 + (pixel_green - green) ** 2 + (pixel_blue - blue) ** 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_red = 0
    total_green = 0
    total_blue = 0
    rgb = []
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
    avg_red = int(total_red / len(pixels))
    rgb.append(avg_red)
    avg_green = int(total_green / len(pixels))
    rgb.append(avg_green)
    avg_blue = int(total_blue / len(pixels))
    rgb.append(avg_blue)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    color_distances = []
    rbg_avg = get_average(pixels)
    for pixel in pixels:
        color_distance = get_pixel_dist(pixel, rbg_avg[0], rbg_avg[1], rbg_avg[2])
        color_distances.append(color_distance)
    minimum_dis = min(color_distances)
    best = 0
    for i in range(len(color_distances)):           # find the index of pixel that has the best color distance
        if color_distances[i] == minimum_dis:
            best = i
            break
    return pixels[best]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            old_pixels = []
            for image in images:
                old_pixels.append(image.get_pixel(x, y))
            new_pixel = result.get_pixel(x, y)
            new_pixel.red = get_best_pixel(old_pixels).red
            new_pixel.green = get_best_pixel(old_pixels).green
            new_pixel.blue = get_best_pixel(old_pixels).blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

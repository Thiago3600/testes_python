from PIL import Image
from utils import in_file, out_file

def simple_grayscale(image):
    w, h = image.size
    img = Image.new("RGB", (w, h))

    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            media = (r+g+b)//3
            img.putpixel((i, j),(media, media, media))

    return img

def media_pond_grayscale(image):
    w, h = image.size
    img = Image.new("RGB", (w, h))

    for i in range(w):
        for j in range(h):
            r, g, b = image.getpixel((i, j))
            media = int(0.3*r+0.59*g+0.11*b)
            img.putpixel((i, j),(media, media, media))

    return img

if __name__ == '__main__':
    img = Image.open(in_file("nature.jpg"))
    # temp = simple_grayscale(img)
    # temp.save(out_file("simple_gray_nature.jpg"))
    temp = media_pond_grayscale(img)
    temp.save(out_file("media_pond_grayscale_nature.jpg"))

  
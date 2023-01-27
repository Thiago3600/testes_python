from email.mime import image
from PIL import Image

def germany(width):

    height = 3*width//5
    BLACK = (0,0,0)
    YELLOW = (255, 204, 0)
    RED = (255, 0, 0)

    offset = height//3

    im = Image.new("RGB", (width, height), BLACK)

    for i in range(width):
        for j in range(offset):
            im.putpixel((i, j+offset), YELLOW)
            im.putpixel((i, j+offset*2), RED)

    return im


if __name__ == "__main__":
    bandeira = germany(700)
    bandeira.show()
    bandeira.save("C:\\Users\\thiag\\Documents\\python\\img.jpg")
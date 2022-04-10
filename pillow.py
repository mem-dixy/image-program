print("start")

import os

import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
PIL.Image.MAX_IMAGE_PIXELS = None


class Cast():
    @staticmethod
    def float_to_integer(number):
        return int(round(number))


class Array:
    @staticmethod
    def subdivide(array, subdivision_size):
        L = array
        S = subdivision_size
        print(array)
        print(len(range(S)))
        print(len(L))
        return [[L[a + b] for a in range(S)] for b in range(0, len(L), S)]


####


class OS:
    @staticmethod
    def working_directory():
        return os.getcwd()

    @staticmethod
    def join(path, *paths):
        return os.path.join(path, *paths)

    @staticmethod
    def remove(path):
        if os.path.isfile(path):
            os.remove(path)

    @staticmethod
    def rename(source, destination):
        if not os.path.isfile(destination):
            os.rename(source, destination)

    @staticmethod
    def filenames(path):
        file = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for name in filenames:
                file.append(os.path.join(dirpath, name))
        return file

    @staticmethod
    def _image_save(image, path):
        if os.path.isfile(path):
            os.remove(path)
        with open(path, "wb") as file:
            image.save(file, "PNG", optimize=True)

    @staticmethod
    def walk_directory(top='.'):
        path = []
        file = []
        for (dirpath, dirnames, filenames) in os.walk(top):
            for dirname in dirnames:
                path.append(os.path.join(dirpath, dirname))
            for filename in filenames:
                file.append((filename, dirpath))
        return (path, file)

    @staticmethod
    def makedirs(paths):
        for path in paths:
            os.mkdir(path)

    @staticmethod
    def chdir(path, call, *args):
        cwd = os.getcwd()
        os.chdir(path)
        ring = call(*args)
        os.chdir(cwd)
        return ring


class Style:
    def __del__(self):
        self.fill = None
        self.anchor = None
        self.spacing = None
        self.align = None
        self.stroke_width = None
        self.stroke_fill = None
        self.font = None
        self.size = None

    def __init__(self, font, size):
        self.fill = (255, 255, 255)
        self.anchor = "ma"
        self.spacing = 4
        self.align = "center"
        self.stroke_width = 0
        self.stroke_fill = (255, 255, 255)
        self.font = font
        self.size = size

    def truetype(self):
        font = self.font
        size = self.size
        index = 0
        encoding = "unic"
        layout_engine = PIL.ImageFont.LAYOUT_BASIC
        return PIL.ImageFont.truetype(font, size, index, encoding, layout_engine)

    def text(self, x, y, text, ImageDraw):
        xy = (int(x), int(y))
        text = text
        fill = self.fill,
        font = self.truetype()
        anchor = self.anchor
        spacing = self.spacing
        align = self.align
        direction = None
        features = None
        language = None
        stroke_width = self.stroke_width
        stroke_fill = self.stroke_fill
        embedded_color = "SBIX"
        ImageDraw.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color)


class Style2:
    def __del__(self):
        self.fill = None
        self.anchor = None
        self.spacing = None
        self.align = None
        self.stroke_width = None
        self.stroke_fill = None
        self.font = None
        self.size = None

    def __init__(self, font, size):
        self.fill = 255
        self.anchor = "ma"
        self.spacing = 4
        self.align = "center"
        self.stroke_width = 0
        self.stroke_fill = 255
        self.font = font
        self.size = size

    def truetype(self):
        font = self.font
        size = self.size
        index = 0
        encoding = "unic"
        layout_engine = PIL.ImageFont.LAYOUT_BASIC
        return PIL.ImageFont.truetype(font, size, index, encoding, layout_engine)

    def text(self, x, y, text, ImageDraw):
        xy = (int(x), int(y))
        text = text
        fill = self.fill,
        font = self.truetype()
        anchor = self.anchor
        spacing = self.spacing
        align = self.align
        direction = None
        features = None
        language = None
        stroke_width = self.stroke_width
        stroke_fill = self.stroke_fill
        embedded_color = False
        ImageDraw.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color)


class Image:
    def __del__(self):
        self.height = None
        self.image = None
        self.ratio = None
        self.size = None
        self.width = None

    def __init__(self, image):
        self.height = image.height
        self.image = image
        self.ratio = image.width / image.height if image.height else 0
        self.size = image.size
        self.width = image.width

    @classmethod
    def new(cls, mode, x, y):
        mode = mode
        size = (x, y)
        color = 0
        return cls(PIL.Image.new(mode, size, color))

    @classmethod
    def open(cls, path):
        fp = path
        mode = "r"
        formats = None
        return cls(PIL.Image.open(fp, mode, formats))

    def convert(self, mode):
        matrix = None
        dither = PIL.Image.NONE
        palette = 0
        colors = 256
        self.__init__(self.image.convert(mode, matrix, dither, palette, colors))

    def resize(self, width, height):
        size = (Cast.float_to_integer(width), Cast.float_to_integer(height))
        resample = PIL.Image.LANCZOS
        box = None
        reducing_gap = None
        self.__init__(self.image.resize(size, resample, box, reducing_gap))

    def resize_to_height(self, height):
        scale = height / self.height
        width = self.width * scale
        self.resize(width, height)

    def resize_to_width(self, width):
        scale = width / self.width
        height = self.height * scale
        self.resize(width, height)

    def rotate(self, rotation):
        angle = rotation
        resample = PIL.Image.BICUBIC
        expand = True
        center = None
        translate = None
        fillcolor = None
        self.__init__(self.image.rotate(angle, resample, expand, center, translate, fillcolor))

    def save_jpg(self, path, quality=75, dpi=0):
        self._save_jpg(path, quality, True, False, dpi, dpi, None, bytes(), "4:4:4", None)

    def _save(self, fp, format, params):
        self.image.save(fp, format, **params)

    def _save_jpg(self, path, quality, optimize, progressive, x, y, icc_profile, exif, subsampling, qtables):
        fp = path
        format = "jpeg"
        params = {
            "quality": quality,
            "optimize": optimize,
            "progressive": progressive,
            "dpi": (x, y),
            "icc_profile": icc_profile,
            "exif": exif,
            "subsampling": subsampling,
            "qtables": qtables
        }
        self._save(fp, format, params)

####
    def save_png(self, path):
        print(PIL.Image.SAVE)
        self.image.save(path, "PNG", optimize=True)
        print(PIL.Image.SAVE)
        print(breakybreaky)

    def paste(self, image, x=0, y=0):
        im = image.image
        x = Cast.float_to_integer(x)
        y = Cast.float_to_integer(y)
        box = (x, y, x + image.width, y + image.height)
        mask = None
        self.image.paste(im, box, mask)


class Canvas:
    def __del__(self):
        self.height = None
        self.ratio = None
        self.width = None

    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(round(x1))
        self.y1 = int(round(y1))
        self.x2 = int(round(x2))
        self.y2 = int(round(y2))
        self.height = self.y2 - self.y1
        self.width = self.x2 - self.x1
        self.ratio = self.width / self.height

    @classmethod
    def scale(cls, canvas, x, y):
        width = canvas.width * x
        height = canvas.height * y
        offset_x = (canvas.width - width) / 2
        offset_y = (canvas.height - height) / 2
        return cls(offset_x, offset_y, offset_x + width, offset_y + height)


JPG_QUALITY = 100
#
screen = Canvas(0, 0, 3840, 2160)
screen = Canvas(0, 0, 1920 * 4, 1080 * 4)
action_safe = Canvas.scale(screen, 0.93, 0.93)
title_safe = Canvas.scale(screen, 0.80, 0.90)
#
picture = Canvas(0, 0, screen.width, screen.width / 2)
caption = Canvas(title_safe.x1, picture.height, title_safe.x2, screen.height)
text = Canvas(0, 0, caption.width, caption.height / 3)
#
page = Canvas(0, 0, screen.height * 8.5 / 11, screen.height)
page_left = Canvas(0, 0, page.width, page.height)
page_right = Canvas(screen.width / 2, 0, page.width, page.height)




def convert_to_jpg(array):
    global screen
    global text

    (name, text_0, text_1, text_2) = array
    path = OS.join("todo", name)
    print("convert " + path)

    photo = Image.open(path)
    
    mode = "L" if photo.image.mode == "L" else "RGB"
    
    image = Image.new("RGB", screen.width, screen.height)

    #style = Style("/System/Library/Fonts/HelveticaNeue.ttc", 64)
    style = Style("/System/Library/Fonts/Supplemental/AmericanTypewriter.ttc", 128)

    line = [item for item in [text_0, text_1, text_2] if item != ""]
    lines = len(line)

    picture = Canvas(0, 0, screen.width, screen.height - (text.height*lines))
    new_width = picture.width
    new_height = picture.height
    if photo.ratio >= picture.ratio:
        new_height = round(picture.width / photo.ratio)
    else:
        new_width = round(picture.height * photo.ratio)
    photo.resize(new_width, new_height)
    offx = (picture.width - new_width) / 2
    offy = (picture.height - new_height) / 2

    image.paste(photo, offx, offy)
    draw = PIL.ImageDraw.Draw(image.image)

    if lines == 0:
        pass
    if lines == 1:
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[0], draw)
    if lines == 2:
        style.text(screen.width / 2, caption.y1 + (text.height * 1), line[0], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[1], draw)
    if lines == 3:
        style.text(screen.width / 2, caption.y1 + (text.height * 0), line[0], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 1), line[1], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[2], draw)

    image.convert(mode)

    new_name = OS.join("done", name)
    names = new_name.split(".")
    image_save = names[0] + ".jpg"
    print("saved " + image_save)
    image.save_jpg(image_save)


def make_dvd(left, right):
    name1 = OS.join("todo", left)
    name2 = OS.join("todo", right)
    print("convert " + name1)
    print("convert " + name2)
    background = Image.new_colour(screen.width, screen.height)

    image_left = Image.open(name1)
    image_left.resize_to_height(screen.height)

    image_right = Image.open(name2)
    image_right.resize_to_height(screen.height)

    screen_middle = screen.width / 2
    background.paste(image_left, screen_middle - image_left.width, 0)
    background.paste(image_right, screen_middle, 0)

    new_name = OS.join("done", left)
    names = new_name.split(".")
    image_save = names[0] + ".jpg"
    print("saved " + image_save)
    background.save_jpg(image_save)


def main(array):
    for item in array:
        convert_to_jpg(item)


def dvd(array):
    for item in Array.subdivide(array, 2):
        left = item[0]
        right = item[1]
        make_dvd(left, right)


print("finish")



print("scan")


def load_paths():
    (path, file) = OS.chdir("todo", OS.walk_directory)
    OS.chdir("done", OS.makedirs, path)
    array = []
    for (item) in file:
        root = "todo"
        (name, path) = item
        array.append(name)
    return array


def jpg_quality_test(path):
    image_open = OS.join("todo", path)
    image = Image.open(image_open)
    for quality in range(101):
        name = str(quality) + ".jpg"
        image_save = OS.join("done", name)
        print("saved " + image_save)
        image.save_jpg(image_save, quality)


paths = [
    ("28_BLACK_16_01.png", "", "", ""),
    ("60_BLACK_18_06.png", "", "", ""),
    ("23_NEGATIVE_027-BLACK_17_01.png", "", "", ""),
    ("06_NEGATIVE_244.png", "", "", ""),
    ("26_NEGATIVE_569.png", "", "", ""),
    ("42_BLACK_26_03.png", "", "", ""),
    ("18_BLACK_11_02.png", "", "", ""),
    ("55_NEGATIVE_488.png", "", "", ""),
    ("10_NEGATIVE_212.png", "", "", ""),
    ("57_NEGATIVE_214-BLACK_18_01.png", "", "", ""),
 ]

main(paths)

paths = load_paths()
paths.sort()
paths.remove(".DS_Store")
for item in paths:
    print(item + ",")

# dvd(paths)

# jpg_quality_test(paths[0])


print("done")

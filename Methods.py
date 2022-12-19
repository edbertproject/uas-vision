import cv2 as cv

# Cropping
def cropping(img):
    row = img.shape[0]
    col = img.shape[1]

    batasAtas = 0
    batasBawah = 0
    batasKiri = 0
    batasKanan = 0
    found = False

    for x in range(row):
        for y in range(col):
            if img[x, y] == 0:
                batasAtas = x
                found = True
                break
        if found:
            break

    found = False

    for x in range(row - 1, 0, -1):
        for y in range(col):
            if img[x, y] == 0:
                batasBawah = x
                found = True
                break
        if found:
            break

    found = False

    for y in range(col):
        for x in range(row):
            if img[x, y] == 0:
                batasKiri = y
                found = True
                break
        if found:
            break

    found = False

    for y in range(col - 1, 0, -1):
        for x in range(row):
            if img[x, y] == 0:
                batasKanan = y
                found = True
                break
        if found:
            break

    imageCrop = img[batasAtas:batasBawah, batasKiri:batasKanan]
    return imageCrop


def compare_percentage_bw(img):
    pixel_total = 0
    iteration = 0
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            pixel_total = pixel_total + 1
            if img[row, col] == 0:
                iteration = iteration + 1
    return iteration, pixel_total


def slicing_image(img, slice_count=5):
    min_height = int(img.shape[0] / slice_count)
    hop_height = min_height
    max_width = int(img.shape[1] / slice_count)
    hop_width = max_width

    slices = []
    for x in range(slice_count):
        startpoint_x = hop_width * x
        for y in range(slice_count):
            startpoint_y = hop_height * y
            slice_image = {
                'startpoint_x': startpoint_x,
                'startpoint_y': startpoint_y,
                'endpoint_x': startpoint_x + hop_width,
                'endpoint_y': startpoint_y + hop_height
            }
            slices.append(slice_image)

    return slices


def image_slice_to_percentage(img, image_slices):
    percentages = []
    for slice in image_slices:
        curr = img[slice['startpoint_x']: slice['endpoint_x'], slice['startpoint_y']: slice['endpoint_y']]
        result = compare_percentage_bw(curr)
        ratio = (result[0] / result[1]) * 100
        percentages.append(round(ratio, 3))
    return percentages


def lower_brightness(img):
    row = img.shape[0]
    col = img.shape[1]
    sec = img.shape[2]
    for i in range(row):
        for j in range(col):
            for k in range(sec):
                img[i][j][k] = abs(img[i][j][k] - 50)
    return img


def adjust_contrast(img):
    row = img.shape[0]
    col = img.shape[1]
    sec = img.shape[2]
    for i in range(row):
        for j in range(col):
            for k in range(sec):
                img[i][j][k] *= 1.5
                if img[i][j][k] > 255:
                    img[i][j][k] = 255
    return img


def read_image_percentage(path):
    img = cv.imread(path)

    img = lower_brightness(img)

    img = adjust_contrast(img)

    # Grayscale
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("Gray", img)

    # Contrass
    # for i in range(row):
    #     for j in range(col):
    #         img[i][j] = int(img[i][j] * 1.1)
    #         if img[i][j] > 255:
    #             img[i][j] = 255
    #         elif img[i][j] < 0:
    #             img[i][j] = 0

    # for i in range(row):
    #     for j in range(col):
    #         img[i][j] -= 10
    #         if img[i][j] < 0:
    #             img[i][j] = 0

    # cv.imshow("B&C", img)

    # Blurring
    img = cv.GaussianBlur(img, (7, 7), 0)
    # cv.imshow("blured", img)

    # Binary
    th, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    # cv.imshow("Binary", img)

    img = cv.morphologyEx(img, cv.MORPH_OPEN, (3, 3), iterations=2)
    # cv.imshow("Erode", img)

    img = cropping(img)
    # cv.imshow("Cropped", img)

    # Resize image
    img = cv.resize(img, (200, 200), interpolation=cv.INTER_AREA)
    # cv.imshow("Resized image", img)

    image_slices = slicing_image(img, 6)

    return image_slice_to_percentage(img, image_slices)

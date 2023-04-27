i = 1
image = 0
def money(j, image1):
    if j < 2:
        image1 = 1000
    if j == 2:
        image1 += 1
    return image1


while i < 3:
    image = money(i, image)
    print(image)
    i += 1
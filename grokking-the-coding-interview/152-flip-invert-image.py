def flip_and_invert_image(image):
    for row in image:
        mid = len(row) // 2
        for i in range(mid + len(row) % 2):
            row[i], row[len(row) - 1 - i] = 1 ^ row[len(row) - 1 - i], 1 ^ row[i]  # Invert before swapping
    return image
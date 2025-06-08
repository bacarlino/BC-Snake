
def get_available_cell_sizes(width, height):

    avail_widths = []
    avail_heights = []

    for i in range(1, width + 1):
        if width % i == 0:
            avail_widths.append(i)
        if height % i == 0:
            avail_heights.append(i)

    return [num for num in avail_widths if num in avail_heights and num >= 16]
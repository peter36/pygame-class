import math


def print_circle(radius):
    size = radius * 2 + 1
    center = radius
    for y in range(0, size):
        line = ''
        for x in range(0, size):
            # We need to get the integer value for the tx value below
            # tx = math.sqrt(radius*radius - (center-y)*(center-y))
            tx = int(math.sqrt(radius*radius - (center-y)*(center-y)) + 0.5)
            if (x == center + tx) or (x == center - tx):
                line = line + '*'
            else:
                line = line + ' '
        print(line)


if __name__ == "__main__":
    print_circle(8)

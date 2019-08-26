import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Lunar Lander')
    parser.add_argument('--scale', '-s', type=int,
                        help='Set to 1 for normal screens, 2 for 4k screens to make the game bigger')

    args = parser.parse_args()
    print(args)
    return args



args = parse_args()
SCALE = args.scale

class MRect:
    def __init__(self, x_pos, y_pos, x, y):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x = x
        self.y = y

    def __str__(self):
        return f'Rectangle {self.x_pos}, {self.y_pos}, {self.x}, {self.y}'


class ScaledMRect(MRect):
    def __init__(self, x_pos, y_pos, x, y):
        super().__init__(x_pos * SCALE,
                       y_pos * SCALE,
                       x * SCALE,
                       y * SCALE)


def main():
    global SCALE

    args = parse_args()
    SCALE = args.scale
    print(f"args.scale: {args.scale}  SCALE: {SCALE}")
    my_rect = MRect(20, 20, 10, 10)
    print(my_rect)

    myScaledRet = ScaledMRect(20, 20, 10, 10)
    print(myScaledRet)

    del SCALE


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        raise e

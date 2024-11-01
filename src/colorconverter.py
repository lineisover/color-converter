import struct
import argparse


def dec_to_rgba(r, g, b, a):
    packed_color = struct.pack('BBBB', b, g, r, a)
    dec_color = struct.unpack('i', packed_color)[0]
    print(dec_color)


def rgba_to_dec(color):
    b, g, r, a = struct.pack('i', color)
    print(f'r: {r}, g: {g}, b: {b}, a: {a}')


def main():
    parser = argparse.ArgumentParser(description='Color converter')
    
    parser.add_argument('-mode', help='Выбор режима конвертирования: "dec_to_rgba" для конвертации из десятичного кодирования в RGBA или "rgba_to_dec" для конвертации из RGBA в десятичное кодирование')
    parser.add_argument('-color', help='Десятичное значение цвета (только для режима "dec_to_rgba")')
    parser.add_argument('-r', help='Значение красного канала (только для режима "rgba_to_dec")')
    parser.add_argument('-g', help='Значение зеленого канала (только для режима "rgba_to_dec")')
    parser.add_argument('-b', help='Значение синего канала (только для режима "rgba_to_dec")')
    parser.add_argument('-a', help='Значение альфа-канала (только для режима "rgba_to_dec")')

    args = parser.parse_args()

    if args.mode == 'dec_to_rgba':
        rgba_to_dec(int(args.color))
    elif args.mode == 'rgba_to_dec':
        dec_to_rgba(int(args.r), int(args.g), int(args.b), int(args.a))

    
if __name__ == '__main__':
    main()

# 1 - blue
# 2 - green
# 3 - red
# 4 - alpha
import os
import sys
import glob
import cv2
import numpy as np
import argparse


def main():
    parser = argparse.ArgumentParser(description='Lane detection script')
    parser.add_argument('path', type=str, help='Images directory')
    parser.add_argument('factor', type=float, help='Reduce image factor')
    parser.add_argument('write', type=bool, default=False, help='Write images')
    parser.add_argument('--type', type=str, default='jpeg', help='Image type')
    args = parser.parse_args()

    files = None
    if os.path.exists(args.path):
        if os.path.isdir(args.path):
            path = ''.join([args.path, '/*.', args.type])
            files = glob.glob(path)
        elif os.path.isfile(args.path):
            files = [args.path]
    else:
        print('No Such file or directory')
        sys.exit(1)
    if not files:
        print('Directory empty')
        sys.exit(1)

    for file in files:
        img = cv2.imread(file)
        h, w = img.shape[:2]
        img_resize = cv2.resize(
            img, (int(w * args.factor), int(h * args.factor)))
        if args.write:
            cv2.imwrite(file, img_resize)


if __name__ == '__main__':
    main()

import argparse
import io
import os
import sys

import lmdb

from PIL import Image

def get_args():
    parser = argparse.ArgumentParser(
        'Extract Modanet images from Chictopia LMDB dataset'
    )
    parser.add_argument("modanet_filenames", help="List of Modanet filenames")
    parser.add_argument("chictopia_lmdb", help="Chictopia LMDB dataset path")
    parser.add_argument("output_dir", help="Directory to write Modanet images to")
    return parser.parse_args()

def main():
    args = get_args()

    with open(args.modanet_filenames, 'r') as files:
        ids = map(lambda s: int(os.path.splitext(s)[0]), files.readlines())

    e = lmdb.open(args.chictopia_lmdb, map_size=2**36, readonly=True, lock=False)
    with e.begin() as t:
        for i in ids:
            d = t.get(str(i).encode('ascii'))
            with io.BytesIO(d) as f:
                image = Image.open(f)
                fname = '%07d.jpg' % i
                image.save(args.output_dir + '/' + fname, 'JPEG')

if __name__ == "__main__":
    main()

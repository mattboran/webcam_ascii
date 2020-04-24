#!/usr/bin/env python
import sys

import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image


def frame_to_chars(frame):
    chars = np.asarray(list(' .,:irs?@9B&#'))
    char_map = {i: e for i, e in enumerate(chars)}
    # Convert to black and white, make low res
    bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    low_res = cv2.resize(bw_frame, (80, 40))
    low_res = cv2.flip(low_res, 1).astype(np.uint8)
    char_indices = (low_res / 255 * (chars.size - 1)).astype(np.uint8)
    # Convert ints to characters using the char_map
    c, inv = np.unique(char_indices, return_inverse=True)
    as_chars = np.array([char_map[x] for x in c])[inv].reshape(low_res.shape)
    return "\n".join(["".join(row) for row in as_chars])

def main():
    # Capture from /dev/video0
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    font = ImageFont.truetype("./VeraMono.ttf", 10)
    while(True):
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()
            text = frame_to_chars(frame)
            # Write to PIL image
            blank_img = np.zeros((580, 500))
            pil_img = Image.fromarray(blank_img)
            draw = ImageDraw.Draw(pil_img)
            draw.text((0, 0), text, font=font)
            # Convert back to np array and write to stdout
            np_img = np.array(pil_img).astype(np.uint8) * 255
            np_img = cv2.resize(np_img, (320, 240), interpolation=cv2.INTER_AREA)
            sys.stdout.buffer.write(np_img.tostring())
            sys.stdout.buffer.flush()
        except KeyboardInterrupt:
            break
    cap.release()

if __name__ == '__main__':
    main()

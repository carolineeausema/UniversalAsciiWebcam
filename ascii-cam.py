#!/usr/bin/env python

__author__ = "Caroline Ausema"
__date__ = "30 March 2022"
__email__ = "carolineeausema@gmail.com"

"""
Simple VideoCapture program that converts gray tones to
ASCII values.

used SamyBencherif's shellMode tutorial:
https://gist.github.com/SamyBencherif/29a0a945cabff92a4b61d78a5fe072a5
"""

import cv2
import numpy as np


def main():
    capture = cv2.VideoCapture(0)

    # TODO: attach time delay

    frame_w = 600   # set up granola camera
    frame_h = 400
    capture.set(3, frame_w)
    capture.set(4, frame_h)
    capture.set(10, 150)

    if capture.isOpened():
        rvalue, frame = capture.read()
    else: # throw an error if unopened
        rvalue = False
        raise ValueError('Err: no camera access')

    while capture.isOpened():
        rvalue, frame = capture.read()
        print(convert_to_ascii(frame))
        if (rvalue):
            cv2.imshow("woooah ur so cute", frame)
# TODO: add break on KeyboardInterrupt


# TODO: add adjustable height/width
def convert_to_ascii(frame, num_columns = 60, num_rows = 17):
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  height, width = frame.shape # create template
  # throw an error if the height/width exceeds input limit
  if num_columns > width or num_rows > height:
      raise ValueError('Err: num rows or columns exceeded limit')
  term_width = width / num_columns
  term_height = height / num_rows

  output = ""   # add characters to return var
  for i in range(num_rows):
    for j in range(num_columns):
        scale_height = int(i * term_height)
        comp_height = int(min(term_height * int((i + 1)), height))
        scale_width = int(j * term_width)
        comp_width = int(min(int(term_width * int((j + 1))), width))

        # calculates the average amt of lightness in graytone
        light = np.mean(frame[scale_height:comp_height, scale_width:comp_width])
        output += choose_chars(light) # gets the right ascii val
    output += '\n'

  return output


# w3 recommend: ' .:-=+*#%@'
def choose_chars(light):
  scale = ' .;-=+*$@#?'
  length = len(scale)
  return scale[min(int(light * length / 255), length - 1)]


if __name__ == '__main__':
    main()

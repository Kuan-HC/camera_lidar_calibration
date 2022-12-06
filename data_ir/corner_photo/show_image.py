#!/usr/bin/env python

import cv2
import numpy as np
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='show image')
    parser.add_argument('--path', type=str, help='file to read')
    args = parser.parse_args()
    return args

def show_image(args):

    cv2.namedWindow('show image, ESC to close', cv2.WINDOW_NORMAL)

    frame = cv2.imread(args.path)
    
    cv2.imshow('show image, ESC to close', frame)

    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()    
   

if __name__=='__main__':
    args = get_args()
    show_image(args)   
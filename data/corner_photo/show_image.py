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
    mtx = np.loadtxt('mtx.txt')
    newcameramtx = np.loadtxt('newcameramtx.txt')
    dist = np.loadtxt('dist.txt')

    undistort_image = cv2.undistort(frame, mtx, dist, None, newcameramtx)
    
    cv2.imshow('show image, ESC to close', undistort_image)

    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()    
   

if __name__=='__main__':
    args = get_args()
    show_image(args)   
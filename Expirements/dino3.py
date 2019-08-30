import time

import cv2
import numpy as np
import pyautogui as pg
from mss.linux import MSS as mss

mon = {'top': 480, 'left': 130, 'width': 70, 'height': 35}


def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def screen_record():
    sct = mss()
    last_time = time.time()

    while (True):
        img = sct.grab(mon)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        img = np.array(img)
        processed_image = process_image(img)
        mean = np.mean(processed_image)
        print('mean = ', mean)

        if not mean == float(0):
            pg.press('space')

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()
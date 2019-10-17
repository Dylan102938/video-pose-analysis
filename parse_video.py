import os
import math

import cv2


def cleardirectory(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)

        except Exception as e:
            print(e)


def parsevideo(file, path):
    cap = cv2.VideoCapture(file)
    framerate = cap.get(5)  # frame rate
    x = 1
    while cap.isOpened():
        frameid = cap.get(1)  # current frame number
        ret, frame = cap.read()

        if not ret:
            break

        if frameid % math.floor(framerate / math.floor(1/0.15)) == 0:
            filename = path + 'frame' + str(int(x)).zfill(6) + ".jpg"
            print(filename)
            x += 1
            cv2.imwrite(filename, frame)

    cap.release()
    print("Done!")


def main():
    path = "videos/"
    base_extension_file = "derek.mp4"
    base_file = path + base_extension_file

    compare_extension_file = "derek2.mp4"
    compare_file = path + compare_extension_file

    base_videos = "images/base-videos/"
    compare_videos = "images/compare-videos/"

    # clear image folders
    cleardirectory(base_videos)
    cleardirectory(compare_videos)

    # parse videos
    parsevideo(base_file, base_videos)
    parsevideo(compare_file, compare_videos)



if __name__ == '__main__':
    main()

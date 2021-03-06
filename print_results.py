import json
import math
import os
import shutil
import os
import pose_similarity

part_names = ["head", "neck", "rshoulder", "relbow", "rhand", "lshoulder", "leblow", "lhand",
                  "rhip", "rknee", "rfoot", "lhip", "lknee", "lfoot", "reye", "leye", "rear", "lear"]


def min(arr1, arr2):
    if len(arr1) > len(arr2):
        return len(arr2)

    return len(arr1)


def cleardirectory(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)

        except Exception as e:
            print(e)


def main():
    # load base json info
    with open("pose-json/base-poses.json", 'r') as file:
        info = json.loads(file.readline())
        video1json = info['frames']

    # load json to compare info
    with open("pose-json/compare-poses.json", 'r') as file:
        info = json.loads(file.readline())
        video2json = info['frames']

    video1 = [[0 for x in range(36)] for y in range(min(video1json, video2json))]
    video2 = [[0 for x in range(36)] for y in range(min(video1json, video2json))]

    framesoff = 0
    frameswrong = []
    for i in range(0, min(video1json, video2json)):
        counter = 0
        for j in range(0, 18):
            video1[i][counter] = video1json[i][part_names[j] + 'x']
            video2[i][counter] = video2json[i][part_names[j] + 'x']
            counter += 1
            video1[i][counter] = video1json[i][part_names[j] + 'y']
            video2[i][counter] = video2json[i][part_names[j] + 'y']
            counter += 1

    for i in range(0, len(video1)):
        print("Average error on frame " + str(i + 1) + ": " + "%.3f" % pose_similarity.averageError(i, video1, video2))

        if pose_similarity.averageError(i, video1, video2) > 0.2:
            framesoff += 1
            frameswrong.append(i)

    print("--------------------------------")
    print(str(framesoff) + " frames of " + str(min(video1json, video2json)) + " wrong")
    print("Percent accurate: " + str(1 - framesoff / min(video1json, video2json)))
    print("Frames wrong: ")
    for frame in frameswrong:
        print("Frame " + str(frame + 1))

    cleardirectory('errorimages')

    for frame in frameswrong:
        basefilename = 'images/base-videos/' + 'frame' + str(frame).zfill(6) + ".jpg"
        comparefilename = 'images/compare-videos/' + 'frame' + str(frame).zfill(6) + ".jpg"
        if os.path.isfile(basefilename):
            shutil.copy(basefilename, 'errorimages/base-' + '%.3f' % (frame*0.1) + 's.jpg')
        if os.path.isfile(comparefilename):
            shutil.copy(comparefilename, 'errorimages/compare-' + '%.3f' % (frame*0.1)  + 's.jpg')


if __name__ == "__main__":
    main()
import json
import math

import pose_similarity

part_names = ["head", "neck", "rshoulder", "relbow", "rhand", "lshoulder", "leblow", "lhand",
                  "rhip", "rknee", "rfoot", "lhip", "lknee", "lfoot", "reye", "leye", "rear", "lear"]


def main():
    frame1 = [[0 for x in range(36)] for y in range(1)]
    frame2 = [[0 for x in range(36)] for y in range(1)]

    with open("pose-json/base-poses.json", 'r') as file:
        info = json.loads(file.readline())
        frame1json = info['frames'][0]
        frame2json = info['frames'][1]
        # print(json.dumps(info, indent=4))

        counter = 0
        for i in range(0, 18):
            frame1[0][counter] = frame1json[part_names[i] + 'x']
            frame2[0][counter] = frame2json[part_names[i] + 'x']
            counter += 1
            frame1[0][counter] = frame1json[part_names[i] + 'y']
            frame2[0][counter] = frame2json[part_names[i] + 'y']
            counter += 1

        print(frame1)
        print(frame2)

        print("Average error: " + str(pose_similarity.averageError(0, frame1, frame2)))


if __name__ == "__main__":
    main()
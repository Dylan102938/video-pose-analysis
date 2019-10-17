import logging
import sys
import time
import json

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from tf_pose import common
import os
import cv2

w, h = model_wh('432x368')
resize_out_ratio = 4.0

e = TfPoseEstimator(get_graph_path("cmu"), target_size=(w, h))


def pose_estimate(path, path_write):
    images = os.listdir(path)
    images.sort()
    print(images)
    humans_json = {}
    humans_json['frames'] = []
    with open(path_write, "w") as outfile:
        outfile.write('{"frames": [')

    part_names = ["head", "neck", "rshoulder", "relbow", "rhand", "lshoulder", "leblow", "lhand",
                  "rhip", "rknee", "rfoot", "lhip", "lknee", "lfoot", "reye", "leye", "rear", "lear"]
    count = 0
    for file in images:
        image = common.read_imgfile(os.path.join(path, file), None, None)
        if image is None:
            sys.exit(-1)

        t = time.time()
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=resize_out_ratio)

        # body parts
        frame_content = '{'
        for i in range(0, 18):
            try:
                body_part = humans[0].body_parts[i]
            except:
                body_part = -1

            if body_part != -1:
                frame_content += '"' + part_names[i] + 'x":' + str(body_part.x * image.shape[1]) + ", "
                frame_content += '"' + part_names[i] + 'y":' + str(body_part.x * image.shape[0]) + ", "
            else:
                frame_content += '"' + part_names[i] + 'x":' + "-1, "
                frame_content += '"' + part_names[i] + 'y":' + "-1, "

        frame_content = frame_content[:-2]
        frame_content += '},'

        with open(path_write, 'a') as outfile:
            if count == len(images) - 1:
                outfile.write(frame_content[:-1])
            else:
                outfile.write(frame_content)

        elapsed = time.time() - t
        count += 1

        print("Finished " + file, " in ", elapsed)
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
        cv2.imwrite(os.path.join(path, file), image)

    with open(path_write, 'a') as outfile:
        outfile.write(']}')

def main():

    # clear directory
    for file in os.listdir("pose-json"):
        file_path = os.path.join("pose-json", file)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)

        except Exception as e:
            print(e)

    # run pose estimation
    pose_estimate("images/base-videos", "pose-json/base-poses.json")
    pose_estimate("images/compare-videos", "pose-json/compare-poses.json")


if __name__ == '__main__':
    main()

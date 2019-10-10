import logging
import sys
import time

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
from tf_pose import common
import os
import parse_video

logger = logging.getLogger('TfPoseEstimatorRun')
logger.handlers.clear()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

e = TfPoseEstimator(get_graph_path("cmu"), target_size=(432, 368))


def pose_estimate(path, path_write):
    images = os.listdir(path)

    for file in images:
        image = common.read_imgfile(os.path.join(path, file), None, None)
        if image is None:
            logger.error('Image can not be read, path=%s' % image)
            sys.exit(-1)

        t = time.time()
        humans = e.inference(image, resize_to_default=True)
        elapsed = time.time() - t
        logger.info('inference image: %s in %.4f seconds.' % (image, elapsed))


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
    parse_video
    main()

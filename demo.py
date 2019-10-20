import parse_video
import pose_estimate
import pose_similarity
import json
import argparse
import printout

def main():
    parser = argparse.ArgumentParser(description='tf-pose-estimation run')
    parser.add_argument('--basefile', type=str, default='./base-video.mp4')
    parser.add_argument('--comparefile', type=str, default='./compare-video.mp4')
    args = parser.parse_args()

    comparefile = args.comparefile
    basefile = args.basefile

    parse_video.main(basefile, comparefile)
    pose_estimate.main()
    printout.main()

if __name__ == "__main__":
    main()
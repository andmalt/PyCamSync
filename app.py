import argparse
from configparser import RawConfigParser
import os
import sys
import time
from src.cam import record_video
sys.path.append('..')

def loadIni(filename):
    if (os.path.isfile(filename)):
        config = RawConfigParser()
        config.read(filename)
        return config
    else:
        print("ERROR: Configuration file not found")
        sys.exit(1)


def main(config:RawConfigParser,fps:float,size,args_time):
    while True:
        try:
            record_video(config,fps,size,args_time)
        except Exception as e:
            print("Exception webcam")
            print(e)
        time.sleep(args_time + 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='pycamsync',
                                     description='This program runs the webcam to record and save the file in a directory set by you',
                                     epilog='2023 Andrea Maltempi')

    parser.add_argument('-i', '--ini', help='Path to INI file (default ./pycamsync.ini)',
                        action='store', required=False, default='./pycamsync.ini')
    parser.add_argument('-f', '--fps', help='Set your desired fps example: 30',
                        action='store', required=False, type=float,default='30')
    parser.add_argument('-s', '--size', help='Set your desired resolution example: 640,480 ',
                        action='store', required=False, default='640,480')
    parser.add_argument('-t', '--time', help='Set the maximum time of videos in seconds.',
                        action='store', required=False,type=int, default='600')

    print("\nPyCamSync Version 1.0")
    print("--------------------------------------------------")
    print("2023 Andrea Maltempi.\n")

    args = parser.parse_args()
    # print(type(args.fps))

    # Reading the configuration file
    config = loadIni(args.ini)

    main(config,args.fps,args.size,args.time)
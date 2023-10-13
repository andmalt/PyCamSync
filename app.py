# from cam import record_video
import argparse
from configparser import RawConfigParser
import os
import sys
import time
from src.cam import record_video

def loadIni(filename):
    if (os.path.isfile(filename)):
        config = RawConfigParser()
        config.read(filename)
        return config
    else:
        print("ERROR: Configuration file not found")
        sys.exit(1)


def main(config:RawConfigParser):
    record_video(config)
    # while True:
    #     time.sleep(120)
    #     try:
    #         record_video(config)
    #     except Exception as e:
    #         print("Exception webcam")
    #         print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='pycamsync',
                                     description='This program runs the webcam to record and save the file in a directory set by you',
                                     epilog='(C) 2023 Andrea Maltempi, All rights reserved.')

    parser.add_argument('-i', '--ini', help='Path to INI file (default ./pycamsync.ini)',
                        action='store', required=False, default='./pycamsync.ini')

    print("\nPyCamSync Version 1.0")
    print("--------------------------------------------------")
    print("(C) 2023 Andrea Maltempi - All rights reserved.\n")

    args = parser.parse_args()

    # Lettura del file di configurazione
    config = loadIni(args.ini)

    main(config)
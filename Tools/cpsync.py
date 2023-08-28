#!/usr/bin/python3
## Editor-independent tool for uploading CircuitPython to the processor
## Initially developed for Mechatronics 1 course
## Author:  Joseph T. Foley <foley AT RU DOT IS>
## Start Date: 2023-08-28




import os
import argparse
import logging


# Which OS are we in?
#import platform
#if platform.system() == "Linux":
#    print("Linux")
#elif platform.system() == "Windows":
#    print("Windows")
#else:
#    print("Mac")


def main():
    """Main program loop"""
    print("""CircuitPython Sync by Joseph. T. Foley<foley AT ru DOT is>
    From https://github.com/RU-V207-Teaching/strasbourg-robotkit""")          
    parser = argparse.ArgumentParser(
        description="Sync files with CirPy")
    parser.add_argument('--log', default="INFO",
        help='Console log level:  Number or DEBUG, INFO, WARNING, ERROR')

    args = parser.parse_args()
    ## Set up logging
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log)
    #print(f"Log level:  {numeric_level}")
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    # log everything to file
    ## TODO:  common logger for all modules
    logpath = 'cpsync.log'
    fh = logging.FileHandler(logpath)
    fh.setLevel(logging.DEBUG)
    # log to console
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)
    # create formatter and add to handlers
    consoleformatter = logging.Formatter('%(message)s')
    ch.setFormatter(consoleformatter)
    spamformatter = logging.Formatter('%(asctime)s %(name)s[%(levelname)s] %(message)s')
    fh.setFormatter(spamformatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info("Starting to log CpSync to log file %s", logpath)

if __name__ == "__main__":
    main()

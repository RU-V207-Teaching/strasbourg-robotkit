#!/usr/bin/python3
## Editor-independent tool for uploading CircuitPython to the processor
## Initially developed for Mechatronics 1 course
## Author:  Joseph T. Foley <foley AT RU DOT IS>
## Start Date: 2023-08-28

## Installation on Windows:
## pip install pywin32

import os
import argparse
import logging
import platform
from pathlib import Path
import shutil

# Which OS are we in?
#import platform
#if platform.system() == "Linux":
#    print("Linux")
#elif platform.system() == "Windows":
#    print("Windows")
#else:
#    print("Mac")
class CircuitPythonSync():
    """Sync files to CircuitPython device"""
    def __init__(self,args, logger):
        self.args = args
        self.logger = logger
        self.dest = None
    def finddestination(self):
        "Is there a CircuitPython drive attached?  Find it"
        if platform.system() == "Windows":
            # we have to enumerate through the drives
            # Based upon https://stackoverflow.com/questions/8319264/how-can-i-get-the-name-of-a-drive-in-python
            # By Shubham Rakshe
            import win32api
            import win32con
            import win32file
            
            drives = [i for i in win32api.GetLogicalDriveStrings().split('\x00') if i]
            #print(drives)
            drive_list = [d for d in drives if win32file.GetDriveType(d) == win32con.DRIVE_REMOVABLE]
            for i in drive_list:
                volname = win32api.GetVolumeInformation(i)[0]
                self.logger.debug(f"volume:{volname} at {i}")
                if volname == "CIRCUITPY":
                    ## found one.  What do we do if there are more?
                    self.logger.info(f"Found CircuitPython device on {i}")                    
                    self.dest = i
                    break
                
        
        elif platform.system() == "Linux":
            self.logger.error("Linux not implemented yet")
            system.exit(0)
        else:
            self.logger.error("Mac not implemented yet")
            system.exit(0)

    def clearoldcode(self, codeglob="*.py"):
        "Clear out any old .py files"
        if not self.dest:
            raise OSError("CircuitPython Drive not set")
        for p in Path(self.dest).glob(codeglob):
            self.logger.info(f"Removing {p}")
            os.remove(p)
            
    def installnewfiles(self, codeglob="*.py"):
        "Copy new files over and rename main file if needed"
        # grab everything in the source directory
        #TODO: look at a manifest?
        for p in Path(self.args.src).glob(codeglob):
            self.logger.info(f"Copying {p} to {self.dest}")
            shutil.copy2(p,self.dest)
        
    
def main():
    """Main program loop"""
    print("""CircuitPython Sync by Joseph. T. Foley<foley AT ru DOT is>
    From https://github.com/RU-V207-Teaching/strasbourg-robotkit""")          
    parser = argparse.ArgumentParser(
        description="Sync files with CirPy")
    parser.add_argument('--log', default="INFO",
        help='Console log level:  Number or DEBUG, INFO, WARNING, ERROR')
    parser.add_argument('--src', default=".",
        help='Where to get CircuitPython code from')
    parser.add_argument('--main',
        help='file to rename to code.py')

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
    CPS = CircuitPythonSync(args,logger)
    CPS.finddestination()
    CPS.clearoldcode()
    CPS.installnewfiles()
    
    
if __name__ == "__main__":
    main()
    

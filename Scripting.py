# get info about operating system
import os
# Work with json files
import json
# Copy and overwrite operation
import shutil
import sys
# Run any terminal command
from subprocess import PIPE, run
# Get access to command line argument

patternToSearchFor = "_project"

"""- This function searches for directories
   that matches a string 
   It returns a list of those directories
"""
def findAllMatchingDir(sourcePath):
    matchDir = []
    for root, dirs, files in os.walk(sourcePath):
        for directory in dirs:
            if patternToSearchFor in directory.lower():
                path = os.path.join(sourcePath, directory)
                matchDir.append(path)
        break
    return matchDir

"""- This function removes the string
    pattern and return the list of 
    directories
"""
def SanitizedDir(sourceList, toRemove):
    sanitizedList = []
    for sourceItem in sourceList:
        _,dir_name = os.path.split(sourceItem)
        new_dirName = dir_name.replace(toRemove, "")
        sanitizedList.append(new_dirName)
    return sanitizedList


"""- This function creates a new diretory
    with the directories we found
"""
def createTargetFolder(dirToCreate, folderPath):
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
        os.chdir(folderPath)
        for dir in dirToCreate:
            os.mkdir(dir)



def main(mainSource, mainTarget):
    currentWD = os.getcwd()
    source_path = os.path.join(currentWD, mainSource)
    target_Path = os.path.join(currentWD, mainTarget)
    returnedMatchingDir = findAllMatchingDir(source_path)
    sanitizedDirList = SanitizedDir(returnedMatchingDir, patternToSearchFor)
    createTargetFolder(sanitizedDirList, target_Path)
    print(sanitizedDirList)

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 3:
        raise Exception("Hey please put 3 arguments! The file, the source and target folder!")
    source, target = args[1:]
    main(source, target)


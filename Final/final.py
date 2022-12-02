import os
import hashlib

print("Welcome to the NAME IN PROGRESS")
print("Looking for hash database...")
currentpath = os.path.abspath(__file__)
currentdir = os.path.split(currentpath)
hashdbpath = currentdir[0] + "/hashes.txt"

if os.path.exists(hashdbpath):
    print("Hash database found")
else:
    print("Hash database not found. Creating...")
    with open('hashes.txt', 'w') as newdb:
        pass

def compareDB(a):
    with open('hashes.txt', "r") as db:
        lines = db.readlines()
        for item in lines:
            if item.find(a) != -1:
                return True

def writeHashes(a):
    with open("hashes.txt", "a") as myfile:
         myfile.write(a)
         myfile.write("\n")
                        
def checkHashes():
    go = True
    t = False
    while go:
        x = input("Enter 32 digit MD5 hash to check against database: ")
        if len(x) != 32:
            print("That wasn't 32 digits.")
        else:
            t = True
            go = False
    if t == True:
        with open('hashes.txt', "r") as db:
            count = 0
            lines = db.readlines()
            for item in lines:
                if item.find(x) != -1:
                    count += 1
            if count >= 1:
                print("Hash match found")
            else:
                print("No hash match found")


def addHashes():
    go = True
    while go:
        x = input("Select target directory or file: ")
        if os.path.exists(x):
            if os.path.isfile(x):
                h = hashlib.md5(x.encode('UTF-8')).hexdigest()
                if not compareDB(h):
                    with open("hashes.txt", "a") as myfile:
                        myfile.write(h)
                        myfile.write("\n") 
                print("Hash added")
                go = False
            elif os.path.isdir(x):
                for root, dirs, files in os.walk(x, topdown=False):
                    for elem in files:
                        h = hashlib.md5(elem.encode('UTF-8')).hexdigest()
                        if not compareDB(h):
                            with open("hashes.txt", "a") as myfile:
                                myfile.write(h)
                                myfile.write("\n")
                    for elem in dirs:
                        h = hashlib.md5(elem.encode('UTF-8')).hexdigest()
                        if not compareDB(h):
                            with open("hashes.txt", "a") as myfile:
                                myfile.write(h)
                                myfile.write("\n")
                print("Hashes added.")
                go = False
                    
        else:
            print("Directory or file not found.")

def startProgram():

    go = True
    while go:
        print("1 - Add hashes to table")
        print("2 - Compare file hash to stored table")
        inp = input("Select an option: ")
        if inp == '1':
            addHashes()
        elif inp == '2':
            checkHashes()
        else:
            print("Invalid input.")

startProgram()

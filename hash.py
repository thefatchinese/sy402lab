import csv
import hashlib
import datetime
import os

donothash = ["vmlinuz.old", "boot", "snap", "etc", "usr", "lib",  "dev", "proc", "run", "sys", "tmp", "var/lib", "var/run", "var/spool", "var"]

def main():
    if os.path.exists("/tmp/sy402lab/output.txt"):
        hashagain()
        quit()
    else:
        firsthash()
        quit()

def firsthash():
    list = []
    directories = os.listdir("/")
    f = open("/tmp/sy402lab/output.txt", "w")
    for directory in directories:
        list.append(directory)
    for item in list:
        if item in donothash:
            continue
        else:
            for root, dirs, files in os.walk("/" + item):
                for file in files: 
                    if ((root.find("var/lib") == True) or (root.find("var/run") == True) or (root.find("var/spool") == True) or (root.find("var/cache") == True)):
                        continue
                    if root.find("home/tina/") == True:
                        continue
                    filepath = os.path.join(root, file)
                    fpath = open(filepath, "rb")
                    time = datetime.datetime.now()
                    bytes = fpath.read()
                    hash = hashlib.sha256(bytes).hexdigest()
                    total = filepath + ", " + hash + ", " + str(time) + "\n"
                    print(total)
                    f.write(total)
    f.close()

def hashagain():
    list = []
    directories = os.listdir("/")
    grandtotal = open("/tmp/sy402lab/output.txt", "r").readlines()
    updated = open("/tmp/sy402lab/updatedversion.txt", "w")
    f2 = open("/tmp/sy402lab/output2.txt", "w")
    for directory in directories:
        list.append(directory)
    for item in list:
        if item in donothash:
            continue
        else:
            for root, dirs, files in os.walk("/" + item):
                for file in files: 
                    if ((root.find("var/lib") == True) or (root.find("var/run") == True) or (root.find("var/spool") == True) or (root.find("var/cache") == True)):
                        continue
                    if root.find("home/tina/") == True:
                        continue
                    filepath = os.path.join(root, file)
                    fpath = open(filepath, "rb")
                    time = datetime.datetime.now()
                    bytes = fpath.read()
                    hash = hashlib.sha256(bytes).hexdigest()
                    total = filepath + ", " + hash + ", " + str(time) + "\n"
                    f2.write(total)
                    if any(hash in line for line in grandtotal) == False:
                        updated.write("New file: " + total)
    f2.close()
    updated.close()

main()

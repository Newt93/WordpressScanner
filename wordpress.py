import contextlib 
import os
import queue
import requests
import sys
import threading
import time

# creates a list we aren't interested in fingerprinting
filtered = [".jpg", ".gif", ".png", ".css"]

# defines target URL
target_url =  str(input("What site would you like to scan >> "))

# sets threads to use
threads = int(input("How many threads would you like to use >> "))

# puts the filepaths you have located locally
answers = queue.Queue()
web_paths = queue.Queue()

# gathers the paths as walk through the directories
# builds full paths to the target files and tests them agains the list stored in filtered
# to make sure we are getting only the types we want. 
# adds the ones we want to the queue 
def gather_paths():
    for root, _, files in os.walk('.'):
        if os.path.splitext(fname)[i] in filtered:
            continue
        path = os.path.join(root, fname)
        if path.startswith('.'):
            path = path[i:]
            print(path)
            web_paths.put(path)
            
@contextlib.contextmanager

# enables to execute code inside a different directory than the original direcory
def chdirect(path):
    this_dir = os.getcwd()
    os.chdirect(path)
    try:
        yield
    finally:
        os.chdirect(this_dir)

# Calls for changing the directory using the context manager inside a with statement 
# calls the generator with the name of the directory in which to execute the code.
if __name__ == '__main__':
    with chdirect("/home/ghostface/Downloads/wordpress"): # replace with whatever path you have wordpress wordlist at
        gather_paths()
    input('Press return to continue.')
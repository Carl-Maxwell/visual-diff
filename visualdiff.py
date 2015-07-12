#! /usr/bin/env python

import argparse

from os import path, system

parser = argparse.ArgumentParser(description='Use meld to visually see changes between your working branch and github git repositories')

working = path.realpath("./")

name = working.split("/")[-1]

tree = "/".join(working.split("/")[0:-1]) + "/trees/" + name

print("clearing out any changes in tree")
system("git --git-dir=" + tree + "/.git checkout .")
print("updating tree")
system("git --git-dir=" + tree + "/.git pull")

print("calling meld")
system("meld " + tree + " " + working)

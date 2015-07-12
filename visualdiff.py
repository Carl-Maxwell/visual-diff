#! /usr/bin/env python

import argparse

from os import path, system

parser = argparse.ArgumentParser(description='Use meld to visually see changes between your working branch and github git repositories')

working = path.realpath("./")

name = working.split("/")[-1]

tree = "/".join(working.split("/")[0:-1]) + "/trees/" + name

if not path.exists(tree + "/.git"):
    raise Exception(".git file does not exist in tree! " + tree)

#print("clearing out any changes in tree")
#print "git --git-dir=" + tree + "/.git checkout ."
#system("git --git-dir=" + tree + "/.git checkout .")
print("updating tree")
print "git --git-dir=" + tree + "/.git pull"
system("git --git-dir=" + tree + "/.git pull")

print("calling meld")
print "meld " + tree + " " + working
system("meld " + tree + " " + working)


# TODO: add a verbose option to disable printing of commands that are run

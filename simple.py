""" A simple script that accepts command line arguments. """
import sys


def main():
    """ Simplest CLI function. """
    print("Reading cmd args")
    for arg in sys.argv[1:]:
        print(arg)
    print("Error check", file=sys.stderr)

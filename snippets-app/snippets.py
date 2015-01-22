#!/usr/bin/python -tt
import argparse
import sys

import logging  # Set the log output file, and the log level 

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet

def get(name):
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""

def main(): 
    """Main function"""     
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Subparser for the put command 
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet") 
    put_parser.add_argument("snippet", help="The snippet text")
    arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":     main()

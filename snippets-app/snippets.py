#! /usr/bin/env python
import argparse
import sys
import logging  # Set the log output file, and the log level 
import psycopg2

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets' user='action' host='localhost'")

def put(name, snippet):
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    try:
       command = "insert into snippets values (%s, %s)"
       cursor.execute(command, (name, snippet))
    except psycopg2.IntegrityError as e:
       connection.rollback()
       command = "update snippets set message=%s where keyword=%s"
       cursor.execute(command, (snippet, name))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


def get(name):
    logging.info("retrieving snippet - {!r}".format(name))
    #cursor = connection.cursor()
    command = "select message from snippets where keyword=%s"
    with connection, connection.cursor () as cursor:
         cursor.execute(command,(name,))
         row = cursor.fetchone()
        
         if not row:
            logging.debug("Keyword not found = {!r}".format(row))
         else:
            logging.debug("message = {!r}".format(row))
            print row
         return row
      
def show():
    command = "select keyword from snippets order by keyword"
    with connection, connection.cursor () as cursor:
         cursor.execute(command)
         keyword_tuple = cursor.fetchall()
    return keyword_tuple

def search_snippet(search_txt):
    search_txt = "%"+search_txt+"%"
    command = "select * from snippets where message like %s"
    with connection, connection.cursor () as cursor:
         cursor.execute(command,(search_txt,))
         result = cursor.fetchall()
         for item in result:print str(item[1]) + ','
          
def main(): 
    """Main function"""     
    logging.info("Constructing parser")
    logging.debug("Database connection established.")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Subparser for the put command 
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet") 
    put_parser.add_argument("snippet", help="The snippet text")
      
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the keyword") 
    
    show_parser = subparsers.add_parser("show", help="display the keyword of users")
   
    search_parser = subparsers.add_parser("search", help="search the description of snippets")
    search_parser.add_argument("search_txt", help="search text")
    
    arguments = parser.parse_args(sys.argv[1:])
    
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
       name, snippet = put(**arguments)
       print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
       name = get(**arguments)
    elif command =="show":
       for item in show():print item
    elif command =="search":
       snippet = search_snippet(**arguments)
      

if __name__ == "__main__":     main()

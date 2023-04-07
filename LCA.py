#!/usr/bin/env python3

if __name__ == "__main__":
    '''
    This is how we handle loading the input dataset, running your function, and printing the output
    '''
    from sys import argv
    from ast import literal_eval
    from lca.todo import find_LCAs 
    
    if len(argv) != 2:
        print("USAGE: %s <parent_dictionary>" % argv[0]); exit(1)
    parent = literal_eval(open(argv[1]).read())
    print(find_LCAs(parent))

#!/usr/bin/python3
    from sys import argv
    x = len(argv) - 1
    if x < 1:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument.".format(x))
    else:
        print("{} arguments.".format(x)
    for i in range (x):
        print("{}: {:s}".format(i + 1, argv[i + 1]))

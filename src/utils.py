from sys import *

def argsGetter():
    if len(argv) == 0:
        exit(84)
    if argv[1] == "-h":
        exit(0)
    if len(argv) != 10:
        exit(84)
    return list(map(float, argv[1:5])), list(map(float, argv[5:]))

def ArgsChecker(nTab, pTab):
    if any(map(lambda x: x < 0, nTab)):
        raise Exception("Number of fertilizer cannot be negative")
    if any(map(lambda x: x < 0, pTab)):
        raise Exception("Prices cannot be negative")

def resultPrint(tmp, pTab, a):
    print("Oat: {} units at ${:.0f}/unit".format(tmp[0], pTab[0]))
    print("Wheat: {} units at ${:.0f}/unit".format(tmp[1], pTab[1]))
    print("Corn: {} units at ${:.0f}/unit".format(tmp[2], pTab[2]))
    print("Barley: {} units at ${:.0f}/unit".format(tmp[3], pTab[3]))
    print("Soy: {} units at ${:.0f}/unit".format(tmp[4], pTab[4]))
    print()
    print("Total production value: ${:.2f}".format(a))
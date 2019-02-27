from inspect import currentframe, getframeinfo

def debug(*args):
    info = getframeinfo(currentframe().f_back)
    print("{}:{}, {}>>".format(info.filename, info.lineno, info.code_context[0]), *args)


x = 2
y = 3
debug(y)
z = 4

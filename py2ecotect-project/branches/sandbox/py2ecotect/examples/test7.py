import py2ecotect as p2e

for i in p2e.__dict__:
    if not i.startswith("__"):print i, p2e.__dict__[i]
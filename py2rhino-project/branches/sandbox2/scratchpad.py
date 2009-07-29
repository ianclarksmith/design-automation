import pythoncom

for i in sorted(pythoncom.Empty.__dict__.keys()):
    print i

print pythoncom.Empty
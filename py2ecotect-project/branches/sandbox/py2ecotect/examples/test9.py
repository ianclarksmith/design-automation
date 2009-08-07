import  _winreg
import os
"""
app = p2e.Application()

print app.get_registry("ECOTECT")
#"HKEY_CURRENT_USER\Software\Autodesk\Ecotect\2009"
"""
"""
#explorer = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\Autodesk\\Ecotect\\2009")
explorer = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Autodesk\\Ecotect\\2010\\AdLM")

try:
    i = 0
    while 1:
        name, value, type = _winreg.EnumValue(explorer, i)
        print repr(name),
        i += 1
except WindowsError:
    print

    
value, type = _winreg.QueryValueEx(explorer, "Type")
print value
"""
#suffix = "Ecotect 2009"
#print value.endswith(suffix)

print os.path.exists("C:\\Program Files\\Autodesk\\Ecotect 2009\\ecotect.exe")


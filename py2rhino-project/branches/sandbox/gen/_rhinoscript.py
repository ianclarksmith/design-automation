# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.98
# By python version 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)]
# From type library 'RhinoScript.tlb'
# On Thu Jul 16 01:34:42 2009
"""RhinoScript 4.0 Type Library"""
makepy_version = '0.4.98'
python_version = 0x20501f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{75B1E1B4-8CAA-43C3-975E-373504024FDB}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IRhinoScript(DispatchBaseClass):
	CLSID = IID('{DC7E0867-5922-4DCB-935F-585F81484030}')
	coclass_clsid = IID('{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

from win32com.client import CoClassBaseClass
class RhinoScript(CoClassBaseClass): # A CoClass
	CLSID = IID('{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRhinoScript,
	]
	default_interface = IRhinoScript

RecordMap = {
}

CLSIDToClassMap = {
	'{48B5D8DC-EDB1-45A9-981B-6C96169A0E7D}' : RhinoScript,
	'{DC7E0867-5922-4DCB-935F-585F81484030}' : IRhinoScript,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'IRhinoScript' : '{DC7E0867-5922-4DCB-935F-585F81484030}',
}



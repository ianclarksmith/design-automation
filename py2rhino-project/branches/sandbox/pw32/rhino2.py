# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.97
# By python version 2.5.4 (r254:67916, Apr 27 2009, 15:41:14) [MSC v.1310 32 bit (Intel)]
# From type library 'Rhino4.tlb'
# On Tue Jul 14 11:39:43 2009
"""Rhinoceros 4.0 Type Library"""
makepy_version = '0.4.97'
python_version = 0x20504f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{E58A8035-577A-42E2-A560-1D3564C1F6C3}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IRhino4(DispatchBaseClass):
	CLSID = IID('{42B5726E-3943-444F-A42A-C42C9B09A561}')
	coclass_clsid = IID('{9413EF92-F0D0-49FA-8480-26880F333990}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}

class IRhino4Application(DispatchBaseClass):
	CLSID = IID('{7BE12411-4563-4971-B30E-2D51F7542516}')
	coclass_clsid = IID('{6560E25E-9A63-453D-892E-8E7B05D27EE8}')

	def GetPlugInObject(self, plugin_uuid=defaultNamedNotOptArg, interface_uuid=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (13, 0), ((8, 0), (8, 0)),plugin_uuid
			, interface_uuid)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'GetPlugInObject', None, UnicodeToString=0)
		return ret

	def GetScriptObject(self):
		return self._ApplyTypes_(2, 1, (12, 0), (), u'GetScriptObject', None,)

	_prop_map_get_ = {
		"Visible": (1, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible" : ((1, LCID, 4, 0),()),
	}

class IRhino4Interface(DispatchBaseClass):
	CLSID = IID('{37C14ADD-3182-48EA-B5AD-7DD102FB4E7A}')
	coclass_clsid = IID('{D9D05B87-0D94-41BF-9FDF-8036704CBB71}')

	def GetPlugInObject(self, plugin_uuid=defaultNamedNotOptArg, interface_uuid=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (13, 0), ((8, 0), (8, 0)),plugin_uuid
			, interface_uuid)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'GetPlugInObject', None, UnicodeToString=0)
		return ret

	def GetScriptObject(self):
		return self._ApplyTypes_(2, 1, (12, 0), (), u'GetScriptObject', None,)

	_prop_map_get_ = {
		"Visible": (1, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible" : ((1, LCID, 4, 0),()),
	}

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Rhino4.Application'
class Application(CoClassBaseClass): # A CoClass
	CLSID = IID('{6560E25E-9A63-453D-892E-8E7B05D27EE8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRhino4Application,
	]
	default_interface = IRhino4Application

class Document(CoClassBaseClass): # A CoClass
	CLSID = IID('{9413EF92-F0D0-49FA-8480-26880F333990}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRhino4,
	]
	default_interface = IRhino4

# This CoClass is known by the name 'Rhino4.Interface'
class Interface(CoClassBaseClass): # A CoClass
	CLSID = IID('{D9D05B87-0D94-41BF-9FDF-8036704CBB71}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRhino4Interface,
	]
	default_interface = IRhino4Interface

RecordMap = {
}

CLSIDToClassMap = {
	'{D9D05B87-0D94-41BF-9FDF-8036704CBB71}' : Interface,
	'{6560E25E-9A63-453D-892E-8E7B05D27EE8}' : Application,
	'{42B5726E-3943-444F-A42A-C42C9B09A561}' : IRhino4,
	'{9413EF92-F0D0-49FA-8480-26880F333990}' : Document,
	'{37C14ADD-3182-48EA-B5AD-7DD102FB4E7A}' : IRhino4Interface,
	'{7BE12411-4563-4971-B30E-2D51F7542516}' : IRhino4Application,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'IRhino4Interface' : '{37C14ADD-3182-48EA-B5AD-7DD102FB4E7A}',
	'IRhino4' : '{42B5726E-3943-444F-A42A-C42C9B09A561}',
	'IRhino4Application' : '{7BE12411-4563-4971-B30E-2D51F7542516}',
}



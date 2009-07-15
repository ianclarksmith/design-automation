# -*- coding: mbcs -*-
typelib_path = 'C:\\Program Files\\Rhinoceros 4.0\\System\\Rhino4.tlb'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes.automation import VARIANT
from comtypes import BSTR
from comtypes import IUnknown
from comtypes import dispid
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring


class Document(CoClass):
    _reg_clsid_ = GUID('{9413EF92-F0D0-49FA-8480-26880F333990}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E58A8035-577A-42E2-A560-1D3564C1F6C3}', 1, 0)
class IRhino4(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{42B5726E-3943-444F-A42A-C42C9B09A561}')
    _idlflags_ = []
    _methods_ = []
Document._com_interfaces_ = [IRhino4]

class IRhino4Interface(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{37C14ADD-3182-48EA-B5AD-7DD102FB4E7A}')
    _idlflags_ = []
    _methods_ = []
IRhino4Interface._disp_methods_ = [
    DISPPROPERTY([dispid(1)], c_int, 'Visible'),
    DISPMETHOD([dispid(2)], VARIANT, 'GetScriptObject'),
    DISPMETHOD([dispid(3)], POINTER(IUnknown), 'GetPlugInObject',
               ( [], BSTR, 'plugin_uuid' ),
               ( [], BSTR, 'interface_uuid' )),
]
IRhino4._disp_methods_ = [
]
class Library(object):
    u'Rhinoceros 4.0 Type Library'
    name = u'Rhino4'
    _reg_typelib_ = ('{E58A8035-577A-42E2-A560-1D3564C1F6C3}', 1, 0)

class IRhino4Application(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{7BE12411-4563-4971-B30E-2D51F7542516}')
    _idlflags_ = []
    _methods_ = []
IRhino4Application._disp_methods_ = [
    DISPPROPERTY([dispid(1)], c_int, 'Visible'),
    DISPMETHOD([dispid(2)], VARIANT, 'GetScriptObject'),
    DISPMETHOD([dispid(3)], POINTER(IUnknown), 'GetPlugInObject',
               ( [], BSTR, 'plugin_uuid' ),
               ( [], BSTR, 'interface_uuid' )),
]
class Application(CoClass):
    _reg_clsid_ = GUID('{6560E25E-9A63-453D-892E-8E7B05D27EE8}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E58A8035-577A-42E2-A560-1D3564C1F6C3}', 1, 0)
Application._com_interfaces_ = [IRhino4Application]

class Interface(CoClass):
    _reg_clsid_ = GUID('{D9D05B87-0D94-41BF-9FDF-8036704CBB71}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{E58A8035-577A-42E2-A560-1D3564C1F6C3}', 1, 0)
Interface._com_interfaces_ = [IRhino4Interface]

__all__ = ['IRhino4Application', 'IRhino4', 'Application',
           'IRhino4Interface', 'Interface', 'Document']
from comtypes import _check_version; _check_version('482')

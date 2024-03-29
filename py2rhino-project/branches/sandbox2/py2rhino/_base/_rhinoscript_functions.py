# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
from _util import *
from _rhinoscript import IRhinoScript

class _RhinoscriptFunctions(IRhinoScript):

    # Class constructor
    def __init__(self, _rso):
        if _rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = _rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_alias(self, alias, macro):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (alias, macro)

        return self._ApplyTypes_(709, 1, (VT_VARIANT, 0), magic, u"AddAlias", None, *flattened)

    def add_search_path(self, folder, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (folder, index)

        return self._ApplyTypes_(511, 1, (VT_VARIANT, 0), magic, u"AddSearchPath", None, *flattened)

    def add_startup_script(self, script_file, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (script_file, index)

        return self._ApplyTypes_(714, 1, (VT_VARIANT, 0), magic, u"AddStartupScript", None, *flattened)

    def alias_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(706, 1, (VT_VARIANT, 0), magic, u"AliasCount", None, *flattened)

    def alias_macro(self, alias, macro):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (alias, macro)

        return self._ApplyTypes_(708, 1, (VT_VARIANT, 0), magic, u"AliasMacro", None, *flattened)

    def alias_names(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(707, 1, (VT_VARIANT, 0), magic, u"AliasNames", None, *flattened)

    def appearance_color(self, item, color):

        magic = ((VT_I2, 1), (VT_I4, 1))
        flattened = (item, color)

        return self._ApplyTypes_(335, 1, (VT_VARIANT, 0), magic, u"AppearanceColor", None, *flattened)

    def appearance_display(self, item, show):

        magic = ((VT_I2, 1), (VT_BOOL, 1))
        flattened = (item, show)

        return self._ApplyTypes_(752, 1, (VT_VARIANT, 0), magic, u"AppearanceDisplay", None, *flattened)

    def autosave_file(self, file):

        magic = ((VT_BSTR, 1),)
        flattened = (file,)

        return self._ApplyTypes_(428, 1, (VT_VARIANT, 0), magic, u"AutosaveFile", None, *flattened)

    def autosave_interval(self, minutes):

        magic = ((VT_I2, 1),)
        flattened = (minutes,)

        return self._ApplyTypes_(429, 1, (VT_VARIANT, 0), magic, u"AutosaveInterval", None, *flattened)

    def build_date(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(360, 1, (VT_VARIANT, 0), magic, u"BuildDate", None, *flattened)

    def clear_command_history(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(592, 1, (VT_VARIANT, 0), magic, u"ClearCommandHistory", None, *flattened)

    def command(self, command, echo):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (command, echo)

        return self._ApplyTypes_(1, 1, (VT_VARIANT, 0), magic, u"Command", None, *flattened)

    def command_history(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(591, 1, (VT_VARIANT, 0), magic, u"CommandHistory", None, *flattened)

    def default_renderer(self, renderer):

        magic = ((VT_BSTR, 1),)
        flattened = (renderer,)

        return self._ApplyTypes_(316, 1, (VT_VARIANT, 0), magic, u"DefaultRenderer", None, *flattened)

    def delete_alias(self, alias):

        magic = ((VT_BSTR, 1),)
        flattened = (alias,)

        return self._ApplyTypes_(710, 1, (VT_VARIANT, 0), magic, u"DeleteAlias", None, *flattened)

    def delete_search_path(self, folder):

        magic = ((VT_BSTR, 1),)
        flattened = (folder,)

        return self._ApplyTypes_(512, 1, (VT_VARIANT, 0), magic, u"DeleteSearchPath", None, *flattened)

    def delete_startup_script(self, script_file):

        magic = ((VT_BSTR, 1),)
        flattened = (script_file,)

        return self._ApplyTypes_(715, 1, (VT_VARIANT, 0), magic, u"DeleteStartupScript", None, *flattened)

    def display_ole_alerts(self, display):

        magic = ((VT_BOOL, 1),)
        flattened = (display,)

        return self._ApplyTypes_(896, 1, (VT_VARIANT, 0), magic, u"DisplayOleAlerts", None, *flattened)

    def edge_analysis_color(self, color):

        magic = ((VT_I4, 1),)
        flattened = (color,)

        return self._ApplyTypes_(449, 1, (VT_VARIANT, 0), magic, u"EdgeAnalysisColor", None, *flattened)

    def edge_analysis_mode(self, mode):

        magic = ((VT_I2, 1),)
        flattened = (mode,)

        return self._ApplyTypes_(448, 1, (VT_VARIANT, 0), magic, u"EdgeAnalysisMode", None, *flattened)

    def enable_autosave(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(430, 1, (VT_VARIANT, 0), magic, u"EnableAutosave", None, *flattened)

    def enable_history_recording(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(735, 1, (VT_VARIANT, 0), magic, u"EnableHistoryRecording", None, *flattened)

    def exe_folder(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(21, 1, (VT_VARIANT, 0), magic, u"ExeFolder", None, *flattened)

    def exit(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(537, 1, (VT_VARIANT, 0), magic, u"Exit", None, *flattened)

    def find_file(self, filename):

        magic = ((VT_BSTR, 1),)
        flattened = (filename,)

        return self._ApplyTypes_(81, 1, (VT_VARIANT, 0), magic, u"FindFile", None, *flattened)

    def get_plug_in_object(self, plug_in):

        magic = ((VT_BSTR, 1),)
        flattened = (plug_in,)

        return self._ApplyTypes_(636, 1, (VT_VARIANT, 0), magic, u"GetPlugInObject", None, *flattened)

    def help(self, topic):

        magic = ((VT_I2, 1),)
        flattened = (topic,)

        return self._ApplyTypes_(22, 1, (VT_VARIANT, 0), magic, u"Help", None, *flattened)

    def in_command(self, ignore_runners):

        magic = ((VT_BOOL, 1),)
        flattened = (ignore_runners,)

        return self._ApplyTypes_(596, 1, (VT_VARIANT, 0), magic, u"InCommand", None, *flattened)

    def install_folder(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(23, 1, (VT_VARIANT, 0), magic, u"InstallFolder", None, *flattened)

    def is_alias(self, alias):

        magic = ((VT_BSTR, 1),)
        flattened = (alias,)

        return self._ApplyTypes_(711, 1, (VT_VARIANT, 0), magic, u"IsAlias", None, *flattened)

    def is_command(self, command_name):

        magic = ((VT_BSTR, 1),)
        flattened = (command_name,)

        return self._ApplyTypes_(530, 1, (VT_VARIANT, 0), magic, u"IsCommand", None, *flattened)

    def last_command_name(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(594, 1, (VT_VARIANT, 0), magic, u"LastCommandName", None, *flattened)

    def last_command_result(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(292, 1, (VT_VARIANT, 0), magic, u"LastCommandResult", None, *flattened)

    def last_loaded_script_file(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(373, 1, (VT_VARIANT, 0), magic, u"LastLoadedScriptFile", None, *flattened)

    def locale_i_d(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(450, 1, (VT_VARIANT, 0), magic, u"LocaleID", None, *flattened)

    def ortho(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(345, 1, (VT_VARIANT, 0), magic, u"Ortho", None, *flattened)

    def osnap(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(347, 1, (VT_VARIANT, 0), magic, u"Osnap", None, *flattened)

    def osnap_dialog(self, visible):

        magic = ((VT_BOOL, 1),)
        flattened = (visible,)

        return self._ApplyTypes_(349, 1, (VT_VARIANT, 0), magic, u"OsnapDialog", None, *flattened)

    def osnap_mode(self, mode):

        magic = ((VT_I2, 1),)
        flattened = (mode,)

        return self._ApplyTypes_(343, 1, (VT_VARIANT, 0), magic, u"OsnapMode", None, *flattened)

    def planar(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(346, 1, (VT_VARIANT, 0), magic, u"Planar", None, *flattened)

    def plug_ins(self, types, status):

        magic = ((VT_I2, 1), (VT_I2, 1))
        flattened = (types, status)

        return self._ApplyTypes_(315, 1, (VT_VARIANT, 0), magic, u"PlugIns", None, *flattened)

    def print_(self, message):

        magic = ((VT_BSTR, 1),)
        flattened = (message,)

        return self._ApplyTypes_(2, 1, (VT_VARIANT, 0), magic, u"Print", None, *flattened)

    def print_ex(self, message):

        magic = ((VT_BSTR, 1),)
        flattened = (message,)

        return self._ApplyTypes_(370, 1, (VT_VARIANT, 0), magic, u"PrintEx", None, *flattened)

    def project_osnaps(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(348, 1, (VT_VARIANT, 0), magic, u"ProjectOsnaps", None, *flattened)

    def prompt(self, prompt):

        magic = ((VT_BSTR, 1),)
        flattened = (prompt,)

        return self._ApplyTypes_(24, 1, (VT_VARIANT, 0), magic, u"Prompt", None, *flattened)

    def registry_key(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(25, 1, (VT_VARIANT, 0), magic, u"RegistryKey", None, *flattened)

    def screen_size(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(553, 1, (VT_VARIANT, 0), magic, u"ScreenSize", None, *flattened)

    def sdk_version(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(359, 1, (VT_VARIANT, 0), magic, u"SdkVersion", None, *flattened)

    def search_path_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(509, 1, (VT_VARIANT, 0), magic, u"SearchPathCount", None, *flattened)

    def search_path_list(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(510, 1, (VT_VARIANT, 0), magic, u"SearchPathList", None, *flattened)

    def send_keystrokes(self, keys, add_return):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (keys, add_return)

        return self._ApplyTypes_(496, 1, (VT_VARIANT, 0), magic, u"SendKeystrokes", None, *flattened)

    def snap(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(344, 1, (VT_VARIANT, 0), magic, u"Snap", None, *flattened)

    def startup_script_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(712, 1, (VT_VARIANT, 0), magic, u"StartupScriptCount", None, *flattened)

    def startup_script_list(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(713, 1, (VT_VARIANT, 0), magic, u"StartupScriptList", None, *flattened)

    def status_bar_distance(self, distance):

        magic = ((VT_R8, 1),)
        flattened = (distance,)

        return self._ApplyTypes_(26, 1, (VT_VARIANT, 0), magic, u"StatusBarDistance", None, *flattened)

    def status_bar_message(self, message):

        magic = ((VT_BSTR, 1),)
        flattened = (message,)

        return self._ApplyTypes_(28, 1, (VT_VARIANT, 0), magic, u"StatusBarMessage", None, *flattened)

    def status_bar_number(self, number):

        magic = ((VT_R8, 1),)
        flattened = (number,)

        return self._ApplyTypes_(312, 1, (VT_VARIANT, 0), magic, u"StatusBarNumber", None, *flattened)

    def status_bar_point(self, point):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(point),)

        return self._ApplyTypes_(27, 1, (VT_VARIANT, 0), magic, u"StatusBarPoint", None, *flattened)

    def template_file(self, filename):

        magic = ((VT_BSTR, 1),)
        flattened = (filename,)

        return self._ApplyTypes_(529, 1, (VT_VARIANT, 0), magic, u"TemplateFile", None, *flattened)

    def template_folder(self, folder):

        magic = ((VT_BSTR, 1),)
        flattened = (folder,)

        return self._ApplyTypes_(528, 1, (VT_VARIANT, 0), magic, u"TemplateFolder", None, *flattened)

    def window_handle(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(29, 1, (VT_VARIANT, 0), magic, u"WindowHandle", None, *flattened)

    def working_folder(self, enable):

        magic = ((VT_BOOL, 1),)
        flattened = (enable,)

        return self._ApplyTypes_(439, 1, (VT_VARIANT, 0), magic, u"WorkingFolder", None, *flattened)

    def block_container_count(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(411, 1, (VT_VARIANT, 0), magic, u"BlockContainerCount", None, *flattened)

    def block_containers(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(412, 1, (VT_VARIANT, 0), magic, u"BlockContainers", None, *flattened)

    def block_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(397, 1, (VT_VARIANT, 0), magic, u"BlockCount", None, *flattened)

    def block_description(self, block, text):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (block, text)

        return self._ApplyTypes_(400, 1, (VT_VARIANT, 0), magic, u"BlockDescription", None, *flattened)

    def block_instance_count(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(404, 1, (VT_VARIANT, 0), magic, u"BlockInstanceCount", None, *flattened)

    def block_instance_insert_point(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(413, 1, (VT_VARIANT, 0), magic, u"BlockInstanceInsertPoint", None, *flattened)

    def block_instance_name(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(571, 1, (VT_VARIANT, 0), magic, u"BlockInstanceName", None, *flattened)

    def block_instance_xform(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(415, 1, (VT_VARIANT, 0), magic, u"BlockInstanceXform", None, *flattened)

    def block_instances(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(414, 1, (VT_VARIANT, 0), magic, u"BlockInstances", None, *flattened)

    def block_names(self, sort):

        magic = ((VT_BOOL, 1),)
        flattened = (sort,)

        return self._ApplyTypes_(396, 1, (VT_VARIANT, 0), magic, u"BlockNames", None, *flattened)

    def block_object_count(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(416, 1, (VT_VARIANT, 0), magic, u"BlockObjectCount", None, *flattened)

    def block_objects(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(417, 1, (VT_VARIANT, 0), magic, u"BlockObjects", None, *flattened)

    def block_path(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(408, 1, (VT_VARIANT, 0), magic, u"BlockPath", None, *flattened)

    def block_u_r_l(self, block, u_r_l):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (block, u_r_l)

        return self._ApplyTypes_(402, 1, (VT_VARIANT, 0), magic, u"BlockURL", None, *flattened)

    def block_u_r_l_tag(self, block, u_r_l):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (block, u_r_l)

        return self._ApplyTypes_(403, 1, (VT_VARIANT, 0), magic, u"BlockURLTag", None, *flattened)

    def delete_block(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(418, 1, (VT_VARIANT, 0), magic, u"DeleteBlock", None, *flattened)

    def explode_block_instance(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(419, 1, (VT_VARIANT, 0), magic, u"ExplodeBlockInstance", None, *flattened)

    def insert_block(self, name, point, scale, angle, normal):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (name, flatten_params(point), flatten_params(scale), angle, flatten_params(normal))

        return self._ApplyTypes_(633, 1, (VT_VARIANT, 0), magic, u"InsertBlock", None, *flattened)

    def insert_block_2(self, name, xform):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (name, flatten_params(xform))

        return self._ApplyTypes_(633, 1, (VT_VARIANT, 0), magic, u"InsertBlock", None, *flattened)

    def is_block(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(398, 1, (VT_VARIANT, 0), magic, u"IsBlock", None, *flattened)

    def is_block_embedded(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(405, 1, (VT_VARIANT, 0), magic, u"IsBlockEmbedded", None, *flattened)

    def is_block_in_use(self, block, where):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (block, where)

        return self._ApplyTypes_(406, 1, (VT_VARIANT, 0), magic, u"IsBlockInUse", None, *flattened)

    def is_block_instance(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(420, 1, (VT_VARIANT, 0), magic, u"IsBlockInstance", None, *flattened)

    def is_block_reference(self, block):

        magic = ((VT_BSTR, 1),)
        flattened = (block,)

        return self._ApplyTypes_(407, 1, (VT_VARIANT, 0), magic, u"IsBlockReference", None, *flattened)

    def rename_block(self, old_block, new_block):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (old_block, new_block)

        return self._ApplyTypes_(399, 1, (VT_VARIANT, 0), magic, u"RenameBlock", None, *flattened)

    def add_arc(self, plane, radius, angle):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), radius, angle)

        return self._ApplyTypes_(651, 1, (VT_VARIANT, 0), magic, u"AddArc", None, *flattened)

    def add_arc_3_pt(self, start, end, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(start), flatten_params(end), flatten_params(point))

        return self._ApplyTypes_(82, 1, (VT_VARIANT, 0), magic, u"AddArc3Pt", None, *flattened)

    def add_circle(self, plane, radius):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), radius)

        return self._ApplyTypes_(83, 1, (VT_VARIANT, 0), magic, u"AddCircle", None, *flattened)

    def add_circle_3_pt(self, first, second, third):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(first), flatten_params(second), flatten_params(third))

        return self._ApplyTypes_(84, 1, (VT_VARIANT, 0), magic, u"AddCircle3Pt", None, *flattened)

    def add_curve(self, points, degree):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (flatten_params(points), degree)

        return self._ApplyTypes_(77, 1, (VT_VARIANT, 0), magic, u"AddCurve", None, *flattened)

    def add_ellipse(self, plane, x_radius, y_radius):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), x_radius, y_radius)

        return self._ApplyTypes_(679, 1, (VT_VARIANT, 0), magic, u"AddEllipse", None, *flattened)

    def add_ellipse_3_pt(self, center, second, third):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(center), flatten_params(second), flatten_params(third))

        return self._ApplyTypes_(680, 1, (VT_VARIANT, 0), magic, u"AddEllipse3Pt", None, *flattened)

    def add_fillet_curve(self, curve_0, curve_1, radius, point_0, point_1):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (curve_0, curve_1, radius, flatten_params(point_0), flatten_params(point_1))

        return self._ApplyTypes_(574, 1, (VT_VARIANT, 0), magic, u"AddFilletCurve", None, *flattened)

    def add_interp_crv_on_srf(self, object, points):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(points))

        return self._ApplyTypes_(513, 1, (VT_VARIANT, 0), magic, u"AddInterpCrvOnSrf", None, *flattened)

    def add_interp_crv_on_srf_u_v(self, object, points):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(points))

        return self._ApplyTypes_(641, 1, (VT_VARIANT, 0), magic, u"AddInterpCrvOnSrfUV", None, *flattened)

    def add_interp_curve(self, points, degree, knot_style, start_tan, end_tan):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_I2, 1), (VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(points), degree, knot_style, flatten_params(start_tan), flatten_params(end_tan))

        return self._ApplyTypes_(268, 1, (VT_VARIANT, 0), magic, u"AddInterpCurve", None, *flattened)

    def add_interp_curve_ex(self, points, degree, knot_style, sharp, start_tangent, end_tangent):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(points), degree, knot_style, sharp, flatten_params(start_tangent), flatten_params(end_tangent))

        return self._ApplyTypes_(520, 1, (VT_VARIANT, 0), magic, u"AddInterpCurveEx", None, *flattened)

    def add_line(self, start, end):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(start), flatten_params(end))

        return self._ApplyTypes_(70, 1, (VT_VARIANT, 0), magic, u"AddLine", None, *flattened)

    def add_nurbs_curve(self, points, knots, degree, weights):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(points), flatten_params(knots), degree, flatten_params(weights))

        return self._ApplyTypes_(309, 1, (VT_VARIANT, 0), magic, u"AddNurbsCurve", None, *flattened)

    def add_polyline(self, points):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(points),)

        return self._ApplyTypes_(85, 1, (VT_VARIANT, 0), magic, u"AddPolyline", None, *flattened)

    def add_sub_crv(self, object, param_0, param_1):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (object, param_0, param_1)

        return self._ApplyTypes_(681, 1, (VT_VARIANT, 0), magic, u"AddSubCrv", None, *flattened)

    def arc_angle(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(86, 1, (VT_VARIANT, 0), magic, u"ArcAngle", None, *flattened)

    def arc_center_point(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(87, 1, (VT_VARIANT, 0), magic, u"ArcCenterPoint", None, *flattened)

    def arc_mid_point(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(88, 1, (VT_VARIANT, 0), magic, u"ArcMidPoint", None, *flattened)

    def arc_radius(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(89, 1, (VT_VARIANT, 0), magic, u"ArcRadius", None, *flattened)

    def circle_center_point(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(90, 1, (VT_VARIANT, 0), magic, u"CircleCenterPoint", None, *flattened)

    def circle_circumference(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(91, 1, (VT_VARIANT, 0), magic, u"CircleCircumference", None, *flattened)

    def circle_radius(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(92, 1, (VT_VARIANT, 0), magic, u"CircleRadius", None, *flattened)

    def close_curve(self, object, tolerance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, tolerance)

        return self._ApplyTypes_(440, 1, (VT_VARIANT, 0), magic, u"CloseCurve", None, *flattened)

    def convert_curve_to_polyline(self, object, angle_tolerance, tolerance, delete_input):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, angle_tolerance, tolerance, delete_input)

        return self._ApplyTypes_(377, 1, (VT_VARIANT, 0), magic, u"ConvertCurveToPolyline", None, *flattened)

    def curve_arc_length_point(self, object, length, from_start):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, length, from_start)

        return self._ApplyTypes_(658, 1, (VT_VARIANT, 0), magic, u"CurveArcLengthPoint", None, *flattened)

    def curve_area(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(643, 1, (VT_VARIANT, 0), magic, u"CurveArea", None, *flattened)

    def curve_area_centroid(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(677, 1, (VT_VARIANT, 0), magic, u"CurveAreaCentroid", None, *flattened)

    def curve_arrows(self, object, style):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, style)

        return self._ApplyTypes_(578, 1, (VT_VARIANT, 0), magic, u"CurveArrows", None, *flattened)

    def curve_boolean_difference(self, curve_a, curve_b):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (curve_a, curve_b)

        return self._ApplyTypes_(811, 1, (VT_VARIANT, 0), magic, u"CurveBooleanDifference", None, *flattened)

    def curve_boolean_intersection(self, curve_a, curve_b):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (curve_a, curve_b)

        return self._ApplyTypes_(810, 1, (VT_VARIANT, 0), magic, u"CurveBooleanIntersection", None, *flattened)

    def curve_boolean_union(self, curves):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(curves),)

        return self._ApplyTypes_(809, 1, (VT_VARIANT, 0), magic, u"CurveBooleanUnion", None, *flattened)

    def curve_brep_intersect(self, curve, brep, tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1))
        flattened = (curve, brep, tolerance)

        return self._ApplyTypes_(545, 1, (VT_VARIANT, 0), magic, u"CurveBrepIntersect", None, *flattened)

    def curve_closest_object(self, curve, objects):

        magic = ((VT_BSTR, 1), (VT_VARIANT, 1))
        flattened = (curve, flatten_params(objects))

        return self._ApplyTypes_(870, 1, (VT_VARIANT, 0), magic, u"CurveClosestObject", None, *flattened)

    def curve_closest_point(self, object, point, index):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (object, flatten_params(point), index)

        return self._ApplyTypes_(93, 1, (VT_VARIANT, 0), magic, u"CurveClosestPoint", None, *flattened)

    def curve_contour_points(self, object, start_point, end_point, interval):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (object, flatten_params(start_point), flatten_params(end_point), interval)

        return self._ApplyTypes_(748, 1, (VT_VARIANT, 0), magic, u"CurveContourPoints", None, *flattened)

    def curve_curvature(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, parameter)

        return self._ApplyTypes_(379, 1, (VT_VARIANT, 0), magic, u"CurveCurvature", None, *flattened)

    def curve_curve_intersection(self, object_1, object_2, tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1))
        flattened = (object_1, object_2, tolerance)

        return self._ApplyTypes_(423, 1, (VT_VARIANT, 0), magic, u"CurveCurveIntersection", None, *flattened)

    def curve_degree(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(94, 1, (VT_VARIANT, 0), magic, u"CurveDegree", None, *flattened)

    def curve_deviation(self, curve_a, curve_b):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (curve_a, curve_b)

        return self._ApplyTypes_(687, 1, (VT_VARIANT, 0), magic, u"CurveDeviation", None, *flattened)

    def curve_dim(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(381, 1, (VT_VARIANT, 0), magic, u"CurveDim", None, *flattened)

    def curve_directions_match(self, curve_1, curve_2):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (curve_1, curve_2)

        return self._ApplyTypes_(543, 1, (VT_VARIANT, 0), magic, u"CurveDirectionsMatch", None, *flattened)

    def curve_discontinuity(self, object, style):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, style)

        return self._ApplyTypes_(579, 1, (VT_VARIANT, 0), magic, u"CurveDiscontinuity", None, *flattened)

    def curve_domain(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(95, 1, (VT_VARIANT, 0), magic, u"CurveDomain", None, *flattened)

    def curve_edit_points(self, object, return_parameters, index):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_I2, 1))
        flattened = (object, return_parameters, index)

        return self._ApplyTypes_(442, 1, (VT_VARIANT, 0), magic, u"CurveEditPoints", None, *flattened)

    def curve_end_point(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(96, 1, (VT_VARIANT, 0), magic, u"CurveEndPoint", None, *flattened)

    def curve_evaluate(self, object, parameter, derivative):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1))
        flattened = (object, parameter, derivative)

        return self._ApplyTypes_(489, 1, (VT_VARIANT, 0), magic, u"CurveEvaluate", None, *flattened)

    def curve_fillet_points(self, curve_0, curve_1, radius, base_point_0, base_point_1):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (curve_0, curve_1, radius, flatten_params(base_point_0), flatten_params(base_point_1))

        return self._ApplyTypes_(572, 1, (VT_VARIANT, 0), magic, u"CurveFilletPoints", None, *flattened)

    def curve_frame(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, parameter)

        return self._ApplyTypes_(675, 1, (VT_VARIANT, 0), magic, u"CurveFrame", None, *flattened)

    def curve_knot_count(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(310, 1, (VT_VARIANT, 0), magic, u"CurveKnotCount", None, *flattened)

    def curve_knots(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(311, 1, (VT_VARIANT, 0), magic, u"CurveKnots", None, *flattened)

    def curve_length(self, object, index, sub_domain):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_ARRAY + VT_I2, 1))
        flattened = (object, index, flatten_params(sub_domain))

        return self._ApplyTypes_(97, 1, (VT_VARIANT, 0), magic, u"CurveLength", None, *flattened)

    def curve_mid_point(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(577, 1, (VT_VARIANT, 0), magic, u"CurveMidPoint", None, *flattened)

    def curve_normal(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(521, 1, (VT_VARIANT, 0), magic, u"CurveNormal", None, *flattened)

    def curve_perp_frame(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, parameter)

        return self._ApplyTypes_(676, 1, (VT_VARIANT, 0), magic, u"CurvePerpFrame", None, *flattened)

    def curve_plane(self, curve):

        magic = ((VT_BSTR, 1),)
        flattened = (curve,)

        return self._ApplyTypes_(609, 1, (VT_VARIANT, 0), magic, u"CurvePlane", None, *flattened)

    def curve_point_count(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(98, 1, (VT_VARIANT, 0), magic, u"CurvePointCount", None, *flattened)

    def curve_points(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(308, 1, (VT_VARIANT, 0), magic, u"CurvePoints", None, *flattened)

    def curve_radius(self, object, point, index):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (object, flatten_params(point), index)

        return self._ApplyTypes_(80, 1, (VT_VARIANT, 0), magic, u"CurveRadius", None, *flattened)

    def curve_seam(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, parameter)

        return self._ApplyTypes_(527, 1, (VT_VARIANT, 0), magic, u"CurveSeam", None, *flattened)

    def curve_start_point(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(99, 1, (VT_VARIANT, 0), magic, u"CurveStartPoint", None, *flattened)

    def curve_surface_intersection(self, curve, surface, tolerance, angle_tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (curve, surface, tolerance, angle_tolerance)

        return self._ApplyTypes_(424, 1, (VT_VARIANT, 0), magic, u"CurveSurfaceIntersection", None, *flattened)

    def curve_tangent(self, object, parameter, index):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1))
        flattened = (object, parameter, index)

        return self._ApplyTypes_(363, 1, (VT_VARIANT, 0), magic, u"CurveTangent", None, *flattened)

    def curve_weights(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(314, 1, (VT_VARIANT, 0), magic, u"CurveWeights", None, *flattened)

    def divide_curve(self, object, segments, create, points):

        magic = ((VT_BSTR, 1), (VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (object, segments, create, points)

        return self._ApplyTypes_(78, 1, (VT_VARIANT, 0), magic, u"DivideCurve", None, *flattened)

    def divide_curve_equidistant(self, object, distance, create, points):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (object, distance, create, points)

        return self._ApplyTypes_(913, 1, (VT_VARIANT, 0), magic, u"DivideCurveEquidistant", None, *flattened)

    def divide_curve_length(self, object, length, create, points):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (object, length, create, points)

        return self._ApplyTypes_(374, 1, (VT_VARIANT, 0), magic, u"DivideCurveLength", None, *flattened)

    def ellipse_center_point(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(524, 1, (VT_VARIANT, 0), magic, u"EllipseCenterPoint", None, *flattened)

    def ellipse_quad_points(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(525, 1, (VT_VARIANT, 0), magic, u"EllipseQuadPoints", None, *flattened)

    def evaluate_curve(self, object, parameter, index):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1))
        flattened = (object, parameter, index)

        return self._ApplyTypes_(100, 1, (VT_VARIANT, 0), magic, u"EvaluateCurve", None, *flattened)

    def explode_curves(self, objects, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), delete)

        return self._ApplyTypes_(446, 1, (VT_VARIANT, 0), magic, u"ExplodeCurves", None, *flattened)

    def extend_curve(self, object, type, side, objects):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_VARIANT, 1))
        flattened = (object, type, side, flatten_params(objects))

        return self._ApplyTypes_(438, 1, (VT_VARIANT, 0), magic, u"ExtendCurve", None, *flattened)

    def extend_curve_length(self, object, type, side, length):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_R8, 1))
        flattened = (object, type, side, length)

        return self._ApplyTypes_(436, 1, (VT_VARIANT, 0), magic, u"ExtendCurveLength", None, *flattened)

    def extend_curve_point(self, object, side, point):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, side, flatten_params(point))

        return self._ApplyTypes_(437, 1, (VT_VARIANT, 0), magic, u"ExtendCurvePoint", None, *flattened)

    def fair_curve(self, object, tolerance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, tolerance)

        return self._ApplyTypes_(599, 1, (VT_VARIANT, 0), magic, u"FairCurve", None, *flattened)

    def fit_curve(self, object, degree, tolerance, angle_tolerance):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (object, degree, tolerance, angle_tolerance)

        return self._ApplyTypes_(813, 1, (VT_VARIANT, 0), magic, u"FitCurve", None, *flattened)

    def insert_curve_knot(self, object, parameter, symmetrical):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, parameter, symmetrical)

        return self._ApplyTypes_(515, 1, (VT_VARIANT, 0), magic, u"InsertCurveKnot", None, *flattened)

    def is_arc(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(101, 1, (VT_VARIANT, 0), magic, u"IsArc", None, *flattened)

    def is_circle(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(102, 1, (VT_VARIANT, 0), magic, u"IsCircle", None, *flattened)

    def is_curve(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(103, 1, (VT_VARIANT, 0), magic, u"IsCurve", None, *flattened)

    def is_curve_closable(self, object, tolerance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, tolerance)

        return self._ApplyTypes_(441, 1, (VT_VARIANT, 0), magic, u"IsCurveClosable", None, *flattened)

    def is_curve_closed(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(104, 1, (VT_VARIANT, 0), magic, u"IsCurveClosed", None, *flattened)

    def is_curve_in_plane(self, object, plane):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(plane))

        return self._ApplyTypes_(483, 1, (VT_VARIANT, 0), magic, u"IsCurveInPlane", None, *flattened)

    def is_curve_linear(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(105, 1, (VT_VARIANT, 0), magic, u"IsCurveLinear", None, *flattened)

    def is_curve_periodic(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(106, 1, (VT_VARIANT, 0), magic, u"IsCurvePeriodic", None, *flattened)

    def is_curve_planar(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(107, 1, (VT_VARIANT, 0), magic, u"IsCurvePlanar", None, *flattened)

    def is_curve_rational(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(380, 1, (VT_VARIANT, 0), magic, u"IsCurveRational", None, *flattened)

    def is_ellipse(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(523, 1, (VT_VARIANT, 0), magic, u"IsEllipse", None, *flattened)

    def is_line(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(108, 1, (VT_VARIANT, 0), magic, u"IsLine", None, *flattened)

    def is_point_on_curve(self, object, point, index):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_I2, 1), (VT_I2, 1))
        flattened = (object, flatten_params(point), index)

        return self._ApplyTypes_(318, 1, (VT_VARIANT, 0), magic, u"IsPointOnCurve", None, *flattened)

    def is_poly_curve(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(368, 1, (VT_VARIANT, 0), magic, u"IsPolyCurve", None, *flattened)

    def is_polyline(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(110, 1, (VT_VARIANT, 0), magic, u"IsPolyline", None, *flattened)

    def join_curves(self, objects, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), delete)

        return self._ApplyTypes_(111, 1, (VT_VARIANT, 0), magic, u"JoinCurves", None, *flattened)

    def line_fit_from_points(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(726, 1, (VT_VARIANT, 0), magic, u"LineFitFromPoints", None, *flattened)

    def make_curve_non_periodic(self, object, delete):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, delete)

        return self._ApplyTypes_(925, 1, (VT_VARIANT, 0), magic, u"MakeCurveNonPeriodic", None, *flattened)

    def make_curve_periodic(self, object, delete):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, delete)

        return self._ApplyTypes_(444, 1, (VT_VARIANT, 0), magic, u"MakeCurvePeriodic", None, *flattened)

    def mesh_polyline(self, polyline):

        magic = ((VT_BSTR, 1),)
        flattened = (polyline,)

        return self._ApplyTypes_(546, 1, (VT_VARIANT, 0), magic, u"MeshPolyline", None, *flattened)

    def offset_curve(self, object, direction, distance, normal, style):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (object, flatten_params(direction), distance, flatten_params(normal), style)

        return self._ApplyTypes_(634, 1, (VT_VARIANT, 0), magic, u"OffsetCurve", None, *flattened)

    def offset_curve_on_surface(self, curve, surface, distance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1))
        flattened = (curve, surface, distance)

        return self._ApplyTypes_(906, 1, (VT_VARIANT, 0), magic, u"OffsetCurveOnSurface", None, *flattened)

    def offset_curve_on_surface_2(self, curve, surface, parameter):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (curve, surface, flatten_params(parameter))

        return self._ApplyTypes_(906, 1, (VT_VARIANT, 0), magic, u"OffsetCurveOnSurface", None, *flattened)

    def planar_closed_curve_containment(self, curve_1, curve_2, plane, tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (curve_1, curve_2, flatten_params(plane), tolerance)

        return self._ApplyTypes_(480, 1, (VT_VARIANT, 0), magic, u"PlanarClosedCurveContainment", None, *flattened)

    def planar_curve_collision(self, curve_1, curve_2, plane, tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (curve_1, curve_2, flatten_params(plane), tolerance)

        return self._ApplyTypes_(481, 1, (VT_VARIANT, 0), magic, u"PlanarCurveCollision", None, *flattened)

    def point_in_planar_closed_curve(self, point, curve, plane, tolerance):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(point), curve, flatten_params(plane), tolerance)

        return self._ApplyTypes_(482, 1, (VT_VARIANT, 0), magic, u"PointInPlanarClosedCurve", None, *flattened)

    def poly_curve_count(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(369, 1, (VT_VARIANT, 0), magic, u"PolyCurveCount", None, *flattened)

    def polyline_vertices(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(112, 1, (VT_VARIANT, 0), magic, u"PolylineVertices", None, *flattened)

    def project_curve_to_mesh(self, curves, meshes, direction):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(curves), flatten_params(meshes), flatten_params(direction))

        return self._ApplyTypes_(911, 1, (VT_VARIANT, 0), magic, u"ProjectCurveToMesh", None, *flattened)

    def project_curve_to_surface(self, curves, surfaces, direction):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(curves), flatten_params(surfaces), flatten_params(direction))

        return self._ApplyTypes_(891, 1, (VT_VARIANT, 0), magic, u"ProjectCurveToSurface", None, *flattened)

    def rebuild_curve(self, object, degree, point_count):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1))
        flattened = (object, degree, point_count)

        return self._ApplyTypes_(814, 1, (VT_VARIANT, 0), magic, u"RebuildCurve", None, *flattened)

    def remove_curve_knot(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, parameter)

        return self._ApplyTypes_(916, 1, (VT_VARIANT, 0), magic, u"RemoveCurveKnot", None, *flattened)

    def reverse_curve(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(542, 1, (VT_VARIANT, 0), magic, u"ReverseCurve", None, *flattened)

    def simplify_curve(self, object, flags):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, flags)

        return self._ApplyTypes_(573, 1, (VT_VARIANT, 0), magic, u"SimplifyCurve", None, *flattened)

    def split_curve(self, object, parameters, delete):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(parameters), delete)

        return self._ApplyTypes_(504, 1, (VT_VARIANT, 0), magic, u"SplitCurve", None, *flattened)

    def trim_curve(self, object, interval, delete):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(interval), delete)

        return self._ApplyTypes_(505, 1, (VT_VARIANT, 0), magic, u"TrimCurve", None, *flattened)

    def add_dim_style(self, dim_style):

        magic = ((VT_BSTR, 1),)
        flattened = (dim_style,)

        return self._ApplyTypes_(455, 1, (VT_VARIANT, 0), magic, u"AddDimStyle", None, *flattened)

    def add_leader(self, points, view, text):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(points), view, text)

        return self._ApplyTypes_(321, 1, (VT_VARIANT, 0), magic, u"AddLeader", None, *flattened)

    def current_dim_style(self, dim_style):

        magic = ((VT_BSTR, 1),)
        flattened = (dim_style,)

        return self._ApplyTypes_(453, 1, (VT_VARIANT, 0), magic, u"CurrentDimStyle", None, *flattened)

    def delete_dim_style(self, dim_style):

        magic = ((VT_BSTR, 1),)
        flattened = (dim_style,)

        return self._ApplyTypes_(456, 1, (VT_VARIANT, 0), magic, u"DeleteDimStyle", None, *flattened)

    def dim_scale(self, scale):

        magic = ((VT_R8, 1),)
        flattened = (scale,)

        return self._ApplyTypes_(460, 1, (VT_VARIANT, 0), magic, u"DimScale", None, *flattened)

    def dim_style_angle_precision(self, dim_style, precision):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (dim_style, precision)

        return self._ApplyTypes_(464, 1, (VT_VARIANT, 0), magic, u"DimStyleAnglePrecision", None, *flattened)

    def dim_style_arrow_size(self, dim_style, size):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (dim_style, size)

        return self._ApplyTypes_(468, 1, (VT_VARIANT, 0), magic, u"DimStyleArrowSize", None, *flattened)

    def dim_style_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(451, 1, (VT_VARIANT, 0), magic, u"DimStyleCount", None, *flattened)

    def dim_style_extension(self, dim_style, extension):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (dim_style, extension)

        return self._ApplyTypes_(466, 1, (VT_VARIANT, 0), magic, u"DimStyleExtension", None, *flattened)

    def dim_style_font(self, dim_style, font):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (dim_style, font)

        return self._ApplyTypes_(462, 1, (VT_VARIANT, 0), magic, u"DimStyleFont", None, *flattened)

    def dim_style_leader_arrow_size(self, dim_style, size):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (dim_style, size)

        return self._ApplyTypes_(704, 1, (VT_VARIANT, 0), magic, u"DimStyleLeaderArrowSize", None, *flattened)

    def dim_style_linear_precision(self, dim_style, precision):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (dim_style, precision)

        return self._ApplyTypes_(463, 1, (VT_VARIANT, 0), magic, u"DimStyleLinearPrecision", None, *flattened)

    def dim_style_names(self, sort):

        magic = ((VT_BOOL, 1),)
        flattened = (sort,)

        return self._ApplyTypes_(452, 1, (VT_VARIANT, 0), magic, u"DimStyleNames", None, *flattened)

    def dim_style_number_format(self, dim_style, format):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (dim_style, format)

        return self._ApplyTypes_(459, 1, (VT_VARIANT, 0), magic, u"DimStyleNumberFormat", None, *flattened)

    def dim_style_offset(self, dim_style, offset):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (dim_style, offset)

        return self._ApplyTypes_(467, 1, (VT_VARIANT, 0), magic, u"DimStyleOffset", None, *flattened)

    def dim_style_text_alignment(self, dim_style, alignment):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (dim_style, alignment)

        return self._ApplyTypes_(461, 1, (VT_VARIANT, 0), magic, u"DimStyleTextAlignment", None, *flattened)

    def dim_style_text_gap(self, dim_style, gap):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (dim_style, gap)

        return self._ApplyTypes_(741, 1, (VT_VARIANT, 0), magic, u"DimStyleTextGap", None, *flattened)

    def dim_style_text_height(self, dim_style, height):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (dim_style, height)

        return self._ApplyTypes_(465, 1, (VT_VARIANT, 0), magic, u"DimStyleTextHeight", None, *flattened)

    def dimension_style(self, object, style):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, style)

        return self._ApplyTypes_(703, 1, (VT_VARIANT, 0), magic, u"DimensionStyle", None, *flattened)

    def dimension_text(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(469, 1, (VT_VARIANT, 0), magic, u"DimensionText", None, *flattened)

    def dimension_user_text(self, object, user_text):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, user_text)

        return self._ApplyTypes_(563, 1, (VT_VARIANT, 0), magic, u"DimensionUserText", None, *flattened)

    def dimension_value(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(568, 1, (VT_VARIANT, 0), magic, u"DimensionValue", None, *flattened)

    def is_aligned_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(566, 1, (VT_VARIANT, 0), magic, u"IsAlignedDimension", None, *flattened)

    def is_angular_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(338, 1, (VT_VARIANT, 0), magic, u"IsAngularDimension", None, *flattened)

    def is_diameter_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(565, 1, (VT_VARIANT, 0), magic, u"IsDiameterDimension", None, *flattened)

    def is_dim_style(self, dim_style):

        magic = ((VT_BSTR, 1),)
        flattened = (dim_style,)

        return self._ApplyTypes_(454, 1, (VT_VARIANT, 0), magic, u"IsDimStyle", None, *flattened)

    def is_dim_style_reference(self, dim_style):

        magic = ((VT_BSTR, 1),)
        flattened = (dim_style,)

        return self._ApplyTypes_(457, 1, (VT_VARIANT, 0), magic, u"IsDimStyleReference", None, *flattened)

    def is_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(564, 1, (VT_VARIANT, 0), magic, u"IsDimension", None, *flattened)

    def is_leader(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(337, 1, (VT_VARIANT, 0), magic, u"IsLeader", None, *flattened)

    def is_linear_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(339, 1, (VT_VARIANT, 0), magic, u"IsLinearDimension", None, *flattened)

    def is_ordinate_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(659, 1, (VT_VARIANT, 0), magic, u"IsOrdinateDimension", None, *flattened)

    def is_radial_dimension(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(340, 1, (VT_VARIANT, 0), magic, u"IsRadialDimension", None, *flattened)

    def leader_text(self, object, text):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, text)

        return self._ApplyTypes_(895, 1, (VT_VARIANT, 0), magic, u"LeaderText", None, *flattened)

    def rename_dim_style(self, old_style, new_style):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (old_style, new_style)

        return self._ApplyTypes_(458, 1, (VT_VARIANT, 0), magic, u"RenameDimStyle", None, *flattened)

    def create_preview_image(self, file, view, size, flags, wireframe):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_ARRAY + VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (file, view, flatten_params(size), flags, wireframe)

        return self._ApplyTypes_(388, 1, (VT_VARIANT, 0), magic, u"CreatePreviewImage", None, *flattened)

    def document_modified(self, modified):

        magic = ((VT_BOOL, 1),)
        flattened = (modified,)

        return self._ApplyTypes_(323, 1, (VT_VARIANT, 0), magic, u"DocumentModified", None, *flattened)

    def document_name(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(113, 1, (VT_VARIANT, 0), magic, u"DocumentName", None, *flattened)

    def document_path(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(301, 1, (VT_VARIANT, 0), magic, u"DocumentPath", None, *flattened)

    def document_u_r_l(self, u_r_l):

        magic = ((VT_BSTR, 1),)
        flattened = (u_r_l,)

        return self._ApplyTypes_(275, 1, (VT_VARIANT, 0), magic, u"DocumentURL", None, *flattened)

    def enable_redraw(self, select):

        magic = ((VT_BOOL, 1),)
        flattened = (select,)

        return self._ApplyTypes_(317, 1, (VT_VARIANT, 0), magic, u"EnableRedraw", None, *flattened)

    def extract_preview_image(self, file_name, model_name):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (file_name, model_name)

        return self._ApplyTypes_(389, 1, (VT_VARIANT, 0), magic, u"ExtractPreviewImage", None, *flattened)

    def is_document_modified(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(273, 1, (VT_VARIANT, 0), magic, u"IsDocumentModified", None, *flattened)

    def notes(self, notes):

        magic = ((VT_BSTR, 1),)
        flattened = (notes,)

        return self._ApplyTypes_(274, 1, (VT_VARIANT, 0), magic, u"Notes", None, *flattened)

    def read_file_version(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(737, 1, (VT_VARIANT, 0), magic, u"ReadFileVersion", None, *flattened)

    def redraw(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(114, 1, (VT_VARIANT, 0), magic, u"Redraw", None, *flattened)

    def render_antialias(self, style):

        magic = ((VT_I2, 1),)
        flattened = (style,)

        return self._ApplyTypes_(333, 1, (VT_VARIANT, 0), magic, u"RenderAntialias", None, *flattened)

    def render_color(self, item, color):

        magic = ((VT_I2, 1), (VT_I4, 1))
        flattened = (item, color)

        return self._ApplyTypes_(331, 1, (VT_VARIANT, 0), magic, u"RenderColor", None, *flattened)

    def render_mesh_density(self, density):

        magic = ((VT_R8, 1),)
        flattened = (density,)

        return self._ApplyTypes_(844, 1, (VT_VARIANT, 0), magic, u"RenderMeshDensity", None, *flattened)

    def render_mesh_max_angle(self, angle):

        magic = ((VT_R8, 1),)
        flattened = (angle,)

        return self._ApplyTypes_(845, 1, (VT_VARIANT, 0), magic, u"RenderMeshMaxAngle", None, *flattened)

    def render_mesh_max_aspect_ratio(self, ratio):

        magic = ((VT_R8, 1),)
        flattened = (ratio,)

        return self._ApplyTypes_(846, 1, (VT_VARIANT, 0), magic, u"RenderMeshMaxAspectRatio", None, *flattened)

    def render_mesh_max_dist_edge_to_srf(self, distance):

        magic = ((VT_R8, 1),)
        flattened = (distance,)

        return self._ApplyTypes_(849, 1, (VT_VARIANT, 0), magic, u"RenderMeshMaxDistEdgeToSrf", None, *flattened)

    def render_mesh_max_edge_length(self, length):

        magic = ((VT_R8, 1),)
        flattened = (length,)

        return self._ApplyTypes_(848, 1, (VT_VARIANT, 0), magic, u"RenderMeshMaxEdgeLength", None, *flattened)

    def render_mesh_min_edge_length(self, length):

        magic = ((VT_R8, 1),)
        flattened = (length,)

        return self._ApplyTypes_(847, 1, (VT_VARIANT, 0), magic, u"RenderMeshMinEdgeLength", None, *flattened)

    def render_mesh_min_initial_grid_quads(self, quads):

        magic = ((VT_I2, 1),)
        flattened = (quads,)

        return self._ApplyTypes_(850, 1, (VT_VARIANT, 0), magic, u"RenderMeshMinInitialGridQuads", None, *flattened)

    def render_mesh_quality(self, quality):

        magic = ((VT_I2, 1),)
        flattened = (quality,)

        return self._ApplyTypes_(843, 1, (VT_VARIANT, 0), magic, u"RenderMeshQuality", None, *flattened)

    def render_mesh_settings(self, settings):

        magic = ((VT_I2, 1),)
        flattened = (settings,)

        return self._ApplyTypes_(851, 1, (VT_VARIANT, 0), magic, u"RenderMeshSettings", None, *flattened)

    def render_resolution(self, resolution):

        magic = ((VT_ARRAY + VT_I2, 1),)
        flattened = (flatten_params(resolution),)

        return self._ApplyTypes_(332, 1, (VT_VARIANT, 0), magic, u"RenderResolution", None, *flattened)

    def render_settings(self, settings):

        magic = ((VT_I2, 1),)
        flattened = (settings,)

        return self._ApplyTypes_(334, 1, (VT_VARIANT, 0), magic, u"RenderSettings", None, *flattened)

    def unit_absolute_tolerance(self, abs_tol):

        magic = ((VT_R8, 1),)
        flattened = (abs_tol,)

        return self._ApplyTypes_(324, 1, (VT_VARIANT, 0), magic, u"UnitAbsoluteTolerance", None, *flattened)

    def unit_angle_tolerance(self, angle_tol):

        magic = ((VT_R8, 1),)
        flattened = (angle_tol,)

        return self._ApplyTypes_(325, 1, (VT_VARIANT, 0), magic, u"UnitAngleTolerance", None, *flattened)

    def unit_custom_unit_system(self, units, scale, name):

        magic = ((VT_R8, 1), (VT_BOOL, 1), (VT_BSTR, 1))
        flattened = (units, scale, name)

        return self._ApplyTypes_(326, 1, (VT_VARIANT, 0), magic, u"UnitCustomUnitSystem", None, *flattened)

    def unit_distance_display_mode(self, mode):

        magic = ((VT_I2, 1),)
        flattened = (mode,)

        return self._ApplyTypes_(327, 1, (VT_VARIANT, 0), magic, u"UnitDistanceDisplayMode", None, *flattened)

    def unit_distance_display_precision(self, precision):

        magic = ((VT_I2, 1),)
        flattened = (precision,)

        return self._ApplyTypes_(328, 1, (VT_VARIANT, 0), magic, u"UnitDistanceDisplayPrecision", None, *flattened)

    def unit_relative_tolerance(self, rel_tol):

        magic = ((VT_R8, 1),)
        flattened = (rel_tol,)

        return self._ApplyTypes_(329, 1, (VT_VARIANT, 0), magic, u"UnitRelativeTolerance", None, *flattened)

    def unit_scale(self, to_system, from_system):

        magic = ((VT_I2, 1), (VT_I2, 1))
        flattened = (to_system, from_system)

        return self._ApplyTypes_(868, 1, (VT_VARIANT, 0), magic, u"UnitScale", None, *flattened)

    def unit_system(self, system, scale):

        magic = ((VT_I2, 1), (VT_BOOL, 1))
        flattened = (system, scale)

        return self._ApplyTypes_(330, 1, (VT_VARIANT, 0), magic, u"UnitSystem", None, *flattened)

    def unit_system_name(self, capitalize, singular, abbreviate):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (capitalize, singular, abbreviate)

        return self._ApplyTypes_(492, 1, (VT_VARIANT, 0), magic, u"UnitSystemName", None, *flattened)

    def add_clipping_plane(self, plane, d_u, d_v, views):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(plane), d_u, d_v, flatten_params(views))

        return self._ApplyTypes_(904, 1, (VT_VARIANT, 0), magic, u"AddClippingPlane", None, *flattened)

    def add_point(self, point):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(point),)

        return self._ApplyTypes_(68, 1, (VT_VARIANT, 0), magic, u"AddPoint", None, *flattened)

    def add_point_cloud(self, points):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(points),)

        return self._ApplyTypes_(69, 1, (VT_VARIANT, 0), magic, u"AddPointCloud", None, *flattened)

    def add_points(self, points):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(points),)

        return self._ApplyTypes_(526, 1, (VT_VARIANT, 0), magic, u"AddPoints", None, *flattened)

    def add_text(self, text, point, height, font, style):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_I2, 1))
        flattened = (text, flatten_params(point), height, font, style)

        return self._ApplyTypes_(76, 1, (VT_VARIANT, 0), magic, u"AddText", None, *flattened)

    def add_text_2(self, text, plane, height, font, style):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_I2, 1))
        flattened = (text, flatten_params(plane), height, font, style)

        return self._ApplyTypes_(76, 1, (VT_VARIANT, 0), magic, u"AddText", None, *flattened)

    def add_text_dot(self, test, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (test, flatten_params(point))

        return self._ApplyTypes_(320, 1, (VT_VARIANT, 0), magic, u"AddTextDot", None, *flattened)

    def bounding_box(self, objects, view, world_coords):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), view, world_coords)

        return self._ApplyTypes_(117, 1, (VT_VARIANT, 0), magic, u"BoundingBox", None, *flattened)

    def compare_geometry(self, object_1, object_2):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object_1, object_2)

        return self._ApplyTypes_(598, 1, (VT_VARIANT, 0), magic, u"CompareGeometry", None, *flattened)

    def is_clipping_plane(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(905, 1, (VT_VARIANT, 0), magic, u"IsClippingPlane", None, *flattened)

    def is_point(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(120, 1, (VT_VARIANT, 0), magic, u"IsPoint", None, *flattened)

    def is_point_cloud(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(121, 1, (VT_VARIANT, 0), magic, u"IsPointCloud", None, *flattened)

    def is_text(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(122, 1, (VT_VARIANT, 0), magic, u"IsText", None, *flattened)

    def is_text_dot(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(336, 1, (VT_VARIANT, 0), magic, u"IsTextDot", None, *flattened)

    def point_cloud_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(128, 1, (VT_VARIANT, 0), magic, u"PointCloudCount", None, *flattened)

    def point_cloud_points(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(129, 1, (VT_VARIANT, 0), magic, u"PointCloudPoints", None, *flattened)

    def point_coordinates(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(130, 1, (VT_VARIANT, 0), magic, u"PointCoordinates", None, *flattened)

    def text_dot_point(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(422, 1, (VT_VARIANT, 0), magic, u"TextDotPoint", None, *flattened)

    def text_dot_text(self, object, text):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, text)

        return self._ApplyTypes_(421, 1, (VT_VARIANT, 0), magic, u"TextDotText", None, *flattened)

    def text_object_font(self, object, font):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, font)

        return self._ApplyTypes_(474, 1, (VT_VARIANT, 0), magic, u"TextObjectFont", None, *flattened)

    def text_object_height(self, object, height):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, height)

        return self._ApplyTypes_(473, 1, (VT_VARIANT, 0), magic, u"TextObjectHeight", None, *flattened)

    def text_object_plane(self, object, plane):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(plane))

        return self._ApplyTypes_(476, 1, (VT_VARIANT, 0), magic, u"TextObjectPlane", None, *flattened)

    def text_object_point(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(471, 1, (VT_VARIANT, 0), magic, u"TextObjectPoint", None, *flattened)

    def text_object_style(self, object, style):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, style)

        return self._ApplyTypes_(475, 1, (VT_VARIANT, 0), magic, u"TextObjectStyle", None, *flattened)

    def text_object_text(self, object, text):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, text)

        return self._ApplyTypes_(472, 1, (VT_VARIANT, 0), magic, u"TextObjectText", None, *flattened)

    def add_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(133, 1, (VT_VARIANT, 0), magic, u"AddGroup", None, *flattened)

    def add_object_to_group(self, object, group):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, group)

        return self._ApplyTypes_(134, 1, (VT_VARIANT, 0), magic, u"AddObjectToGroup", None, *flattened)

    def add_objects_to_group(self, objects, group):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(objects), group)

        return self._ApplyTypes_(135, 1, (VT_VARIANT, 0), magic, u"AddObjectsToGroup", None, *flattened)

    def delete_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(136, 1, (VT_VARIANT, 0), magic, u"DeleteGroup", None, *flattened)

    def group_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(137, 1, (VT_VARIANT, 0), magic, u"GroupCount", None, *flattened)

    def group_names(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(138, 1, (VT_VARIANT, 0), magic, u"GroupNames", None, *flattened)

    def hide_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(871, 1, (VT_VARIANT, 0), magic, u"HideGroup", None, *flattened)

    def is_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(139, 1, (VT_VARIANT, 0), magic, u"IsGroup", None, *flattened)

    def is_group_empty(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(140, 1, (VT_VARIANT, 0), magic, u"IsGroupEmpty", None, *flattened)

    def lock_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(873, 1, (VT_VARIANT, 0), magic, u"LockGroup", None, *flattened)

    def remove_object_from_all_groups(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(141, 1, (VT_VARIANT, 0), magic, u"RemoveObjectFromAllGroups", None, *flattened)

    def remove_object_from_group(self, object, group):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, group)

        return self._ApplyTypes_(142, 1, (VT_VARIANT, 0), magic, u"RemoveObjectFromGroup", None, *flattened)

    def remove_object_from_top_group(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(143, 1, (VT_VARIANT, 0), magic, u"RemoveObjectFromTopGroup", None, *flattened)

    def remove_objects_from_group(self, objects, group):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(objects), group)

        return self._ApplyTypes_(144, 1, (VT_VARIANT, 0), magic, u"RemoveObjectsFromGroup", None, *flattened)

    def rename_group(self, old_group, new_group):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (old_group, new_group)

        return self._ApplyTypes_(145, 1, (VT_VARIANT, 0), magic, u"RenameGroup", None, *flattened)

    def show_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(872, 1, (VT_VARIANT, 0), magic, u"ShowGroup", None, *flattened)

    def unlock_group(self, group):

        magic = ((VT_BSTR, 1),)
        flattened = (group,)

        return self._ApplyTypes_(874, 1, (VT_VARIANT, 0), magic, u"UnlockGroup", None, *flattened)

    def add_hatch(self, curve, hatch, scale, rotation):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (curve, hatch, scale, rotation)

        return self._ApplyTypes_(835, 1, (VT_VARIANT, 0), magic, u"AddHatch", None, *flattened)

    def add_hatch_patterns(self, file_name, replace):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (file_name, replace)

        return self._ApplyTypes_(826, 1, (VT_VARIANT, 0), magic, u"AddHatchPatterns", None, *flattened)

    def add_hatches(self, curves, hatch, scale, rotation):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(curves), hatch, scale, rotation)

        return self._ApplyTypes_(836, 1, (VT_VARIANT, 0), magic, u"AddHatches", None, *flattened)

    def current_hatch_pattern(self, hatch):

        magic = ((VT_BSTR, 1),)
        flattened = (hatch,)

        return self._ApplyTypes_(827, 1, (VT_VARIANT, 0), magic, u"CurrentHatchPattern", None, *flattened)

    def explode_hatch(self, hatch, delete):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (hatch, delete)

        return self._ApplyTypes_(841, 1, (VT_VARIANT, 0), magic, u"ExplodeHatch", None, *flattened)

    def hatch_pattern(self, object, hatch):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, hatch)

        return self._ApplyTypes_(837, 1, (VT_VARIANT, 0), magic, u"HatchPattern", None, *flattened)

    def hatch_pattern_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(828, 1, (VT_VARIANT, 0), magic, u"HatchPatternCount", None, *flattened)

    def hatch_pattern_description(self, hatch):

        magic = ((VT_BSTR, 1),)
        flattened = (hatch,)

        return self._ApplyTypes_(829, 1, (VT_VARIANT, 0), magic, u"HatchPatternDescription", None, *flattened)

    def hatch_pattern_fill_type(self, hatch):

        magic = ((VT_BSTR, 1),)
        flattened = (hatch,)

        return self._ApplyTypes_(831, 1, (VT_VARIANT, 0), magic, u"HatchPatternFillType", None, *flattened)

    def hatch_pattern_names(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(830, 1, (VT_VARIANT, 0), magic, u"HatchPatternNames", None, *flattened)

    def hatch_rotation(self, object, rotation):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, rotation)

        return self._ApplyTypes_(839, 1, (VT_VARIANT, 0), magic, u"HatchRotation", None, *flattened)

    def hatch_scale(self, object, scale):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, scale)

        return self._ApplyTypes_(838, 1, (VT_VARIANT, 0), magic, u"HatchScale", None, *flattened)

    def is_hatch(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(840, 1, (VT_VARIANT, 0), magic, u"IsHatch", None, *flattened)

    def is_hatch_pattern(self, hatch):

        magic = ((VT_BSTR, 1),)
        flattened = (hatch,)

        return self._ApplyTypes_(832, 1, (VT_VARIANT, 0), magic, u"IsHatchPattern", None, *flattened)

    def is_hatch_pattern_current(self, hatch):

        magic = ((VT_BSTR, 1),)
        flattened = (hatch,)

        return self._ApplyTypes_(833, 1, (VT_VARIANT, 0), magic, u"IsHatchPatternCurrent", None, *flattened)

    def is_hatch_pattern_reference(self, hatch):

        magic = ((VT_BSTR, 1),)
        flattened = (hatch,)

        return self._ApplyTypes_(834, 1, (VT_VARIANT, 0), magic, u"IsHatchPatternReference", None, *flattened)

    def add_layer(self, layer, color, visible, locked, parent):

        magic = ((VT_BSTR, 1), (VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BSTR, 1))
        flattened = (layer, color, visible, locked, parent)

        return self._ApplyTypes_(3, 1, (VT_VARIANT, 0), magic, u"AddLayer", None, *flattened)

    def current_layer(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(5, 1, (VT_VARIANT, 0), magic, u"CurrentLayer", None, *flattened)

    def delete_layer(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(4, 1, (VT_VARIANT, 0), magic, u"DeleteLayer", None, *flattened)

    def expand_layer(self, layer, expand):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (layer, expand)

        return self._ApplyTypes_(690, 1, (VT_VARIANT, 0), magic, u"ExpandLayer", None, *flattened)

    def is_layer(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(6, 1, (VT_VARIANT, 0), magic, u"IsLayer", None, *flattened)

    def is_layer_changeable(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(18, 1, (VT_VARIANT, 0), magic, u"IsLayerChangeable", None, *flattened)

    def is_layer_child_of(self, layer, test):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (layer, test)

        return self._ApplyTypes_(692, 1, (VT_VARIANT, 0), magic, u"IsLayerChildOf", None, *flattened)

    def is_layer_current(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(313, 1, (VT_VARIANT, 0), magic, u"IsLayerCurrent", None, *flattened)

    def is_layer_empty(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(7, 1, (VT_VARIANT, 0), magic, u"IsLayerEmpty", None, *flattened)

    def is_layer_expanded(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(689, 1, (VT_VARIANT, 0), magic, u"IsLayerExpanded", None, *flattened)

    def is_layer_locked(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(8, 1, (VT_VARIANT, 0), magic, u"IsLayerLocked", None, *flattened)

    def is_layer_on(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(9, 1, (VT_VARIANT, 0), magic, u"IsLayerOn", None, *flattened)

    def is_layer_parent_of(self, layer, test):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (layer, test)

        return self._ApplyTypes_(693, 1, (VT_VARIANT, 0), magic, u"IsLayerParentOf", None, *flattened)

    def is_layer_reference(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(10, 1, (VT_VARIANT, 0), magic, u"IsLayerReference", None, *flattened)

    def is_layer_selectable(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(19, 1, (VT_VARIANT, 0), magic, u"IsLayerSelectable", None, *flattened)

    def is_layer_visible(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(20, 1, (VT_VARIANT, 0), magic, u"IsLayerVisible", None, *flattened)

    def layer_child_count(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(694, 1, (VT_VARIANT, 0), magic, u"LayerChildCount", None, *flattened)

    def layer_children(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(691, 1, (VT_VARIANT, 0), magic, u"LayerChildren", None, *flattened)

    def layer_color(self, layer, color):

        magic = ((VT_BSTR, 1), (VT_I4, 1))
        flattened = (layer, color)

        return self._ApplyTypes_(11, 1, (VT_VARIANT, 0), magic, u"LayerColor", None, *flattened)

    def layer_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(12, 1, (VT_VARIANT, 0), magic, u"LayerCount", None, *flattened)

    def layer_linetype(self, layer, linetype):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (layer, linetype)

        return self._ApplyTypes_(602, 1, (VT_VARIANT, 0), magic, u"LayerLinetype", None, *flattened)

    def layer_locked(self, layer, visible):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (layer, visible)

        return self._ApplyTypes_(601, 1, (VT_VARIANT, 0), magic, u"LayerLocked", None, *flattened)

    def layer_material_index(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(13, 1, (VT_VARIANT, 0), magic, u"LayerMaterialIndex", None, *flattened)

    def layer_mode(self, layer, mode):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (layer, mode)

        return self._ApplyTypes_(14, 1, (VT_VARIANT, 0), magic, u"LayerMode", None, *flattened)

    def layer_names(self, sort):

        magic = ((VT_BOOL, 1),)
        flattened = (sort,)

        return self._ApplyTypes_(15, 1, (VT_VARIANT, 0), magic, u"LayerNames", None, *flattened)

    def layer_order(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(17, 1, (VT_VARIANT, 0), magic, u"LayerOrder", None, *flattened)

    def layer_print_color(self, layer, color):

        magic = ((VT_BSTR, 1), (VT_I4, 1))
        flattened = (layer, color)

        return self._ApplyTypes_(603, 1, (VT_VARIANT, 0), magic, u"LayerPrintColor", None, *flattened)

    def layer_print_width(self, layer, width):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (layer, width)

        return self._ApplyTypes_(604, 1, (VT_VARIANT, 0), magic, u"LayerPrintWidth", None, *flattened)

    def layer_visible(self, layer, visible):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (layer, visible)

        return self._ApplyTypes_(600, 1, (VT_VARIANT, 0), magic, u"LayerVisible", None, *flattened)

    def parent_layer(self, layer, parent):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (layer, parent)

        return self._ApplyTypes_(688, 1, (VT_VARIANT, 0), magic, u"ParentLayer", None, *flattened)

    def purge_layer(self, layer):

        magic = ((VT_BSTR, 1),)
        flattened = (layer,)

        return self._ApplyTypes_(291, 1, (VT_VARIANT, 0), magic, u"PurgeLayer", None, *flattened)

    def rename_layer(self, old_name, new_name):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (old_name, new_name)

        return self._ApplyTypes_(16, 1, (VT_VARIANT, 0), magic, u"RenameLayer", None, *flattened)

    def add_directional_light(self, start_point, end_point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(start_point), flatten_params(end_point))

        return self._ApplyTypes_(153, 1, (VT_VARIANT, 0), magic, u"AddDirectionalLight", None, *flattened)

    def add_linear_light(self, start_point, end_point, width):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(start_point), flatten_params(end_point), width)

        return self._ApplyTypes_(154, 1, (VT_VARIANT, 0), magic, u"AddLinearLight", None, *flattened)

    def add_point_light(self, point):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(point),)

        return self._ApplyTypes_(155, 1, (VT_VARIANT, 0), magic, u"AddPointLight", None, *flattened)

    def add_rectangular_light(self, origin, width, height):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(origin), flatten_params(width), flatten_params(height))

        return self._ApplyTypes_(156, 1, (VT_VARIANT, 0), magic, u"AddRectangularLight", None, *flattened)

    def add_spot_light(self, origin, radius, apex):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(origin), radius, flatten_params(apex))

        return self._ApplyTypes_(157, 1, (VT_VARIANT, 0), magic, u"AddSpotLight", None, *flattened)

    def enable_light(self, object, enable):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, enable)

        return self._ApplyTypes_(158, 1, (VT_VARIANT, 0), magic, u"EnableLight", None, *flattened)

    def is_directional_light(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(159, 1, (VT_VARIANT, 0), magic, u"IsDirectionalLight", None, *flattened)

    def is_light(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(160, 1, (VT_VARIANT, 0), magic, u"IsLight", None, *flattened)

    def is_light_enabled(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(161, 1, (VT_VARIANT, 0), magic, u"IsLightEnabled", None, *flattened)

    def is_light_reference(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(162, 1, (VT_VARIANT, 0), magic, u"IsLightReference", None, *flattened)

    def is_linear_light(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(163, 1, (VT_VARIANT, 0), magic, u"IsLinearLight", None, *flattened)

    def is_point_light(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(164, 1, (VT_VARIANT, 0), magic, u"IsPointLight", None, *flattened)

    def is_rectangular_light(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(165, 1, (VT_VARIANT, 0), magic, u"IsRectangularLight", None, *flattened)

    def is_spot_light(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(166, 1, (VT_VARIANT, 0), magic, u"IsSpotLight", None, *flattened)

    def light_color(self, object, color):

        magic = ((VT_BSTR, 1), (VT_I4, 1))
        flattened = (object, color)

        return self._ApplyTypes_(167, 1, (VT_VARIANT, 0), magic, u"LightColor", None, *flattened)

    def light_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(168, 1, (VT_VARIANT, 0), magic, u"LightCount", None, *flattened)

    def light_direction(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(direction))

        return self._ApplyTypes_(491, 1, (VT_VARIANT, 0), magic, u"LightDirection", None, *flattened)

    def light_location(self, object, location):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(location))

        return self._ApplyTypes_(490, 1, (VT_VARIANT, 0), magic, u"LightLocation", None, *flattened)

    def light_name(self, object, name):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, name)

        return self._ApplyTypes_(169, 1, (VT_VARIANT, 0), magic, u"LightName", None, *flattened)

    def light_objects(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(170, 1, (VT_VARIANT, 0), magic, u"LightObjects", None, *flattened)

    def rectangular_light_plane(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(776, 1, (VT_VARIANT, 0), magic, u"RectangularLightPlane", None, *flattened)

    def spot_light_hardness(self, object, hardness):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, hardness)

        return self._ApplyTypes_(171, 1, (VT_VARIANT, 0), magic, u"SpotLightHardness", None, *flattened)

    def spot_light_radius(self, object, radius):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, radius)

        return self._ApplyTypes_(584, 1, (VT_VARIANT, 0), magic, u"SpotLightRadius", None, *flattened)

    def spot_light_shadow_intensity(self, object, intensity):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, intensity)

        return self._ApplyTypes_(172, 1, (VT_VARIANT, 0), magic, u"SpotLightShadowIntensity", None, *flattened)

    def distance_to_plane(self, plane, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane), flatten_params(point))

        return self._ApplyTypes_(628, 1, (VT_VARIANT, 0), magic, u"DistanceToPlane", None, *flattened)

    def evaluate_plane(self, plane, parameter):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane), flatten_params(parameter))

        return self._ApplyTypes_(751, 1, (VT_VARIANT, 0), magic, u"EvaluatePlane", None, *flattened)

    def intersect_planes(self, plane_1, plane_2, plane_3):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane_1), flatten_params(plane_2), flatten_params(plane_3))

        return self._ApplyTypes_(745, 1, (VT_VARIANT, 0), magic, u"IntersectPlanes", None, *flattened)

    def line_closest_point(self, line, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), flatten_params(point))

        return self._ApplyTypes_(899, 1, (VT_VARIANT, 0), magic, u"LineClosestPoint", None, *flattened)

    def line_is_farther_than(self, line, distance, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), distance, flatten_params(point))

        return self._ApplyTypes_(902, 1, (VT_VARIANT, 0), magic, u"LineIsFartherThan", None, *flattened)

    def line_is_farther_than_2(self, line, distance, line_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), distance, flatten_params(line_2))

        return self._ApplyTypes_(902, 1, (VT_VARIANT, 0), magic, u"LineIsFartherThan", None, *flattened)

    def line_line_intersection(self, line_a, line_b, planar):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(line_a), flatten_params(line_b), planar)

        return self._ApplyTypes_(736, 1, (VT_VARIANT, 0), magic, u"LineLineIntersection", None, *flattened)

    def line_max_distance_to(self, line, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), flatten_params(point))

        return self._ApplyTypes_(901, 1, (VT_VARIANT, 0), magic, u"LineMaxDistanceTo", None, *flattened)

    def line_max_distance_to_2(self, line, line_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), flatten_params(line_2))

        return self._ApplyTypes_(901, 1, (VT_VARIANT, 0), magic, u"LineMaxDistanceTo", None, *flattened)

    def line_min_distance_to(self, line, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), flatten_params(point))

        return self._ApplyTypes_(900, 1, (VT_VARIANT, 0), magic, u"LineMinDistanceTo", None, *flattened)

    def line_min_distance_to_2(self, line, line_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), flatten_params(line_2))

        return self._ApplyTypes_(900, 1, (VT_VARIANT, 0), magic, u"LineMinDistanceTo", None, *flattened)

    def line_plane(self, line):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(line),)

        return self._ApplyTypes_(898, 1, (VT_VARIANT, 0), magic, u"LinePlane", None, *flattened)

    def line_plane_intersection(self, line, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(line), flatten_params(point))

        return self._ApplyTypes_(743, 1, (VT_VARIANT, 0), magic, u"LinePlaneIntersection", None, *flattened)

    def line_transform(self, line, xform):

        #magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        #flattened = (flatten_params(line), flatten_params(xform))
        
        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(line), xform)
        
        return self._ApplyTypes_(897, 1, (VT_VARIANT, 0), magic, u"LineTransform", None, *flattened)

    def move_plane(self, plane, origin):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane), flatten_params(origin))

        return self._ApplyTypes_(631, 1, (VT_VARIANT, 0), magic, u"MovePlane", None, *flattened)

    def plane_closest_point(self, plane, point, return_point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(plane), flatten_params(point), return_point)

        return self._ApplyTypes_(629, 1, (VT_VARIANT, 0), magic, u"PlaneClosestPoint", None, *flattened)

    def plane_equation(self, plane):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(plane),)

        return self._ApplyTypes_(642, 1, (VT_VARIANT, 0), magic, u"PlaneEquation", None, *flattened)

    def plane_fit_from_points(self, points):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(points),)

        return self._ApplyTypes_(725, 1, (VT_VARIANT, 0), magic, u"PlaneFitFromPoints", None, *flattened)

    def plane_from_frame(self, origin, xaxis, yaxis):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(origin), flatten_params(xaxis), flatten_params(yaxis))

        return self._ApplyTypes_(627, 1, (VT_VARIANT, 0), magic, u"PlaneFromFrame", None, *flattened)

    def plane_from_normal(self, origin, normal):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(origin), flatten_params(normal))

        return self._ApplyTypes_(626, 1, (VT_VARIANT, 0), magic, u"PlaneFromNormal", None, *flattened)

    def plane_from_points(self, origin, point_x, point_y):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(origin), flatten_params(point_x), flatten_params(point_y))

        return self._ApplyTypes_(649, 1, (VT_VARIANT, 0), magic, u"PlaneFromPoints", None, *flattened)

    def plane_plane_intersection(self, plane_1, point_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane_1), flatten_params(point_2))

        return self._ApplyTypes_(744, 1, (VT_VARIANT, 0), magic, u"PlanePlaneIntersection", None, *flattened)

    def plane_transform(self, plane, xform):

        #magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        #flattened = (flatten_params(plane), flatten_params(xform))
        
        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(plane), xform)        

        return self._ApplyTypes_(801, 1, (VT_VARIANT, 0), magic, u"PlaneTransform", None, *flattened)

    def rotate_plane(self, plane, angle, axis):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane), angle, flatten_params(axis))

        return self._ApplyTypes_(630, 1, (VT_VARIANT, 0), magic, u"RotatePlane", None, *flattened)

    def world_x_y_plane(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(652, 1, (VT_VARIANT, 0), magic, u"WorldXYPlane", None, *flattened)

    def world_y_z_plane(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(653, 1, (VT_VARIANT, 0), magic, u"WorldYZPlane", None, *flattened)

    def world_z_x_plane(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(654, 1, (VT_VARIANT, 0), magic, u"WorldZXPlane", None, *flattened)

    def is_linetype(self, linetype):

        magic = ((VT_BSTR, 1),)
        flattened = (linetype,)

        return self._ApplyTypes_(607, 1, (VT_VARIANT, 0), magic, u"IsLinetype", None, *flattened)

    def is_linetype_reference(self, linetype):

        magic = ((VT_BSTR, 1),)
        flattened = (linetype,)

        return self._ApplyTypes_(608, 1, (VT_VARIANT, 0), magic, u"IsLinetypeReference", None, *flattened)

    def linetype_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(605, 1, (VT_VARIANT, 0), magic, u"LinetypeCount", None, *flattened)

    def linetype_names(self, sort):

        magic = ((VT_BOOL, 1),)
        flattened = (sort,)

        return self._ApplyTypes_(606, 1, (VT_VARIANT, 0), magic, u"LinetypeNames", None, *flattened)

    def add_material_to_layer(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(173, 1, (VT_VARIANT, 0), magic, u"AddMaterialToLayer", None, *flattened)

    def add_material_to_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(174, 1, (VT_VARIANT, 0), magic, u"AddMaterialToObject", None, *flattened)

    def copy_material(self, src_index, dst_index):

        magic = ((VT_I2, 1), (VT_I2, 1))
        flattened = (src_index, dst_index)

        return self._ApplyTypes_(812, 1, (VT_VARIANT, 0), magic, u"CopyMaterial", None, *flattened)

    def is_material_default(self, material_index):

        magic = ((VT_I2, 1),)
        flattened = (material_index,)

        return self._ApplyTypes_(175, 1, (VT_VARIANT, 0), magic, u"IsMaterialDefault", None, *flattened)

    def is_material_reference(self, material_index):

        magic = ((VT_I2, 1),)
        flattened = (material_index,)

        return self._ApplyTypes_(176, 1, (VT_VARIANT, 0), magic, u"IsMaterialReference", None, *flattened)

    def match_material(self, src_material_index):

        magic = ((VT_I2, 1),)
        flattened = (src_material_index,)

        return self._ApplyTypes_(322, 1, (VT_VARIANT, 0), magic, u"MatchMaterial", None, *flattened)

    def match_material_2(self, src_object, dest_objects):

        magic = ((VT_BSTR, 1), (VT_VARIANT, 1))
        flattened = (src_object, flatten_params(dest_objects))

        return self._ApplyTypes_(322, 1, (VT_VARIANT, 0), magic, u"MatchMaterial", None, *flattened)

    def material_bump(self, material_index, file_name):

        magic = ((VT_I2, 1), (VT_BSTR, 1))
        flattened = (material_index, file_name)

        return self._ApplyTypes_(177, 1, (VT_VARIANT, 0), magic, u"MaterialBump", None, *flattened)

    def material_color(self, material_index, color):

        magic = ((VT_I2, 1), (VT_I4, 1))
        flattened = (material_index, color)

        return self._ApplyTypes_(178, 1, (VT_VARIANT, 0), magic, u"MaterialColor", None, *flattened)

    def material_environment_map(self, material_index, file_name):

        magic = ((VT_I2, 1), (VT_BSTR, 1))
        flattened = (material_index, file_name)

        return self._ApplyTypes_(754, 1, (VT_VARIANT, 0), magic, u"MaterialEnvironmentMap", None, *flattened)

    def material_name(self, material_index, name):

        magic = ((VT_I2, 1), (VT_BSTR, 1))
        flattened = (material_index, name)

        return self._ApplyTypes_(179, 1, (VT_VARIANT, 0), magic, u"MaterialName", None, *flattened)

    def material_reflective_color(self, material_index, color):

        magic = ((VT_I2, 1), (VT_I4, 1))
        flattened = (material_index, color)

        return self._ApplyTypes_(180, 1, (VT_VARIANT, 0), magic, u"MaterialReflectiveColor", None, *flattened)

    def material_shine(self, material_index, shine):

        magic = ((VT_I2, 1), (VT_R8, 1))
        flattened = (material_index, shine)

        return self._ApplyTypes_(181, 1, (VT_VARIANT, 0), magic, u"MaterialShine", None, *flattened)

    def material_texture(self, material_index, file_name):

        magic = ((VT_I2, 1), (VT_BSTR, 1))
        flattened = (material_index, file_name)

        return self._ApplyTypes_(182, 1, (VT_VARIANT, 0), magic, u"MaterialTexture", None, *flattened)

    def material_transparency(self, material_index, transparency):

        magic = ((VT_I2, 1), (VT_R8, 1))
        flattened = (material_index, transparency)

        return self._ApplyTypes_(183, 1, (VT_VARIANT, 0), magic, u"MaterialTransparency", None, *flattened)

    def material_transparency_map(self, material_index, file_name):

        magic = ((VT_I2, 1), (VT_BSTR, 1))
        flattened = (material_index, file_name)

        return self._ApplyTypes_(753, 1, (VT_VARIANT, 0), magic, u"MaterialTransparencyMap", None, *flattened)

    def angle(self, point_1, point_2, world):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2), world)

        return self._ApplyTypes_(115, 1, (VT_VARIANT, 0), magic, u"Angle", None, *flattened)

    def angle_2(self, point_1, point_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2))

        return self._ApplyTypes_(116, 1, (VT_VARIANT, 0), magic, u"Angle2", None, *flattened)

    def deviation(self, numbers):

        magic = ((VT_ARRAY + VT_I2, 1),)
        flattened = (flatten_params(numbers),)

        return self._ApplyTypes_(773, 1, (VT_VARIANT, 0), magic, u"Deviation", None, *flattened)

    def distance(self, point_1, point_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2))

        return self._ApplyTypes_(118, 1, (VT_VARIANT, 0), magic, u"Distance", None, *flattened)

    def distance_2(self, point_1, point_array):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_array))

        return self._ApplyTypes_(118, 1, (VT_VARIANT, 0), magic, u"Distance", None, *flattened)

    def hypot(self, number_x, number_y):

        magic = ((VT_R8, 1), (VT_R8, 1))
        flattened = (number_x, number_y)

        return self._ApplyTypes_(765, 1, (VT_VARIANT, 0), magic, u"Hypot", None, *flattened)

    def max(self, numbers):

        magic = ((VT_ARRAY + VT_I2, 1),)
        flattened = (flatten_params(numbers),)

        return self._ApplyTypes_(768, 1, (VT_VARIANT, 0), magic, u"Max", None, *flattened)

    def mean(self, numbers):

        magic = ((VT_ARRAY + VT_I2, 1),)
        flattened = (flatten_params(numbers),)

        return self._ApplyTypes_(771, 1, (VT_VARIANT, 0), magic, u"Mean", None, *flattened)

    def median(self, numbers):

        magic = ((VT_ARRAY + VT_I2, 1),)
        flattened = (flatten_params(numbers),)

        return self._ApplyTypes_(772, 1, (VT_VARIANT, 0), magic, u"Median", None, *flattened)

    def min(self, numbers):

        magic = ((VT_ARRAY + VT_I2, 1),)
        flattened = (flatten_params(numbers),)

        return self._ApplyTypes_(769, 1, (VT_VARIANT, 0), magic, u"Min", None, *flattened)

    def polar(self, point, angle, distance, plane):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point), angle, distance, flatten_params(plane))

        return self._ApplyTypes_(662, 1, (VT_VARIANT, 0), magic, u"Polar", None, *flattened)

    def add_mesh(self, vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1))
        flattened = (flatten_params(vertices), flatten_params(face_vertices), flatten_params(vertex_normals), flatten_params(texture_coordinates), flatten_params(vertex_colors))
        #flattened = (vertices, flatten_params(face_vertices), flatten_params(vertex_normals), flatten_params(texture_coordinates), flatten_params(vertex_colors))
        

        return self._ApplyTypes_(494, 1, (VT_VARIANT, 0), magic, u"AddMesh", None, *flattened)

    def add_planar_mesh(self, object, delete):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, delete)

        return self._ApplyTypes_(915, 1, (VT_VARIANT, 0), magic, u"AddPlanarMesh", None, *flattened)

    def curve_mesh_intersection(self, curve, mesh, return_faces):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (curve, mesh, return_faces)

        return self._ApplyTypes_(842, 1, (VT_VARIANT, 0), magic, u"CurveMeshIntersection", None, *flattened)

    def disjoint_mesh_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(721, 1, (VT_VARIANT, 0), magic, u"DisjointMeshCount", None, *flattened)

    def duplicate_mesh_border(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(853, 1, (VT_VARIANT, 0), magic, u"DuplicateMeshBorder", None, *flattened)

    def explode_meshes(self, objects, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), delete)

        return self._ApplyTypes_(903, 1, (VT_VARIANT, 0), magic, u"ExplodeMeshes", None, *flattened)

    def is_mesh(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(119, 1, (VT_VARIANT, 0), magic, u"IsMesh", None, *flattened)

    def is_mesh_closed(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(355, 1, (VT_VARIANT, 0), magic, u"IsMeshClosed", None, *flattened)

    def is_mesh_manifold(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(855, 1, (VT_VARIANT, 0), magic, u"IsMeshManifold", None, *flattened)

    def mesh_area(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(353, 1, (VT_VARIANT, 0), magic, u"MeshArea", None, *flattened)

    def mesh_area_centroid(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(477, 1, (VT_VARIANT, 0), magic, u"MeshAreaCentroid", None, *flattened)

    def mesh_boolean_difference(self, input_0, input_1, delete):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input_0), flatten_params(input_1), delete)

        return self._ApplyTypes_(732, 1, (VT_VARIANT, 0), magic, u"MeshBooleanDifference", None, *flattened)

    def mesh_boolean_intersection(self, input_0, input_1, delete):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input_0), flatten_params(input_1), delete)

        return self._ApplyTypes_(733, 1, (VT_VARIANT, 0), magic, u"MeshBooleanIntersection", None, *flattened)

    def mesh_boolean_split(self, input_0, input_1, delete):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input_0), flatten_params(input_1), delete)

        return self._ApplyTypes_(734, 1, (VT_VARIANT, 0), magic, u"MeshBooleanSplit", None, *flattened)

    def mesh_boolean_union(self, input, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input), delete)

        return self._ApplyTypes_(731, 1, (VT_VARIANT, 0), magic, u"MeshBooleanUnion", None, *flattened)

    def mesh_closest_point(self, object, point, tolerance):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (object, flatten_params(point), tolerance)

        return self._ApplyTypes_(750, 1, (VT_VARIANT, 0), magic, u"MeshClosestPoint", None, *flattened)

    def mesh_contour_points(self, object, start_point, end_point, interval, remove_coincident_points):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(start_point), flatten_params(end_point), interval, remove_coincident_points)

        return self._ApplyTypes_(123, 1, (VT_VARIANT, 0), magic, u"MeshContourPoints", None, *flattened)

    def mesh_face_centers(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(570, 1, (VT_VARIANT, 0), magic, u"MeshFaceCenters", None, *flattened)

    def mesh_face_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(124, 1, (VT_VARIANT, 0), magic, u"MeshFaceCount", None, *flattened)

    def mesh_face_normals(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(569, 1, (VT_VARIANT, 0), magic, u"MeshFaceNormals", None, *flattened)

    def mesh_face_vertices(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(495, 1, (VT_VARIANT, 0), magic, u"MeshFaceVertices", None, *flattened)

    def mesh_faces(self, object, face_type):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, face_type)

        return self._ApplyTypes_(125, 1, (VT_VARIANT, 0), magic, u"MeshFaces", None, *flattened)

    def mesh_has_face_normals(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(696, 1, (VT_VARIANT, 0), magic, u"MeshHasFaceNormals", None, *flattened)

    def mesh_has_texture_coordinates(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(697, 1, (VT_VARIANT, 0), magic, u"MeshHasTextureCoordinates", None, *flattened)

    def mesh_has_vertex_colors(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(698, 1, (VT_VARIANT, 0), magic, u"MeshHasVertexColors", None, *flattened)

    def mesh_has_vertex_normals(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(695, 1, (VT_VARIANT, 0), magic, u"MeshHasVertexNormals", None, *flattened)

    def mesh_mesh_intersection(self, mesh_1, mesh_2, tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1))
        flattened = (mesh_1, mesh_2, tolerance)

        return self._ApplyTypes_(749, 1, (VT_VARIANT, 0), magic, u"MeshMeshIntersection", None, *flattened)

    def mesh_naked_edge_points(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(580, 1, (VT_VARIANT, 0), magic, u"MeshNakedEdgePoints", None, *flattened)

    def mesh_offset(self, mesh, distance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (mesh, distance)

        return self._ApplyTypes_(720, 1, (VT_VARIANT, 0), magic, u"MeshOffset", None, *flattened)

    def mesh_quad_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(350, 1, (VT_VARIANT, 0), magic, u"MeshQuadCount", None, *flattened)

    def mesh_quads_to_triangles(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(352, 1, (VT_VARIANT, 0), magic, u"MeshQuadsToTriangles", None, *flattened)

    def mesh_texture_coordinates(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(425, 1, (VT_VARIANT, 0), magic, u"MeshTextureCoordinates", None, *flattened)

    def mesh_triangle_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(351, 1, (VT_VARIANT, 0), magic, u"MeshTriangleCount", None, *flattened)

    def mesh_vertex_colors(self, object, vertex_colors):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_I2, 1))
        flattened = (object, flatten_params(vertex_colors))

        return self._ApplyTypes_(699, 1, (VT_VARIANT, 0), magic, u"MeshVertexColors", None, *flattened)

    def mesh_vertex_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(126, 1, (VT_VARIANT, 0), magic, u"MeshVertexCount", None, *flattened)

    def mesh_vertex_normals(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(426, 1, (VT_VARIANT, 0), magic, u"MeshVertexNormals", None, *flattened)

    def mesh_vertices(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(127, 1, (VT_VARIANT, 0), magic, u"MeshVertices", None, *flattened)

    def mesh_volume(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(354, 1, (VT_VARIANT, 0), magic, u"MeshVolume", None, *flattened)

    def mesh_volume_centroid(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(478, 1, (VT_VARIANT, 0), magic, u"MeshVolumeCentroid", None, *flattened)

    def pull_curve_to_mesh(self, mesh, curve):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (mesh, curve)

        return self._ApplyTypes_(719, 1, (VT_VARIANT, 0), magic, u"PullCurveToMesh", None, *flattened)

    def split_disjoint_mesh(self, object, delete):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, delete)

        return self._ApplyTypes_(722, 1, (VT_VARIANT, 0), magic, u"SplitDisjointMesh", None, *flattened)

    def unify_mesh_normals(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(723, 1, (VT_VARIANT, 0), magic, u"UnifyMeshNormals", None, *flattened)

    def add_object_mesh(self, object, quality, enable):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, quality, enable)

        return self._ApplyTypes_(866, 1, (VT_VARIANT, 0), magic, u"AddObjectMesh", None, *flattened)

    def box_morph_object(self, objects, box_points, copy):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), flatten_params(box_points), copy)

        return self._ApplyTypes_(918, 1, (VT_VARIANT, 0), magic, u"BoxMorphObject", None, *flattened)

    def copy_object(self, object, start, end):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(start), flatten_params(end))

        return self._ApplyTypes_(184, 1, (VT_VARIANT, 0), magic, u"CopyObject", None, *flattened)

    def copy_object_2(self, object, translation):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(translation))

        return self._ApplyTypes_(184, 1, (VT_VARIANT, 0), magic, u"CopyObject", None, *flattened)

    def copy_objects(self, objects, start, end):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(objects), flatten_params(start), flatten_params(end))

        return self._ApplyTypes_(295, 1, (VT_VARIANT, 0), magic, u"CopyObjects", None, *flattened)

    def copy_objects_2(self, translation):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(translation),)

        return self._ApplyTypes_(295, 1, (VT_VARIANT, 0), magic, u"CopyObjects", None, *flattened)

    def delete_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(185, 1, (VT_VARIANT, 0), magic, u"DeleteObject", None, *flattened)

    def delete_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(186, 1, (VT_VARIANT, 0), magic, u"DeleteObjects", None, *flattened)

    def enable_object_mesh(self, objects, enable):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), enable)

        return self._ApplyTypes_(856, 1, (VT_VARIANT, 0), magic, u"EnableObjectMesh", None, *flattened)

    def flash_object(self, objects, style):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), style)

        return self._ApplyTypes_(869, 1, (VT_VARIANT, 0), magic, u"FlashObject", None, *flattened)

    def hide_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(187, 1, (VT_VARIANT, 0), magic, u"HideObject", None, *flattened)

    def hide_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(303, 1, (VT_VARIANT, 0), magic, u"HideObjects", None, *flattened)

    def is_layout_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(919, 1, (VT_VARIANT, 0), magic, u"IsLayoutObject", None, *flattened)

    def is_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(46, 1, (VT_VARIANT, 0), magic, u"IsObject", None, *flattened)

    def is_object_hidden(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(47, 1, (VT_VARIANT, 0), magic, u"IsObjectHidden", None, *flattened)

    def is_object_in_box(self, object, box, mode):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(box), mode)

        return self._ApplyTypes_(799, 1, (VT_VARIANT, 0), magic, u"IsObjectInBox", None, *flattened)

    def is_object_in_group(self, object, group):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, group)

        return self._ApplyTypes_(188, 1, (VT_VARIANT, 0), magic, u"IsObjectInGroup", None, *flattened)

    def is_object_locked(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(48, 1, (VT_VARIANT, 0), magic, u"IsObjectLocked", None, *flattened)

    def is_object_normal(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(49, 1, (VT_VARIANT, 0), magic, u"IsObjectNormal", None, *flattened)

    def is_object_reference(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(271, 1, (VT_VARIANT, 0), magic, u"IsObjectReference", None, *flattened)

    def is_object_selectable(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(307, 1, (VT_VARIANT, 0), magic, u"IsObjectSelectable", None, *flattened)

    def is_object_selected(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(50, 1, (VT_VARIANT, 0), magic, u"IsObjectSelected", None, *flattened)

    def is_object_solid(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(189, 1, (VT_VARIANT, 0), magic, u"IsObjectSolid", None, *flattened)

    def is_object_valid(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(522, 1, (VT_VARIANT, 0), magic, u"IsObjectValid", None, *flattened)

    def is_visible_in_view(self, object, view):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, view)

        return self._ApplyTypes_(727, 1, (VT_VARIANT, 0), magic, u"IsVisibleInView", None, *flattened)

    def lock_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(190, 1, (VT_VARIANT, 0), magic, u"LockObject", None, *flattened)

    def lock_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(304, 1, (VT_VARIANT, 0), magic, u"LockObjects", None, *flattened)

    def match_object_attributes(self, targets, source):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(targets), source)

        return self._ApplyTypes_(781, 1, (VT_VARIANT, 0), magic, u"MatchObjectAttributes", None, *flattened)

    def mirror_object(self, object, start_pt, end_pt, copy):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(start_pt), flatten_params(end_pt), copy)

        return self._ApplyTypes_(589, 1, (VT_VARIANT, 0), magic, u"MirrorObject", None, *flattened)

    def mirror_objects(self, objects, start_pt, end_pt, copy):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), flatten_params(start_pt), flatten_params(end_pt), copy)

        return self._ApplyTypes_(590, 1, (VT_VARIANT, 0), magic, u"MirrorObjects", None, *flattened)

    def move_object(self, object, start, end):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(start), flatten_params(end))

        return self._ApplyTypes_(270, 1, (VT_VARIANT, 0), magic, u"MoveObject", None, *flattened)

    def move_object_2(self, object, translation):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(translation))

        return self._ApplyTypes_(270, 1, (VT_VARIANT, 0), magic, u"MoveObject", None, *flattened)

    def move_objects(self, objects, start, end):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(objects), flatten_params(start), flatten_params(end))

        return self._ApplyTypes_(296, 1, (VT_VARIANT, 0), magic, u"MoveObjects", None, *flattened)

    def move_objects_2(self, translation):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(translation),)

        return self._ApplyTypes_(296, 1, (VT_VARIANT, 0), magic, u"MoveObjects", None, *flattened)

    def object_color(self, objects, color):

        magic = ((VT_VARIANT, 1), (VT_I4, 1))
        flattened = (flatten_params(objects), color)

        return self._ApplyTypes_(191, 1, (VT_VARIANT, 0), magic, u"ObjectColor", None, *flattened)

    def object_color_source(self, objects, source):

        magic = ((VT_VARIANT, 1), (VT_I2, 1))
        flattened = (flatten_params(objects), source)

        return self._ApplyTypes_(192, 1, (VT_VARIANT, 0), magic, u"ObjectColorSource", None, *flattened)

    def object_description(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(470, 1, (VT_VARIANT, 0), magic, u"ObjectDescription", None, *flattened)

    def object_dump(self, object, type):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, type)

        return self._ApplyTypes_(705, 1, (VT_VARIANT, 0), magic, u"ObjectDump", None, *flattened)

    def object_groups(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(193, 1, (VT_VARIANT, 0), magic, u"ObjectGroups", None, *flattened)

    def object_has_mesh(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(867, 1, (VT_VARIANT, 0), magic, u"ObjectHasMesh", None, *flattened)

    def object_layer(self, objects, layer):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(objects), layer)

        return self._ApplyTypes_(51, 1, (VT_VARIANT, 0), magic, u"ObjectLayer", None, *flattened)

    def object_layout(self, object, layout, return_name):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, layout, return_name)

        return self._ApplyTypes_(924, 1, (VT_VARIANT, 0), magic, u"ObjectLayout", None, *flattened)

    def object_linetype(self, objects, layer):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(objects), layer)

        return self._ApplyTypes_(646, 1, (VT_VARIANT, 0), magic, u"ObjectLinetype", None, *flattened)

    def object_linetype_source(self, objects, source):

        magic = ((VT_VARIANT, 1), (VT_I2, 1))
        flattened = (flatten_params(objects), source)

        return self._ApplyTypes_(647, 1, (VT_VARIANT, 0), magic, u"ObjectLinetypeSource", None, *flattened)

    def object_material_index(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(194, 1, (VT_VARIANT, 0), magic, u"ObjectMaterialIndex", None, *flattened)

    def object_material_source(self, objects, source):

        magic = ((VT_VARIANT, 1), (VT_I2, 1))
        flattened = (flatten_params(objects), source)

        return self._ApplyTypes_(195, 1, (VT_VARIANT, 0), magic, u"ObjectMaterialSource", None, *flattened)

    def object_mesh_density(self, object, density):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, density)

        return self._ApplyTypes_(858, 1, (VT_VARIANT, 0), magic, u"ObjectMeshDensity", None, *flattened)

    def object_mesh_max_angle(self, object, angle):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, angle)

        return self._ApplyTypes_(859, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxAngle", None, *flattened)

    def object_mesh_max_aspect_ratio(self, object, ratio):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, ratio)

        return self._ApplyTypes_(860, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxAspectRatio", None, *flattened)

    def object_mesh_max_dist_edge_to_srf(self, object, distance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, distance)

        return self._ApplyTypes_(863, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxDistEdgeToSrf", None, *flattened)

    def object_mesh_max_edge_length(self, object, length):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, length)

        return self._ApplyTypes_(862, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMaxEdgeLength", None, *flattened)

    def object_mesh_min_edge_length(self, object, length):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, length)

        return self._ApplyTypes_(861, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMinEdgeLength", None, *flattened)

    def object_mesh_min_initial_grid_quads(self, object, quads):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, quads)

        return self._ApplyTypes_(864, 1, (VT_VARIANT, 0), magic, u"ObjectMeshMinInitialGridQuads", None, *flattened)

    def object_mesh_quality(self, object, quality):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, quality)

        return self._ApplyTypes_(857, 1, (VT_VARIANT, 0), magic, u"ObjectMeshQuality", None, *flattened)

    def object_mesh_settings(self, object, settings):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, settings)

        return self._ApplyTypes_(865, 1, (VT_VARIANT, 0), magic, u"ObjectMeshSettings", None, *flattened)

    def object_name(self, objects, name):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(objects), name)

        return self._ApplyTypes_(196, 1, (VT_VARIANT, 0), magic, u"ObjectName", None, *flattened)

    def object_names(self, objects, names):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(objects), flatten_params(names))

        return self._ApplyTypes_(639, 1, (VT_VARIANT, 0), magic, u"ObjectNames", None, *flattened)

    def object_print_color(self, objects, color):

        magic = ((VT_VARIANT, 1), (VT_I4, 1))
        flattened = (flatten_params(objects), color)

        return self._ApplyTypes_(805, 1, (VT_VARIANT, 0), magic, u"ObjectPrintColor", None, *flattened)

    def object_print_color_source(self, objects, source):

        magic = ((VT_VARIANT, 1), (VT_I2, 1))
        flattened = (flatten_params(objects), source)

        return self._ApplyTypes_(806, 1, (VT_VARIANT, 0), magic, u"ObjectPrintColorSource", None, *flattened)

    def object_print_width(self, objects, width):

        magic = ((VT_VARIANT, 1), (VT_R8, 1))
        flattened = (flatten_params(objects), width)

        return self._ApplyTypes_(807, 1, (VT_VARIANT, 0), magic, u"ObjectPrintWidth", None, *flattened)

    def object_print_width_source(self, objects, source):

        magic = ((VT_VARIANT, 1), (VT_I2, 1))
        flattened = (flatten_params(objects), source)

        return self._ApplyTypes_(808, 1, (VT_VARIANT, 0), magic, u"ObjectPrintWidthSource", None, *flattened)

    def object_top_group(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(197, 1, (VT_VARIANT, 0), magic, u"ObjectTopGroup", None, *flattened)

    def object_type(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(198, 1, (VT_VARIANT, 0), magic, u"ObjectType", None, *flattened)

    def object_u_r_l(self, objects, u_r_l):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1))
        flattened = (flatten_params(objects), u_r_l)

        return self._ApplyTypes_(199, 1, (VT_VARIANT, 0), magic, u"ObjectURL", None, *flattened)

    def orient_object(self, object, reference, target, flags):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (object, flatten_params(reference), flatten_params(target), flags)

        return self._ApplyTypes_(390, 1, (VT_VARIANT, 0), magic, u"OrientObject", None, *flattened)

    def orient_objects(self, objects, reference, target, flags):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (flatten_params(objects), flatten_params(reference), flatten_params(target), flags)

        return self._ApplyTypes_(391, 1, (VT_VARIANT, 0), magic, u"OrientObjects", None, *flattened)

    def remap_object(self, object, src_plane, dst_plane, copy):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(src_plane), flatten_params(dst_plane), copy)

        return self._ApplyTypes_(655, 1, (VT_VARIANT, 0), magic, u"RemapObject", None, *flattened)

    def remap_objects(self, object, src_plane, dst_plane, copy):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(object), flatten_params(src_plane), flatten_params(dst_plane), copy)

        return self._ApplyTypes_(656, 1, (VT_VARIANT, 0), magic, u"RemapObjects", None, *flattened)

    def rotate_object(self, object, point, angle, axis, copy):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(point), angle, flatten_params(axis), copy)

        return self._ApplyTypes_(392, 1, (VT_VARIANT, 0), magic, u"RotateObject", None, *flattened)

    def rotate_objects(self, objects, point, angle, axis, copy):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), flatten_params(point), angle, flatten_params(axis), copy)

        return self._ApplyTypes_(393, 1, (VT_VARIANT, 0), magic, u"RotateObjects", None, *flattened)

    def scale_object(self, object, origin, scale, copy):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(origin), flatten_params(scale), copy)

        return self._ApplyTypes_(585, 1, (VT_VARIANT, 0), magic, u"ScaleObject", None, *flattened)

    def scale_objects(self, objects, origin, scale, copy):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), flatten_params(origin), flatten_params(scale), copy)

        return self._ApplyTypes_(586, 1, (VT_VARIANT, 0), magic, u"ScaleObjects", None, *flattened)

    def select_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(200, 1, (VT_VARIANT, 0), magic, u"SelectObject", None, *flattened)

    def select_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(298, 1, (VT_VARIANT, 0), magic, u"SelectObjects", None, *flattened)

    def shear_object(self, object, origin, ref_pt, scale, copy):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (object, flatten_params(origin), flatten_params(ref_pt), scale, copy)

        return self._ApplyTypes_(587, 1, (VT_VARIANT, 0), magic, u"ShearObject", None, *flattened)

    def shear_objects(self, objects, origin, ref_pt, scale, copy):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), flatten_params(origin), flatten_params(ref_pt), scale, copy)

        return self._ApplyTypes_(588, 1, (VT_VARIANT, 0), magic, u"ShearObjects", None, *flattened)

    def show_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(201, 1, (VT_VARIANT, 0), magic, u"ShowObject", None, *flattened)

    def show_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(305, 1, (VT_VARIANT, 0), magic, u"ShowObjects", None, *flattened)

    def transform_object(self, object, matrix, copy):

        magic = ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (object, matrix, copy)

        return self._ApplyTypes_(272, 1, (VT_VARIANT, 0), magic, u"TransformObject", None, *flattened)

    def transform_objects(self, objects, matrix, copy):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (objects, flatten_params(matrix), copy)

        return self._ApplyTypes_(302, 1, (VT_VARIANT, 0), magic, u"TransformObjects", None, *flattened)

    def unlock_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(202, 1, (VT_VARIANT, 0), magic, u"UnlockObject", None, *flattened)

    def unlock_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(306, 1, (VT_VARIANT, 0), magic, u"UnlockObjects", None, *flattened)

    def unselect_object(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(299, 1, (VT_VARIANT, 0), magic, u"UnselectObject", None, *flattened)

    def unselect_objects(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(300, 1, (VT_VARIANT, 0), magic, u"UnselectObjects", None, *flattened)

    def enable_object_grips(self, object, enable):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, enable)

        return self._ApplyTypes_(499, 1, (VT_VARIANT, 0), magic, u"EnableObjectGrips", None, *flattened)

    def get_object_grip(self, message, pre_select, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (message, pre_select, select)

        return self._ApplyTypes_(561, 1, (VT_VARIANT, 0), magic, u"GetObjectGrip", None, *flattened)

    def get_object_grips(self, message, pre_select, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (message, pre_select, select)

        return self._ApplyTypes_(562, 1, (VT_VARIANT, 0), magic, u"GetObjectGrips", None, *flattened)

    def next_object_grip(self, object, index, direction, enable):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, index, direction, enable)

        return self._ApplyTypes_(558, 1, (VT_VARIANT, 0), magic, u"NextObjectGrip", None, *flattened)

    def object_grip_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(500, 1, (VT_VARIANT, 0), magic, u"ObjectGripCount", None, *flattened)

    def object_grip_location(self, object, index, point):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, index, flatten_params(point))

        return self._ApplyTypes_(556, 1, (VT_VARIANT, 0), magic, u"ObjectGripLocation", None, *flattened)

    def object_grip_locations(self, object, points):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(points))

        return self._ApplyTypes_(557, 1, (VT_VARIANT, 0), magic, u"ObjectGripLocations", None, *flattened)

    def object_grips_on(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(497, 1, (VT_VARIANT, 0), magic, u"ObjectGripsOn", None, *flattened)

    def object_grips_selected(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(498, 1, (VT_VARIANT, 0), magic, u"ObjectGripsSelected", None, *flattened)

    def prev_object_grip(self, object, index, direction, enable):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, index, direction, enable)

        return self._ApplyTypes_(559, 1, (VT_VARIANT, 0), magic, u"PrevObjectGrip", None, *flattened)

    def select_object_grip(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(554, 1, (VT_VARIANT, 0), magic, u"SelectObjectGrip", None, *flattened)

    def select_object_grips(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(501, 1, (VT_VARIANT, 0), magic, u"SelectObjectGrips", None, *flattened)

    def selected_object_grips(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(560, 1, (VT_VARIANT, 0), magic, u"SelectedObjectGrips", None, *flattened)

    def unselect_object_grip(self, object, index):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, index)

        return self._ApplyTypes_(555, 1, (VT_VARIANT, 0), magic, u"UnselectObjectGrip", None, *flattened)

    def unselect_object_grips(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(502, 1, (VT_VARIANT, 0), magic, u"UnselectObjectGrips", None, *flattened)

    def is_vector_parallel_to(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(660, 1, (VT_VARIANT, 0), magic, u"IsVectorParallelTo", None, *flattened)

    def is_vector_perpendicular_to(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(661, 1, (VT_VARIANT, 0), magic, u"IsVectorPerpendicularTo", None, *flattened)

    def is_vector_tiny(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(610, 1, (VT_VARIANT, 0), magic, u"IsVectorTiny", None, *flattened)

    def is_vector_zero(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(611, 1, (VT_VARIANT, 0), magic, u"IsVectorZero", None, *flattened)

    def point_add(self, point_1, point_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2))

        return self._ApplyTypes_(666, 1, (VT_VARIANT, 0), magic, u"PointAdd", None, *flattened)

    def point_array_bounding_box(self, points, view, world_coords):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (flatten_params(points), view, world_coords)

        return self._ApplyTypes_(746, 1, (VT_VARIANT, 0), magic, u"PointArrayBoundingBox", None, *flattened)

    def point_array_closest_point(self, points, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(points), flatten_params(point))

        return self._ApplyTypes_(742, 1, (VT_VARIANT, 0), magic, u"PointArrayClosestPoint", None, *flattened)

    def point_array_transform(self, points, xform):

        #magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        #flattened = (flatten_params(points), flatten_params(xform))
        
        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(points), xform)     

        return self._ApplyTypes_(802, 1, (VT_VARIANT, 0), magic, u"PointArrayTransform", None, *flattened)

    def point_compare(self, point_1, point_2, tolerance):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2), tolerance)

        return self._ApplyTypes_(667, 1, (VT_VARIANT, 0), magic, u"PointCompare", None, *flattened)

    def point_divide(self, point, scale):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(point), scale)

        return self._ApplyTypes_(668, 1, (VT_VARIANT, 0), magic, u"PointDivide", None, *flattened)

    def point_scale(self, point, scale):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(point), scale)

        return self._ApplyTypes_(669, 1, (VT_VARIANT, 0), magic, u"PointScale", None, *flattened)

    def point_subtract(self, point_1, point_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2))

        return self._ApplyTypes_(670, 1, (VT_VARIANT, 0), magic, u"PointSubtract", None, *flattened)

    def point_transform(self, point, xform):

        #magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        #flattened = (flatten_params(point), flatten_params(xform))
        
        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(point), xform)        

        return self._ApplyTypes_(671, 1, (VT_VARIANT, 0), magic, u"PointTransform", None, *flattened)

    def points_are_coplanar(self, points, tolerance):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(points), tolerance)

        return self._ApplyTypes_(593, 1, (VT_VARIANT, 0), magic, u"PointsAreCoplanar", None, *flattened)

    def project_point_to_mesh(self, points, meshes, direction):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(points), flatten_params(meshes), flatten_params(direction))

        return self._ApplyTypes_(912, 1, (VT_VARIANT, 0), magic, u"ProjectPointToMesh", None, *flattened)

    def project_point_to_surface(self, points, surfaces, direction):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(points), flatten_params(surfaces), flatten_params(direction))

        return self._ApplyTypes_(892, 1, (VT_VARIANT, 0), magic, u"ProjectPointToSurface", None, *flattened)

    def pull_points(self, object, points):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(points))

        return self._ApplyTypes_(716, 1, (VT_VARIANT, 0), magic, u"PullPoints", None, *flattened)

    def vector_add(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(612, 1, (VT_VARIANT, 0), magic, u"VectorAdd", None, *flattened)

    def vector_compare(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(613, 1, (VT_VARIANT, 0), magic, u"VectorCompare", None, *flattened)

    def vector_create(self, point_1, point_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point_1), flatten_params(point_2))

        return self._ApplyTypes_(614, 1, (VT_VARIANT, 0), magic, u"VectorCreate", None, *flattened)

    def vector_cross_product(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(615, 1, (VT_VARIANT, 0), magic, u"VectorCrossProduct", None, *flattened)

    def vector_divide(self, vector, divide):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(vector), divide)

        return self._ApplyTypes_(625, 1, (VT_VARIANT, 0), magic, u"VectorDivide", None, *flattened)

    def vector_dot_product(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(616, 1, (VT_VARIANT, 0), magic, u"VectorDotProduct", None, *flattened)

    def vector_length(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(617, 1, (VT_VARIANT, 0), magic, u"VectorLength", None, *flattened)

    def vector_multiply(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(624, 1, (VT_VARIANT, 0), magic, u"VectorMultiply", None, *flattened)

    def vector_reverse(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(618, 1, (VT_VARIANT, 0), magic, u"VectorReverse", None, *flattened)

    def vector_rotate(self, vector, angle, axis):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector), angle, flatten_params(axis))

        return self._ApplyTypes_(678, 1, (VT_VARIANT, 0), magic, u"VectorRotate", None, *flattened)

    def vector_scale(self, vector, scale):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(vector), scale)

        return self._ApplyTypes_(619, 1, (VT_VARIANT, 0), magic, u"VectorScale", None, *flattened)

    def vector_subtract(self, vector_1, vector_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(vector_1), flatten_params(vector_2))

        return self._ApplyTypes_(620, 1, (VT_VARIANT, 0), magic, u"VectorSubtract", None, *flattened)

    def vector_transform(self, vector, xform):

        #magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        #flattened = (flatten_params(vector), flatten_params(xform))
        
        magic = ((VT_ARRAY + VT_R8, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(vector), xform)

        return self._ApplyTypes_(800, 1, (VT_VARIANT, 0), magic, u"VectorTransform", None, *flattened)

    def vector_unitize(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(621, 1, (VT_VARIANT, 0), magic, u"VectorUnitize", None, *flattened)

    def all_objects(self, select, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (select, include_lights, include_grips)

        return self._ApplyTypes_(30, 1, (VT_VARIANT, 0), magic, u"AllObjects", None, *flattened)

    def first_object(self, select, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (select, include_lights, include_grips)

        return self._ApplyTypes_(31, 1, (VT_VARIANT, 0), magic, u"FirstObject", None, *flattened)

    def get_curve_object(self, message, pre_select, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (message, pre_select, select)

        return self._ApplyTypes_(575, 1, (VT_VARIANT, 0), magic, u"GetCurveObject", None, *flattened)

    def get_object(self, message, type, pre_select, select, objects):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1))
        flattened = (message, type, pre_select, select, flatten_params(objects))

        return self._ApplyTypes_(32, 1, (VT_VARIANT, 0), magic, u"GetObject", None, *flattened)

    def get_object_ex(self, message, type, pre_select, select, objects):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1))
        flattened = (message, type, pre_select, select, flatten_params(objects))

        return self._ApplyTypes_(819, 1, (VT_VARIANT, 0), magic, u"GetObjectEx", None, *flattened)

    def get_objects(self, message, type, group, pre_select, select, objects):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1))
        flattened = (message, type, group, pre_select, select, flatten_params(objects))

        return self._ApplyTypes_(33, 1, (VT_VARIANT, 0), magic, u"GetObjects", None, *flattened)

    def get_objects_ex(self, message, type, group, pre_select, select, objects):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_VARIANT, 1))
        flattened = (message, type, group, pre_select, select, flatten_params(objects))

        return self._ApplyTypes_(820, 1, (VT_VARIANT, 0), magic, u"GetObjectsEx", None, *flattened)

    def get_point_coordinates(self, message, pre_select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (message, pre_select)

        return self._ApplyTypes_(645, 1, (VT_VARIANT, 0), magic, u"GetPointCoordinates", None, *flattened)

    def get_surface_object(self, message, pre_select, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (message, pre_select, select)

        return self._ApplyTypes_(576, 1, (VT_VARIANT, 0), magic, u"GetSurfaceObject", None, *flattened)

    def hidden_objects(self, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (include_lights, include_grips)

        return self._ApplyTypes_(366, 1, (VT_VARIANT, 0), magic, u"HiddenObjects", None, *flattened)

    def invert_selected_objects(self, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (include_lights, include_grips)

        return self._ApplyTypes_(34, 1, (VT_VARIANT, 0), magic, u"InvertSelectedObjects", None, *flattened)

    def last_created_objects(self, select):

        magic = ((VT_BOOL, 1),)
        flattened = (select,)

        return self._ApplyTypes_(485, 1, (VT_VARIANT, 0), magic, u"LastCreatedObjects", None, *flattened)

    def last_object(self, select, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (select, include_lights, include_grips)

        return self._ApplyTypes_(35, 1, (VT_VARIANT, 0), magic, u"LastObject", None, *flattened)

    def locked_objects(self, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (include_lights, include_grips)

        return self._ApplyTypes_(365, 1, (VT_VARIANT, 0), magic, u"LockedObjects", None, *flattened)

    def next_object(self, object, select, include_lights, include_grips):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (object, select, include_lights, include_grips)

        return self._ApplyTypes_(36, 1, (VT_VARIANT, 0), magic, u"NextObject", None, *flattened)

    def normal_objects(self, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (include_lights, include_grips)

        return self._ApplyTypes_(364, 1, (VT_VARIANT, 0), magic, u"NormalObjects", None, *flattened)

    def objects_by_color(self, color, select, include_lights):

        magic = ((VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (color, select, include_lights)

        return self._ApplyTypes_(37, 1, (VT_VARIANT, 0), magic, u"ObjectsByColor", None, *flattened)

    def objects_by_group(self, group, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (group, select)

        return self._ApplyTypes_(38, 1, (VT_VARIANT, 0), magic, u"ObjectsByGroup", None, *flattened)

    def objects_by_layer(self, layer, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (layer, select)

        return self._ApplyTypes_(39, 1, (VT_VARIANT, 0), magic, u"ObjectsByLayer", None, *flattened)

    def objects_by_name(self, name, select, include_lights):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (name, select, include_lights)

        return self._ApplyTypes_(40, 1, (VT_VARIANT, 0), magic, u"ObjectsByName", None, *flattened)

    def objects_by_type(self, type, select):

        magic = ((VT_I2, 1), (VT_BOOL, 1))
        flattened = (type, select)

        return self._ApplyTypes_(41, 1, (VT_VARIANT, 0), magic, u"ObjectsByType", None, *flattened)

    def objects_by_u_r_l(self, u_r_l, select, include_lights):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (u_r_l, select, include_lights)

        return self._ApplyTypes_(42, 1, (VT_VARIANT, 0), magic, u"ObjectsByURL", None, *flattened)

    def prev_selected_objects(self, select):

        magic = ((VT_BOOL, 1),)
        flattened = (select,)

        return self._ApplyTypes_(486, 1, (VT_VARIANT, 0), magic, u"PrevSelectedObjects", None, *flattened)

    def reference_objects(self, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (include_lights, include_grips)

        return self._ApplyTypes_(367, 1, (VT_VARIANT, 0), magic, u"ReferenceObjects", None, *flattened)

    def selected_objects(self, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (include_lights, include_grips)

        return self._ApplyTypes_(43, 1, (VT_VARIANT, 0), magic, u"SelectedObjects", None, *flattened)

    def unselect_all_objects(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(44, 1, (VT_VARIANT, 0), magic, u"UnselectAllObjects", None, *flattened)

    def unselected_objects(self, select, include_lights, include_grips):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (select, include_lights, include_grips)

        return self._ApplyTypes_(45, 1, (VT_VARIANT, 0), magic, u"UnselectedObjects", None, *flattened)

    def visible_objects(self, view, select, include_lights, include_grips):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (view, select, include_lights, include_grips)

        return self._ApplyTypes_(825, 1, (VT_VARIANT, 0), magic, u"VisibleObjects", None, *flattened)

    def add_box(self, corners):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(corners),)

        return self._ApplyTypes_(72, 1, (VT_VARIANT, 0), magic, u"AddBox", None, *flattened)

    def add_cone(self, base, height_pnt, radius, cap):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(base), flatten_params(height_pnt), radius, cap)

        return self._ApplyTypes_(75, 1, (VT_VARIANT, 0), magic, u"AddCone", None, *flattened)

    def add_cone_2(self, plane, height, radius, cap):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(plane), height, radius, cap)

        return self._ApplyTypes_(75, 1, (VT_VARIANT, 0), magic, u"AddCone", None, *flattened)

    def add_cut_plane(self, objects, start_point, end_point, normal):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(objects), flatten_params(start_point), flatten_params(end_point), flatten_params(normal))

        return self._ApplyTypes_(822, 1, (VT_VARIANT, 0), magic, u"AddCutPlane", None, *flattened)

    def add_cylinder(self, base, height_pnt, radius, cap):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(base), flatten_params(height_pnt), radius, cap)

        return self._ApplyTypes_(73, 1, (VT_VARIANT, 0), magic, u"AddCylinder", None, *flattened)

    def add_cylinder_2(self, plane, height, radius, cap):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (flatten_params(plane), height, radius, cap)

        return self._ApplyTypes_(73, 1, (VT_VARIANT, 0), magic, u"AddCylinder", None, *flattened)

    def add_edge_srf(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(203, 1, (VT_VARIANT, 0), magic, u"AddEdgeSrf", None, *flattened)

    def add_loft_srf(self, objects, start_pt, end_pt, type, style, value, closed):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), flatten_params(start_pt), flatten_params(end_pt), type, style, value, closed)

        return self._ApplyTypes_(567, 1, (VT_VARIANT, 0), magic, u"AddLoftSrf", None, *flattened)

    def add_nurbs_surface(self, point_count, points, knots_u, knots_v, degree, weights):

        magic = ((VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_I2, 1))
        flattened = (flatten_params(point_count), flatten_params(points), flatten_params(knots_u), flatten_params(knots_v), flatten_params(degree), flatten_params(weights))

        return self._ApplyTypes_(435, 1, (VT_VARIANT, 0), magic, u"AddNurbsSurface", None, *flattened)

    def add_planar_srf(self, objects):

        magic = ((VT_VARIANT, 1),)
        flattened = (flatten_params(objects),)

        return self._ApplyTypes_(371, 1, (VT_VARIANT, 0), magic, u"AddPlanarSrf", None, *flattened)

    def add_plane_surface(self, plane, d_u, d_v):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), d_u, d_v)

        return self._ApplyTypes_(648, 1, (VT_VARIANT, 0), magic, u"AddPlaneSurface", None, *flattened)

    def add_rail_rev_srf(self, profile, rail, axis):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (profile, rail, flatten_params(axis))

        return self._ApplyTypes_(536, 1, (VT_VARIANT, 0), magic, u"AddRailRevSrf", None, *flattened)

    def add_rev_srf(self, profile, axis, start_angle, end_angle):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (profile, flatten_params(axis), start_angle, end_angle)

        return self._ApplyTypes_(535, 1, (VT_VARIANT, 0), magic, u"AddRevSrf", None, *flattened)

    def add_sphere(self, center, radius):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(center), radius)

        return self._ApplyTypes_(71, 1, (VT_VARIANT, 0), magic, u"AddSphere", None, *flattened)

    def add_sphere_2(self, plane, radius):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), radius)

        return self._ApplyTypes_(71, 1, (VT_VARIANT, 0), magic, u"AddSphere", None, *flattened)

    def add_srf_contour_crvs(self, object, start_point, end_point, interval):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (object, flatten_params(start_point), flatten_params(end_point), interval)

        return self._ApplyTypes_(747, 1, (VT_VARIANT, 0), magic, u"AddSrfContourCrvs", None, *flattened)

    def add_srf_contour_crvs_2(self, object, plane, interval):
        """
        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (object, flatten_params(plane), interval)
        """
        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (object, pythoncom.Empty, flatten_params(plane), interval)        

        return self._ApplyTypes_(747, 1, (VT_VARIANT, 0), magic, u"AddSrfContourCrvs", None, *flattened)

    def add_srf_control_pt_grid(self, count, points, degree):

        magic = ((VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(count), flatten_params(points), flatten_params(degree))

        return self._ApplyTypes_(294, 1, (VT_VARIANT, 0), magic, u"AddSrfControlPtGrid", None, *flattened)

    def add_srf_pt(self, points):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(points),)

        return self._ApplyTypes_(204, 1, (VT_VARIANT, 0), magic, u"AddSrfPt", None, *flattened)

    def add_srf_pt_grid(self, count, points, degree, closed):

        magic = ((VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_BOOL, 1))
        flattened = (flatten_params(count), flatten_params(points), flatten_params(degree), flatten_params(closed))

        return self._ApplyTypes_(293, 1, (VT_VARIANT, 0), magic, u"AddSrfPtGrid", None, *flattened)

    def add_srf_section_crvs(self, object, plane):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(plane))

        return self._ApplyTypes_(803, 1, (VT_VARIANT, 0), magic, u"AddSrfSectionCrvs", None, *flattened)

    def add_sweep_1(self, rail, shapes, start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg):

        magic = ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1), (VT_I2, 1), (VT_VARIANT, 1), (VT_I2, 1), (VT_VARIANT, 1))
        flattened = (rail, flatten_params(shapes), flatten_params(start_pt), flatten_params(end_pt), closed, style, style_arg, simplify, simplify_arg)

        return self._ApplyTypes_(893, 1, (VT_VARIANT, 0), magic, u"AddSweep1", None, *flattened)

    def add_sweep_2(self, rails, shapes, start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_I2, 1), (VT_VARIANT, 1))
        flattened = (flatten_params(rails), flatten_params(shapes), flatten_params(start_pt), flatten_params(end_pt), closed, simple_sweep, maintain_height, simplify, simplify_arg)

        return self._ApplyTypes_(894, 1, (VT_VARIANT, 0), magic, u"AddSweep2", None, *flattened)

    def add_torus(self, base, major_radius, minor_radius, direction):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(base), major_radius, minor_radius, flatten_params(direction))

        return self._ApplyTypes_(74, 1, (VT_VARIANT, 0), magic, u"AddTorus", None, *flattened)

    def add_torus_2(self, plane, major_radius, minor_radius):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), major_radius, minor_radius)

        return self._ApplyTypes_(74, 1, (VT_VARIANT, 0), magic, u"AddTorus", None, *flattened)

    def boolean_difference(self, input_0, input_1, delete):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input_0), flatten_params(input_1), delete)

        return self._ApplyTypes_(508, 1, (VT_VARIANT, 0), magic, u"BooleanDifference", None, *flattened)

    def boolean_intersection(self, input_0, input_1, delete):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input_0), flatten_params(input_1), delete)

        return self._ApplyTypes_(507, 1, (VT_VARIANT, 0), magic, u"BooleanIntersection", None, *flattened)

    def boolean_union(self, input, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(input), delete)

        return self._ApplyTypes_(506, 1, (VT_VARIANT, 0), magic, u"BooleanUnion", None, *flattened)

    def brep_closest_point(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(514, 1, (VT_VARIANT, 0), magic, u"BrepClosestPoint", None, *flattened)

    def cap_planar_holes(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(701, 1, (VT_VARIANT, 0), magic, u"CapPlanarHoles", None, *flattened)

    def duplicate_edge_curves(self, object, select):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, select)

        return self._ApplyTypes_(657, 1, (VT_VARIANT, 0), magic, u"DuplicateEdgeCurves", None, *flattened)

    def duplicate_surface_border(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(852, 1, (VT_VARIANT, 0), magic, u"DuplicateSurfaceBorder", None, *flattened)

    def evaluate_surface(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(parameter))

        return self._ApplyTypes_(205, 1, (VT_VARIANT, 0), magic, u"EvaluateSurface", None, *flattened)

    def explode_polysurfaces(self, objects, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(objects), delete)

        return self._ApplyTypes_(447, 1, (VT_VARIANT, 0), magic, u"ExplodePolysurfaces", None, *flattened)

    def extract_iso_curve(self, object, parameter, dir):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (object, flatten_params(parameter), dir)

        return self._ApplyTypes_(488, 1, (VT_VARIANT, 0), magic, u"ExtractIsoCurve", None, *flattened)

    def extrude_curve(self, curve, path):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (curve, path)

        return self._ApplyTypes_(538, 1, (VT_VARIANT, 0), magic, u"ExtrudeCurve", None, *flattened)

    def extrude_curve_point(self, curve, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (curve, flatten_params(point))

        return self._ApplyTypes_(540, 1, (VT_VARIANT, 0), magic, u"ExtrudeCurvePoint", None, *flattened)

    def extrude_curve_straight(self, curve, start_point, end_point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (curve, flatten_params(start_point), flatten_params(end_point))

        return self._ApplyTypes_(539, 1, (VT_VARIANT, 0), magic, u"ExtrudeCurveStraight", None, *flattened)

    def extrude_curve_tapered(self, curve, distance, direction, base_point, angle, corner_type):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_I2, 1))
        flattened = (curve, distance, flatten_params(direction), flatten_params(base_point), angle, corner_type)

        return self._ApplyTypes_(914, 1, (VT_VARIANT, 0), magic, u"ExtrudeCurveTapered", None, *flattened)

    def extrude_surface(self, surface, curve, cap):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (surface, curve, cap)

        return self._ApplyTypes_(541, 1, (VT_VARIANT, 0), magic, u"ExtrudeSurface", None, *flattened)

    def fit_surface(self, object, degree, tolerance):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_I2, 1), (VT_R8, 1))
        flattened = (object, flatten_params(degree), tolerance)

        return self._ApplyTypes_(815, 1, (VT_VARIANT, 0), magic, u"FitSurface", None, *flattened)

    def flip_surface(self, object, flip):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, flip)

        return self._ApplyTypes_(718, 1, (VT_VARIANT, 0), magic, u"FlipSurface", None, *flattened)

    def insert_surface_knot(self, object, parameter, direction, symmetrical):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, parameter, direction, symmetrical)

        return self._ApplyTypes_(516, 1, (VT_VARIANT, 0), magic, u"InsertSurfaceKnot", None, *flattened)

    def intersect_breps(self, brep_1, brep_2, tolerance):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1))
        flattened = (brep_1, brep_2, tolerance)

        return self._ApplyTypes_(544, 1, (VT_VARIANT, 0), magic, u"IntersectBreps", None, *flattened)

    def is_brep(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(206, 1, (VT_VARIANT, 0), magic, u"IsBrep", None, *flattened)

    def is_brep_manifold(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(854, 1, (VT_VARIANT, 0), magic, u"IsBrepManifold", None, *flattened)

    def is_cone(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(885, 1, (VT_VARIANT, 0), magic, u"IsCone", None, *flattened)

    def is_cylinder(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(884, 1, (VT_VARIANT, 0), magic, u"IsCylinder", None, *flattened)

    def is_parameter_on_surface(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(parameter))

        return self._ApplyTypes_(879, 1, (VT_VARIANT, 0), magic, u"IsParameterOnSurface", None, *flattened)

    def is_plane_surface(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(638, 1, (VT_VARIANT, 0), magic, u"IsPlaneSurface", None, *flattened)

    def is_point_in_surface(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(443, 1, (VT_VARIANT, 0), magic, u"IsPointInSurface", None, *flattened)

    def is_point_on_surface(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(319, 1, (VT_VARIANT, 0), magic, u"IsPointOnSurface", None, *flattened)

    def is_poly_surface(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(207, 1, (VT_VARIANT, 0), magic, u"IsPolySurface", None, *flattened)

    def is_poly_surface_closed(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(208, 1, (VT_VARIANT, 0), magic, u"IsPolySurfaceClosed", None, *flattened)

    def is_poly_surface_planar(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(209, 1, (VT_VARIANT, 0), magic, u"IsPolySurfacePlanar", None, *flattened)

    def is_sphere(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(883, 1, (VT_VARIANT, 0), magic, u"IsSphere", None, *flattened)

    def is_surface(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(210, 1, (VT_VARIANT, 0), magic, u"IsSurface", None, *flattened)

    def is_surface_closed(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, direction)

        return self._ApplyTypes_(211, 1, (VT_VARIANT, 0), magic, u"IsSurfaceClosed", None, *flattened)

    def is_surface_periodic(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, direction)

        return self._ApplyTypes_(212, 1, (VT_VARIANT, 0), magic, u"IsSurfacePeriodic", None, *flattened)

    def is_surface_planar(self, object, tolerance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, tolerance)

        return self._ApplyTypes_(213, 1, (VT_VARIANT, 0), magic, u"IsSurfacePlanar", None, *flattened)

    def is_surface_rational(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(434, 1, (VT_VARIANT, 0), magic, u"IsSurfaceRational", None, *flattened)

    def is_surface_singular(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, direction)

        return self._ApplyTypes_(214, 1, (VT_VARIANT, 0), magic, u"IsSurfaceSingular", None, *flattened)

    def is_surface_trimmed(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(269, 1, (VT_VARIANT, 0), magic, u"IsSurfaceTrimmed", None, *flattened)

    def is_torus(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(886, 1, (VT_VARIANT, 0), magic, u"IsTorus", None, *flattened)

    def join_surfaces(self, object, delete):

        magic = ((VT_VARIANT, 1), (VT_BOOL, 1))
        flattened = (flatten_params(object), delete)

        return self._ApplyTypes_(487, 1, (VT_VARIANT, 0), magic, u"JoinSurfaces", None, *flattened)

    def make_surface_non_periodic(self, object, direction, delete):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, direction, delete)

        return self._ApplyTypes_(926, 1, (VT_VARIANT, 0), magic, u"MakeSurfaceNonPeriodic", None, *flattened)

    def make_surface_periodic(self, object, direction, delete):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (object, direction, delete)

        return self._ApplyTypes_(445, 1, (VT_VARIANT, 0), magic, u"MakeSurfacePeriodic", None, *flattened)

    def offset_surface(self, object, distance):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (object, distance)

        return self._ApplyTypes_(635, 1, (VT_VARIANT, 0), magic, u"OffsetSurface", None, *flattened)

    def pull_curve(self, surface, curve, delete):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (surface, curve, delete)

        return self._ApplyTypes_(493, 1, (VT_VARIANT, 0), magic, u"PullCurve", None, *flattened)

    def rebuild_surface(self, object, degree, point_count):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_I2, 1))
        flattened = (object, flatten_params(degree), flatten_params(point_count))

        return self._ApplyTypes_(816, 1, (VT_VARIANT, 0), magic, u"RebuildSurface", None, *flattened)

    def remove_surface_knot(self, object, parameter, direction):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1))
        flattened = (object, parameter, direction)

        return self._ApplyTypes_(917, 1, (VT_VARIANT, 0), magic, u"RemoveSurfaceKnot", None, *flattened)

    def reverse_surface(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, direction)

        return self._ApplyTypes_(927, 1, (VT_VARIANT, 0), magic, u"ReverseSurface", None, *flattened)

    def short_path(self, surface, start, end):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (surface, flatten_params(start), flatten_params(end))

        return self._ApplyTypes_(702, 1, (VT_VARIANT, 0), magic, u"ShortPath", None, *flattened)

    def shrink_trimmed_surface(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(700, 1, (VT_VARIANT, 0), magic, u"ShrinkTrimmedSurface", None, *flattened)

    def split_brep(self, brep, cutter, delete):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (brep, cutter, delete)

        return self._ApplyTypes_(637, 1, (VT_VARIANT, 0), magic, u"SplitBrep", None, *flattened)

    def surface_area(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(382, 1, (VT_VARIANT, 0), magic, u"SurfaceArea", None, *flattened)

    def surface_area_centroid(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(384, 1, (VT_VARIANT, 0), magic, u"SurfaceAreaCentroid", None, *flattened)

    def surface_area_moments(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(386, 1, (VT_VARIANT, 0), magic, u"SurfaceAreaMoments", None, *flattened)

    def surface_closest_point(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(215, 1, (VT_VARIANT, 0), magic, u"SurfaceClosestPoint", None, *flattened)

    def surface_cone(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(889, 1, (VT_VARIANT, 0), magic, u"SurfaceCone", None, *flattened)

    def surface_contour_points(self, object, start_point, end_point, interval, angle):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (object, flatten_params(start_point), flatten_params(end_point), interval, angle)

        return self._ApplyTypes_(79, 1, (VT_VARIANT, 0), magic, u"SurfaceContourPoints", None, *flattened)

    def surface_curvature(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(parameter))

        return self._ApplyTypes_(378, 1, (VT_VARIANT, 0), magic, u"SurfaceCurvature", None, *flattened)

    def surface_curvature_analysis(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(632, 1, (VT_VARIANT, 0), magic, u"SurfaceCurvatureAnalysis", None, *flattened)

    def surface_cylinder(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(888, 1, (VT_VARIANT, 0), magic, u"SurfaceCylinder", None, *flattened)

    def surface_degree(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, direction)

        return self._ApplyTypes_(216, 1, (VT_VARIANT, 0), magic, u"SurfaceDegree", None, *flattened)

    def surface_domain(self, object, direction):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, direction)

        return self._ApplyTypes_(217, 1, (VT_VARIANT, 0), magic, u"SurfaceDomain", None, *flattened)

    def surface_edit_points(self, object, return_parameters, return_all):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (object, return_parameters, return_all)

        return self._ApplyTypes_(427, 1, (VT_VARIANT, 0), magic, u"SurfaceEditPoints", None, *flattened)

    def surface_evaluate(self, object, parameter, derivative):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_I2, 1))
        flattened = (object, flatten_params(parameter), derivative)

        return self._ApplyTypes_(583, 1, (VT_VARIANT, 0), magic, u"SurfaceEvaluate", None, *flattened)

    def surface_frame(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(parameter))

        return self._ApplyTypes_(623, 1, (VT_VARIANT, 0), magic, u"SurfaceFrame", None, *flattened)

    def surface_isocurve_density(self, object, density):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (object, density)

        return self._ApplyTypes_(361, 1, (VT_VARIANT, 0), magic, u"SurfaceIsocurveDensity", None, *flattened)

    def surface_knot_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(431, 1, (VT_VARIANT, 0), magic, u"SurfaceKnotCount", None, *flattened)

    def surface_knots(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(432, 1, (VT_VARIANT, 0), magic, u"SurfaceKnots", None, *flattened)

    def surface_normal(self, object, parameter):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(parameter))

        return self._ApplyTypes_(362, 1, (VT_VARIANT, 0), magic, u"SurfaceNormal", None, *flattened)

    def surface_point_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(218, 1, (VT_VARIANT, 0), magic, u"SurfacePointCount", None, *flattened)

    def surface_points(self, object, return_all):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, return_all)

        return self._ApplyTypes_(372, 1, (VT_VARIANT, 0), magic, u"SurfacePoints", None, *flattened)

    def surface_principal_curvature(self, object, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (object, flatten_params(point))

        return self._ApplyTypes_(717, 1, (VT_VARIANT, 0), magic, u"SurfacePrincipalCurvature", None, *flattened)

    def surface_seam(self, object, direction, parameter):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1))
        flattened = (object, direction, parameter)

        return self._ApplyTypes_(804, 1, (VT_VARIANT, 0), magic, u"SurfaceSeam", None, *flattened)

    def surface_sphere(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(887, 1, (VT_VARIANT, 0), magic, u"SurfaceSphere", None, *flattened)

    def surface_surface_intersection(self, surface_a, surface_b, tolerance, create):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (surface_a, surface_b, tolerance, create)

        return self._ApplyTypes_(484, 1, (VT_VARIANT, 0), magic, u"SurfaceSurfaceIntersection", None, *flattened)

    def surface_torus(self, surface):

        magic = ((VT_BSTR, 1),)
        flattened = (surface,)

        return self._ApplyTypes_(890, 1, (VT_VARIANT, 0), magic, u"SurfaceTorus", None, *flattened)

    def surface_volume(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(383, 1, (VT_VARIANT, 0), magic, u"SurfaceVolume", None, *flattened)

    def surface_volume_centroid(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(385, 1, (VT_VARIANT, 0), magic, u"SurfaceVolumeCentroid", None, *flattened)

    def surface_volume_moments(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(387, 1, (VT_VARIANT, 0), magic, u"SurfaceVolumeMoments", None, *flattened)

    def surface_weights(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(433, 1, (VT_VARIANT, 0), magic, u"SurfaceWeights", None, *flattened)

    def is_xform_identity(self, xform):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(xform),)

        return self._ApplyTypes_(786, 1, (VT_VARIANT, 0), magic, u"IsXformIdentity", None, *flattened)

    def is_xform_similarity(self, xform):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(xform),)

        return self._ApplyTypes_(787, 1, (VT_VARIANT, 0), magic, u"IsXformSimilarity", None, *flattened)

    def is_xform_zero(self, xform):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(xform),)

        return self._ApplyTypes_(785, 1, (VT_VARIANT, 0), magic, u"IsXformZero", None, *flattened)

    def xform_c_plane_to_world(self, point, plane):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point), flatten_params(plane))

        return self._ApplyTypes_(131, 1, (VT_VARIANT, 0), magic, u"XformCPlaneToWorld", None, *flattened)

    def xform_change_basis(self, plane_1, plane_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane_1), flatten_params(plane_2))

        return self._ApplyTypes_(796, 1, (VT_VARIANT, 0), magic, u"XformChangeBasis", None, *flattened)

    def xform_change_basis_2(self, x_0, y_0, z_0, x_1, y_1, z_1):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(x_0), flatten_params(y_0), flatten_params(z_0), flatten_params(x_1), flatten_params(y_1), flatten_params(z_1))

        return self._ApplyTypes_(796, 1, (VT_VARIANT, 0), magic, u"XformChangeBasis", None, *flattened)

    def xform_compare(self, xform_1, xform_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(xform_1), flatten_params(xform_2))

        return self._ApplyTypes_(789, 1, (VT_VARIANT, 0), magic, u"XformCompare", None, *flattened)

    def xform_determinant(self, xform):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(xform),)

        return self._ApplyTypes_(818, 1, (VT_VARIANT, 0), magic, u"XformDeterminant", None, *flattened)

    def xform_diagonal(self, value):

        magic = ((VT_R8, 1),)
        flattened = (value,)

        return self._ApplyTypes_(784, 1, (VT_VARIANT, 0), magic, u"XformDiagonal", None, *flattened)

    def xform_identity(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(783, 1, (VT_VARIANT, 0), magic, u"XformIdentity", None, *flattened)

    def xform_inverse(self, xform):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(xform),)

        return self._ApplyTypes_(817, 1, (VT_VARIANT, 0), magic, u"XformInverse", None, *flattened)

    def xform_mirror(self, point, normal):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point), flatten_params(normal))

        return self._ApplyTypes_(795, 1, (VT_VARIANT, 0), magic, u"XformMirror", None, *flattened)

    def xform_multiply(self, xform_1, xform_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(xform_1), flatten_params(xform_2))

        return self._ApplyTypes_(788, 1, (VT_VARIANT, 0), magic, u"XformMultiply", None, *flattened)

    def xform_planar_projection(self, plane):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(plane),)

        return self._ApplyTypes_(793, 1, (VT_VARIANT, 0), magic, u"XformPlanarProjection", None, *flattened)

    def xform_rotation(self, plane_1, plane_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane_1), flatten_params(plane_2))

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_rotation_2(self, angle, axis, point):

        magic = ((VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (angle, flatten_params(axis), flatten_params(point))

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_rotation_3(self, start_dir, end_dir, point):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(start_dir), flatten_params(end_dir), flatten_params(point))

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_rotation_4(self, x_0, y_0, z_0, x_1, y_1, z_1):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(x_0), flatten_params(y_0), flatten_params(z_0), flatten_params(x_1), flatten_params(y_1), flatten_params(z_1))

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_scale(self, plane, x_scale, y_scale, z_scale):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(plane), x_scale, y_scale, z_scale)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_scale_2(self, x_scale, y_scale, z_scale):

        magic = ((VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (x_scale, y_scale, z_scale)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_scale_3(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_scale_4(self, point, scale):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(point), scale)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_screen_to_world(self, point, view, convert):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (flatten_params(point), view, convert)

        return self._ApplyTypes_(581, 1, (VT_VARIANT, 0), magic, u"XformScreenToWorld", None, *flattened)

    def xform_shear(self, plane, x_1, y_1, z_1):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(plane), flatten_params(x_1), flatten_params(y_1), flatten_params(z_1))

        return self._ApplyTypes_(791, 1, (VT_VARIANT, 0), magic, u"XformShear", None, *flattened)

    def xform_translation(self, vector):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(vector),)

        return self._ApplyTypes_(792, 1, (VT_VARIANT, 0), magic, u"XformTranslation", None, *flattened)

    def xform_world_to_c_plane(self, point, plane):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (flatten_params(point), flatten_params(plane))

        return self._ApplyTypes_(132, 1, (VT_VARIANT, 0), magic, u"XformWorldToCPlane", None, *flattened)

    def xform_world_to_screen(self, point, view, convert):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (flatten_params(point), view, convert)

        return self._ApplyTypes_(582, 1, (VT_VARIANT, 0), magic, u"XformWorldToScreen", None, *flattened)

    def xform_zero(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(782, 1, (VT_VARIANT, 0), magic, u"XformZero", None, *flattened)

    def attribute_data_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(685, 1, (VT_VARIANT, 0), magic, u"AttributeDataCount", None, *flattened)

    def delete_attribute_data(self, object, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, section, entry)

        return self._ApplyTypes_(684, 1, (VT_VARIANT, 0), magic, u"DeleteAttributeData", None, *flattened)

    def delete_document_data(self, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (section, entry)

        return self._ApplyTypes_(237, 1, (VT_VARIANT, 0), magic, u"DeleteDocumentData", None, *flattened)

    def delete_object_data(self, object, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, section, entry)

        return self._ApplyTypes_(238, 1, (VT_VARIANT, 0), magic, u"DeleteObjectData", None, *flattened)

    def document_data_count(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(239, 1, (VT_VARIANT, 0), magic, u"DocumentDataCount", None, *flattened)

    def get_attribute_data(self, object, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, section, entry)

        return self._ApplyTypes_(682, 1, (VT_VARIANT, 0), magic, u"GetAttributeData", None, *flattened)

    def get_document_data(self, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (section, entry)

        return self._ApplyTypes_(240, 1, (VT_VARIANT, 0), magic, u"GetDocumentData", None, *flattened)

    def get_object_data(self, object, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, section, entry)

        return self._ApplyTypes_(241, 1, (VT_VARIANT, 0), magic, u"GetObjectData", None, *flattened)

    def get_user_text(self, object, key, attach_to_geometry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, key, attach_to_geometry)

        return self._ApplyTypes_(729, 1, (VT_VARIANT, 0), magic, u"GetUserText", None, *flattened)

    def is_attribute_data(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(686, 1, (VT_VARIANT, 0), magic, u"IsAttributeData", None, *flattened)

    def is_document_data(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(278, 1, (VT_VARIANT, 0), magic, u"IsDocumentData", None, *flattened)

    def is_object_data(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(279, 1, (VT_VARIANT, 0), magic, u"IsObjectData", None, *flattened)

    def is_user_text(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(730, 1, (VT_VARIANT, 0), magic, u"IsUserText", None, *flattened)

    def object_data_count(self, object):

        magic = ((VT_BSTR, 1),)
        flattened = (object,)

        return self._ApplyTypes_(242, 1, (VT_VARIANT, 0), magic, u"ObjectDataCount", None, *flattened)

    def set_attribute_data(self, object, section, entry, value):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, section, entry, value)

        return self._ApplyTypes_(683, 1, (VT_VARIANT, 0), magic, u"SetAttributeData", None, *flattened)

    def set_document_data(self, section, entry, value):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (section, entry, value)

        return self._ApplyTypes_(243, 1, (VT_VARIANT, 0), magic, u"SetDocumentData", None, *flattened)

    def set_object_data(self, object, section, entry, value):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, section, entry, value)

        return self._ApplyTypes_(244, 1, (VT_VARIANT, 0), magic, u"SetObjectData", None, *flattened)

    def set_user_text(self, object, key, value, attach_to_geometry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (object, key, value, attach_to_geometry)

        return self._ApplyTypes_(728, 1, (VT_VARIANT, 0), magic, u"SetUserText", None, *flattened)

    def browse_for_folder(self, folder, message, title):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (folder, message, title)

        return self._ApplyTypes_(146, 1, (VT_VARIANT, 0), magic, u"BrowseForFolder", None, *flattened)

    def check_list_box(self, items, values, message, title):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_BOOL, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(items), flatten_params(values), message, title)

        return self._ApplyTypes_(52, 1, (VT_VARIANT, 0), magic, u"CheckListBox", None, *flattened)

    def combo_list_box(self, items, message, title):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(items), message, title)

        return self._ApplyTypes_(53, 1, (VT_VARIANT, 0), magic, u"ComboListBox", None, *flattened)

    def edit_box(self, string, message, title):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (string, message, title)

        return self._ApplyTypes_(54, 1, (VT_VARIANT, 0), magic, u"EditBox", None, *flattened)

    def get_angle(self, point, reference, angle, message):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BSTR, 1))
        flattened = (flatten_params(point), flatten_params(reference), angle, message)

        return self._ApplyTypes_(277, 1, (VT_VARIANT, 0), magic, u"GetAngle", None, *flattened)

    def get_boolean(self, message, items, defaults):

        magic = ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_ARRAY + VT_BOOL, 1))
        flattened = (message, flatten_params(items), flatten_params(defaults))

        return self._ApplyTypes_(622, 1, (VT_VARIANT, 0), magic, u"GetBoolean", None, *flattened)

    def get_box(self, mode, point, prompt_1, prompt_2, prompt_3):

        magic = ((VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (mode, flatten_params(point), prompt_1, prompt_2, prompt_3)

        return self._ApplyTypes_(342, 1, (VT_VARIANT, 0), magic, u"GetBox", None, *flattened)

    def get_color(self, color):

        magic = ((VT_I4, 1),)
        flattened = (color,)

        return self._ApplyTypes_(65, 1, (VT_VARIANT, 0), magic, u"GetColor", None, *flattened)

    def get_distance(self, point, distance, message_1, message_2):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(point), distance, message_1, message_2)

        return self._ApplyTypes_(66, 1, (VT_VARIANT, 0), magic, u"GetDistance", None, *flattened)

    def get_integer(self, message, number, min, max):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_I2, 1))
        flattened = (message, number, min, max)

        return self._ApplyTypes_(64, 1, (VT_VARIANT, 0), magic, u"GetInteger", None, *flattened)

    def get_layer(self, title, layer, show_new_layer, show_set_current):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1))
        flattened = (title, layer, show_new_layer, show_set_current)

        return self._ApplyTypes_(672, 1, (VT_VARIANT, 0), magic, u"GetLayer", None, *flattened)

    def get_linetype(self, linetype):

        magic = ((VT_BSTR, 1),)
        flattened = (linetype,)

        return self._ApplyTypes_(673, 1, (VT_VARIANT, 0), magic, u"GetLinetype", None, *flattened)

    def get_point(self, message, point, distance, plane):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1))
        flattened = (message, flatten_params(point), distance, plane)

        return self._ApplyTypes_(61, 1, (VT_VARIANT, 0), magic, u"GetPoint", None, *flattened)

    def get_point_on_curve(self, object, message):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, message)

        return self._ApplyTypes_(147, 1, (VT_VARIANT, 0), magic, u"GetPointOnCurve", None, *flattened)

    def get_point_on_line(self, message, start, end, track):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1))
        flattened = (message, flatten_params(start), flatten_params(end), track)

        return self._ApplyTypes_(798, 1, (VT_VARIANT, 0), magic, u"GetPointOnLine", None, *flattened)

    def get_point_on_mesh(self, object, message):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, message)

        return self._ApplyTypes_(401, 1, (VT_VARIANT, 0), magic, u"GetPointOnMesh", None, *flattened)

    def get_point_on_plane(self, message, plane, point):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (message, flatten_params(plane), flatten_params(point))

        return self._ApplyTypes_(797, 1, (VT_VARIANT, 0), magic, u"GetPointOnPlane", None, *flattened)

    def get_point_on_surface(self, object, message):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, message)

        return self._ApplyTypes_(148, 1, (VT_VARIANT, 0), magic, u"GetPointOnSurface", None, *flattened)

    def get_points(self, draw, plane, message_1, message_2, max_points, base_point):

        magic = ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_I2, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (draw, plane, message_1, message_2, max_points, flatten_params(base_point))

        return self._ApplyTypes_(67, 1, (VT_VARIANT, 0), magic, u"GetPoints", None, *flattened)

    def get_print_width(self, print_width):

        magic = ((VT_R8, 1),)
        flattened = (print_width,)

        return self._ApplyTypes_(674, 1, (VT_VARIANT, 0), magic, u"GetPrintWidth", None, *flattened)

    def get_real(self, message, number, min, max):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1), (VT_R8, 1))
        flattened = (message, number, min, max)

        return self._ApplyTypes_(63, 1, (VT_VARIANT, 0), magic, u"GetReal", None, *flattened)

    def get_rectangle(self, mode, point, prompt_1, prompt_2, prompt_3):

        magic = ((VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (mode, flatten_params(point), prompt_1, prompt_2, prompt_3)

        return self._ApplyTypes_(341, 1, (VT_VARIANT, 0), magic, u"GetRectangle", None, *flattened)

    def get_string(self, message, string, strings):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1))
        flattened = (message, string, flatten_params(strings))

        return self._ApplyTypes_(62, 1, (VT_VARIANT, 0), magic, u"GetString", None, *flattened)

    def get_surface_iso_param_point(self, object, message):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (object, message)

        return self._ApplyTypes_(775, 1, (VT_VARIANT, 0), magic, u"GetSurfaceIsoParamPoint", None, *flattened)

    def html_box(self, file_name, arguments, options, modal):

        magic = ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (file_name, arguments, options, modal)

        return self._ApplyTypes_(276, 1, (VT_VARIANT, 0), magic, u"HtmlBox", None, *flattened)

    def integer_box(self, message, number, title):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BSTR, 1))
        flattened = (message, number, title)

        return self._ApplyTypes_(55, 1, (VT_VARIANT, 0), magic, u"IntegerBox", None, *flattened)

    def list_box(self, items, message, title):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(items), message, title)

        return self._ApplyTypes_(56, 1, (VT_VARIANT, 0), magic, u"ListBox", None, *flattened)

    def message_beep(self, beep):

        magic = ((VT_I2, 1),)
        flattened = (beep,)

        return self._ApplyTypes_(149, 1, (VT_VARIANT, 0), magic, u"MessageBeep", None, *flattened)

    def message_box(self, message, buttons, title):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_BSTR, 1))
        flattened = (message, buttons, title)

        return self._ApplyTypes_(150, 1, (VT_VARIANT, 0), magic, u"MessageBox", None, *flattened)

    def multi_list_box(self, items, message, title):

        magic = ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(items), message, title)

        return self._ApplyTypes_(57, 1, (VT_VARIANT, 0), magic, u"MultiListBox", None, *flattened)

    def open_file_name(self, title, filter, folder, filename, extension):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (title, filter, folder, filename, extension)

        return self._ApplyTypes_(151, 1, (VT_VARIANT, 0), magic, u"OpenFileName", None, *flattened)

    def open_file_names(self, title, filter, folder, filename, extension):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (title, filter, folder, filename, extension)

        return self._ApplyTypes_(821, 1, (VT_VARIANT, 0), magic, u"OpenFileNames", None, *flattened)

    def popup_menu(self, items, modes, point, view):

        magic = ((VT_VARIANT, 1), (VT_ARRAY + VT_I2, 1), (VT_ARRAY + VT_R8, 1), (VT_BSTR, 1))
        flattened = (flatten_params(items), flatten_params(modes), flatten_params(point), view)

        return self._ApplyTypes_(595, 1, (VT_VARIANT, 0), magic, u"PopupMenu", None, *flattened)

    def property_list_box(self, items, values, message, title):

        magic = ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (flatten_params(items), flatten_params(values), message, title)

        return self._ApplyTypes_(58, 1, (VT_VARIANT, 0), magic, u"PropertyListBox", None, *flattened)

    def real_box(self, message, number, title):

        magic = ((VT_BSTR, 1), (VT_R8, 1), (VT_BSTR, 1))
        flattened = (message, number, title)

        return self._ApplyTypes_(59, 1, (VT_VARIANT, 0), magic, u"RealBox", None, *flattened)

    def save_file_name(self, title, filter, folder, filename, extension):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (title, filter, folder, filename, extension)

        return self._ApplyTypes_(152, 1, (VT_VARIANT, 0), magic, u"SaveFileName", None, *flattened)

    def string_box(self, message, string, title):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (message, string, title)

        return self._ApplyTypes_(60, 1, (VT_VARIANT, 0), magic, u"StringBox", None, *flattened)

    def all_procedures(self, all):

        magic = ((VT_BOOL, 1),)
        flattened = (all,)

        return self._ApplyTypes_(503, 1, (VT_VARIANT, 0), magic, u"AllProcedures", None, *flattened)

    def clipboard_text(self, text):

        magic = ((VT_BSTR, 1),)
        flattened = (text,)

        return self._ApplyTypes_(245, 1, (VT_VARIANT, 0), magic, u"ClipboardText", None, *flattened)

    def color_adjust_luma(self, r_g_b, luma, scale):

        magic = ((VT_I4, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (r_g_b, luma, scale)

        return self._ApplyTypes_(878, 1, (VT_VARIANT, 0), magic, u"ColorAdjustLuma", None, *flattened)

    def color_blue_value(self, r_g_b):

        magic = ((VT_I4, 1),)
        flattened = (r_g_b,)

        return self._ApplyTypes_(882, 1, (VT_VARIANT, 0), magic, u"ColorBlueValue", None, *flattened)

    def color_green_value(self, r_g_b):

        magic = ((VT_I4, 1),)
        flattened = (r_g_b,)

        return self._ApplyTypes_(881, 1, (VT_VARIANT, 0), magic, u"ColorGreenValue", None, *flattened)

    def color_h_l_s_to_r_g_b(self, r_g_b):

        magic = ((VT_I4, 1),)
        flattened = (r_g_b,)

        return self._ApplyTypes_(877, 1, (VT_VARIANT, 0), magic, u"ColorHLSToRGB", None, *flattened)

    def color_r_g_b_to_h_l_s(self, r_g_b):

        magic = ((VT_I4, 1),)
        flattened = (r_g_b,)

        return self._ApplyTypes_(876, 1, (VT_VARIANT, 0), magic, u"ColorRGBToHLS", None, *flattened)

    def color_red_value(self, r_g_b):

        magic = ((VT_I4, 1),)
        flattened = (r_g_b,)

        return self._ApplyTypes_(880, 1, (VT_VARIANT, 0), magic, u"ColorRedValue", None, *flattened)

    def cull_duplicate_numbers(self, numbers, tolerance):

        magic = ((VT_ARRAY + VT_I2, 1), (VT_R8, 1))
        flattened = (flatten_params(numbers), tolerance)

        return self._ApplyTypes_(550, 1, (VT_VARIANT, 0), magic, u"CullDuplicateNumbers", None, *flattened)

    def cull_duplicate_points(self, points, tolerance):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (flatten_params(points), tolerance)

        return self._ApplyTypes_(548, 1, (VT_VARIANT, 0), magic, u"CullDuplicatePoints", None, *flattened)

    def cull_duplicate_strings(self, strings, case_sensitive):

        magic = ((VT_ARRAY + VT_I2, 1), (VT_BOOL, 1))
        flattened = (flatten_params(strings), case_sensitive)

        return self._ApplyTypes_(549, 1, (VT_VARIANT, 0), magic, u"CullDuplicateStrings", None, *flattened)

    def current_printer(self, printer):

        magic = ((VT_BSTR, 1),)
        flattened = (printer,)

        return self._ApplyTypes_(358, 1, (VT_VARIANT, 0), magic, u"CurrentPrinter", None, *flattened)

    def get_settings(self, filename, section, entry):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (filename, section, entry)

        return self._ApplyTypes_(246, 1, (VT_VARIANT, 0), magic, u"GetSettings", None, *flattened)

    def is_procedure(self, sub_name):

        magic = ((VT_BSTR, 1),)
        flattened = (sub_name,)

        return self._ApplyTypes_(287, 1, (VT_VARIANT, 0), magic, u"IsProcedure", None, *flattened)

    def printer_names(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(356, 1, (VT_VARIANT, 0), magic, u"PrinterNames", None, *flattened)

    def pt_2_str(self, point, precision, space):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_I2, 1), (VT_BOOL, 1))
        flattened = (flatten_params(point), precision, space)

        return self._ApplyTypes_(297, 1, (VT_VARIANT, 0), magic, u"Pt2Str", None, *flattened)

    def save_settings(self, filename, section, entry, string):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (filename, section, entry, string)

        return self._ApplyTypes_(247, 1, (VT_VARIANT, 0), magic, u"SaveSettings", None, *flattened)

    def simplify_array(self, points):

        magic = ((VT_ARRAY + VT_R8, 1),)
        flattened = (flatten_params(points),)

        return self._ApplyTypes_(597, 1, (VT_VARIANT, 0), magic, u"SimplifyArray", None, *flattened)

    def sleep(self, milliseconds):

        magic = ((VT_I4, 1),)
        flattened = (milliseconds,)

        return self._ApplyTypes_(248, 1, (VT_VARIANT, 0), magic, u"Sleep", None, *flattened)

    def spool_to_printer(self, file, printer):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (file, printer)

        return self._ApplyTypes_(357, 1, (VT_VARIANT, 0), magic, u"SpoolToPrinter", None, *flattened)

    def str_2_pt(self, point):

        magic = ((VT_BSTR, 1),)
        flattened = (point,)

        return self._ApplyTypes_(409, 1, (VT_VARIANT, 0), magic, u"Str2Pt", None, *flattened)

    def str_2_pt_array(self, points):

        magic = ((VT_BSTR, 1),)
        flattened = (points,)

        return self._ApplyTypes_(410, 1, (VT_VARIANT, 0), magic, u"Str2PtArray", None, *flattened)

    def strtok(self, text, delimiters):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (text, delimiters)

        return self._ApplyTypes_(250, 1, (VT_VARIANT, 0), magic, u"Strtok", None, *flattened)

    def text_out(self, text, title):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (text, title)

        return self._ApplyTypes_(755, 1, (VT_VARIANT, 0), magic, u"TextOut", None, *flattened)

    def version(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(288, 1, (VT_VARIANT, 0), magic, u"Version", None, *flattened)

    def add_named_c_plane(self, name, view):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (name, view)

        return self._ApplyTypes_(280, 1, (VT_VARIANT, 0), magic, u"AddNamedCPlane", None, *flattened)

    def add_named_view(self, name, view):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (name, view)

        return self._ApplyTypes_(281, 1, (VT_VARIANT, 0), magic, u"AddNamedView", None, *flattened)

    def background_bitmap(self, view, file_name, point, width):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_R8, 1))
        flattened = (view, file_name, flatten_params(point), width)

        return self._ApplyTypes_(780, 1, (VT_VARIANT, 0), magic, u"BackgroundBitmap", None, *flattened)

    def current_detail(self, layout, detail, return_names):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (layout, detail, return_names)

        return self._ApplyTypes_(923, 1, (VT_VARIANT, 0), magic, u"CurrentDetail", None, *flattened)

    def current_view(self, view, return_name):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, return_name)

        return self._ApplyTypes_(251, 1, (VT_VARIANT, 0), magic, u"CurrentView", None, *flattened)

    def delete_named_c_plane(self, name):

        magic = ((VT_BSTR, 1),)
        flattened = (name,)

        return self._ApplyTypes_(284, 1, (VT_VARIANT, 0), magic, u"DeleteNamedCPlane", None, *flattened)

    def delete_named_view(self, name):

        magic = ((VT_BSTR, 1),)
        flattened = (name,)

        return self._ApplyTypes_(285, 1, (VT_VARIANT, 0), magic, u"DeleteNamedView", None, *flattened)

    def detail_names(self, layout, return_names):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (layout, return_names)

        return self._ApplyTypes_(922, 1, (VT_VARIANT, 0), magic, u"DetailNames", None, *flattened)

    def is_background_bitmap(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(779, 1, (VT_VARIANT, 0), magic, u"IsBackgroundBitmap", None, *flattened)

    def is_detail(self, layout, detail):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (layout, detail)

        return self._ApplyTypes_(921, 1, (VT_VARIANT, 0), magic, u"IsDetail", None, *flattened)

    def is_layout(self, layout):

        magic = ((VT_BSTR, 1),)
        flattened = (layout,)

        return self._ApplyTypes_(920, 1, (VT_VARIANT, 0), magic, u"IsLayout", None, *flattened)

    def is_view(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(252, 1, (VT_VARIANT, 0), magic, u"IsView", None, *flattened)

    def is_view_current(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(253, 1, (VT_VARIANT, 0), magic, u"IsViewCurrent", None, *flattened)

    def is_view_maximized(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(254, 1, (VT_VARIANT, 0), magic, u"IsViewMaximized", None, *flattened)

    def is_view_perspective(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(255, 1, (VT_VARIANT, 0), magic, u"IsViewPerspective", None, *flattened)

    def is_view_title_visible(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(256, 1, (VT_VARIANT, 0), magic, u"IsViewTitleVisible", None, *flattened)

    def is_wallpaper(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(531, 1, (VT_VARIANT, 0), magic, u"IsWallpaper", None, *flattened)

    def maximize_restore_view(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(257, 1, (VT_VARIANT, 0), magic, u"MaximizeRestoreView", None, *flattened)

    def named_c_plane(self, name):

        magic = ((VT_BSTR, 1),)
        flattened = (name,)

        return self._ApplyTypes_(286, 1, (VT_VARIANT, 0), magic, u"NamedCPlane", None, *flattened)

    def named_c_planes(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(258, 1, (VT_VARIANT, 0), magic, u"NamedCPlanes", None, *flattened)

    def named_views(self):

        magic = ()
        flattened = ()

        return self._ApplyTypes_(259, 1, (VT_VARIANT, 0), magic, u"NamedViews", None, *flattened)

    def rename_view(self, old_title, new_title):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (old_title, new_title)

        return self._ApplyTypes_(260, 1, (VT_VARIANT, 0), magic, u"RenameView", None, *flattened)

    def restore_named_c_plane(self, name, view):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (name, view)

        return self._ApplyTypes_(282, 1, (VT_VARIANT, 0), magic, u"RestoreNamedCPlane", None, *flattened)

    def restore_named_view(self, name, view, restore_bitmap):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (name, view, restore_bitmap)

        return self._ApplyTypes_(283, 1, (VT_VARIANT, 0), magic, u"RestoreNamedView", None, *flattened)

    def rotate_camera(self, view, direction, angle):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1))
        flattened = (view, direction, angle)

        return self._ApplyTypes_(519, 1, (VT_VARIANT, 0), magic, u"RotateCamera", None, *flattened)

    def rotate_view(self, view, direction, angle):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1))
        flattened = (view, direction, angle)

        return self._ApplyTypes_(650, 1, (VT_VARIANT, 0), magic, u"RotateView", None, *flattened)

    def show_grid(self, view, show):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, show)

        return self._ApplyTypes_(738, 1, (VT_VARIANT, 0), magic, u"ShowGrid", None, *flattened)

    def show_grid_axes(self, view, show):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, show)

        return self._ApplyTypes_(739, 1, (VT_VARIANT, 0), magic, u"ShowGridAxes", None, *flattened)

    def show_view_title(self, view, state):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, state)

        return self._ApplyTypes_(261, 1, (VT_VARIANT, 0), magic, u"ShowViewTitle", None, *flattened)

    def show_world_axes(self, view, show):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, show)

        return self._ApplyTypes_(740, 1, (VT_VARIANT, 0), magic, u"ShowWorldAxes", None, *flattened)

    def synchronize_c_planes(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(289, 1, (VT_VARIANT, 0), magic, u"SynchronizeCPlanes", None, *flattened)

    def tilt_view(self, view, direction, angle):

        magic = ((VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1))
        flattened = (view, direction, angle)

        return self._ApplyTypes_(518, 1, (VT_VARIANT, 0), magic, u"TiltView", None, *flattened)

    def view_c_plane(self, view, plane):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (view, flatten_params(plane))

        return self._ApplyTypes_(264, 1, (VT_VARIANT, 0), magic, u"ViewCPlane", None, *flattened)

    def view_camera(self, view, camera):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (view, flatten_params(camera))

        return self._ApplyTypes_(394, 1, (VT_VARIANT, 0), magic, u"ViewCamera", None, *flattened)

    def view_camera_lens(self, view, length):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (view, length)

        return self._ApplyTypes_(262, 1, (VT_VARIANT, 0), magic, u"ViewCameraLens", None, *flattened)

    def view_camera_plane(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(778, 1, (VT_VARIANT, 0), magic, u"ViewCameraPlane", None, *flattened)

    def view_camera_target(self, view, camera, target):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (view, flatten_params(camera), flatten_params(target))

        return self._ApplyTypes_(263, 1, (VT_VARIANT, 0), magic, u"ViewCameraTarget", None, *flattened)

    def view_camera_up(self, view, up_vector):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (view, flatten_params(up_vector))

        return self._ApplyTypes_(517, 1, (VT_VARIANT, 0), magic, u"ViewCameraUp", None, *flattened)

    def view_display_mode(self, view, mode):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (view, mode)

        return self._ApplyTypes_(290, 1, (VT_VARIANT, 0), magic, u"ViewDisplayMode", None, *flattened)

    def view_display_mode_ex(self, view, mode, return_names):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, mode, return_names)

        return self._ApplyTypes_(910, 1, (VT_VARIANT, 0), magic, u"ViewDisplayModeEx", None, *flattened)

    def view_display_mode_name(self, mode):

        magic = ((VT_BSTR, 1),)
        flattened = (mode,)

        return self._ApplyTypes_(909, 1, (VT_VARIANT, 0), magic, u"ViewDisplayModeName", None, *flattened)

    def view_display_modes(self, return_name):

        magic = ((VT_BOOL, 1),)
        flattened = (return_name,)

        return self._ApplyTypes_(908, 1, (VT_VARIANT, 0), magic, u"ViewDisplayModes", None, *flattened)

    def view_names(self, return_names, type):

        magic = ((VT_BOOL, 1), (VT_I2, 1))
        flattened = (return_names, type)

        return self._ApplyTypes_(265, 1, (VT_VARIANT, 0), magic, u"ViewNames", None, *flattened)

    def view_near_corners(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(823, 1, (VT_VARIANT, 0), magic, u"ViewNearCorners", None, *flattened)

    def view_projection(self, view, mode):

        magic = ((VT_BSTR, 1), (VT_I2, 1))
        flattened = (view, mode)

        return self._ApplyTypes_(266, 1, (VT_VARIANT, 0), magic, u"ViewProjection", None, *flattened)

    def view_radius(self, view, radius):

        magic = ((VT_BSTR, 1), (VT_R8, 1))
        flattened = (view, radius)

        return self._ApplyTypes_(824, 1, (VT_VARIANT, 0), magic, u"ViewRadius", None, *flattened)

    def view_size(self, view):

        magic = ((VT_BSTR, 1),)
        flattened = (view,)

        return self._ApplyTypes_(267, 1, (VT_VARIANT, 0), magic, u"ViewSize", None, *flattened)

    def view_target(self, view, target):

        magic = ((VT_BSTR, 1), (VT_ARRAY + VT_R8, 1))
        flattened = (view, flatten_params(target))

        return self._ApplyTypes_(395, 1, (VT_VARIANT, 0), magic, u"ViewTarget", None, *flattened)

    def view_title(self, mode):

        magic = ((VT_BSTR, 1),)
        flattened = (mode,)

        return self._ApplyTypes_(907, 1, (VT_VARIANT, 0), magic, u"ViewTitle", None, *flattened)

    def wallpaper(self, view, file_name):

        magic = ((VT_BSTR, 1), (VT_BSTR, 1))
        flattened = (view, file_name)

        return self._ApplyTypes_(532, 1, (VT_VARIANT, 0), magic, u"Wallpaper", None, *flattened)

    def wallpaper_gray_scale(self, view, gray_scale):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, gray_scale)

        return self._ApplyTypes_(534, 1, (VT_VARIANT, 0), magic, u"WallpaperGrayScale", None, *flattened)

    def wallpaper_hidden(self, view, hidden):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, hidden)

        return self._ApplyTypes_(533, 1, (VT_VARIANT, 0), magic, u"WallpaperHidden", None, *flattened)

    def zoom_bounding_box(self, corners, view, all):

        magic = ((VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (flatten_params(corners), view, all)

        return self._ApplyTypes_(479, 1, (VT_VARIANT, 0), magic, u"ZoomBoundingBox", None, *flattened)

    def zoom_extents(self, view, all):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, all)

        return self._ApplyTypes_(375, 1, (VT_VARIANT, 0), magic, u"ZoomExtents", None, *flattened)

    def zoom_selected(self, view, all):

        magic = ((VT_BSTR, 1), (VT_BOOL, 1))
        flattened = (view, all)

        return self._ApplyTypes_(376, 1, (VT_VARIANT, 0), magic, u"ZoomSelected", None, *flattened)


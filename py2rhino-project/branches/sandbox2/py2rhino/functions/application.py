# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_alias(alias, macro):

    return _rsf.add_alias(alias, macro)

def add_search_path(folder, index=pythoncom.Empty):

    return _rsf.add_search_path(folder, index)

def add_startup_script(script_file, index=pythoncom.Empty):

    return _rsf.add_startup_script(script_file, index)

def alias_count():

    return _rsf.alias_count()

def alias_macro(alias, macro=pythoncom.Empty):

    return _rsf.alias_macro(alias, macro)

def alias_names():

    return _rsf.alias_names()

def appearance_color(item, color=pythoncom.Empty):

    return _rsf.appearance_color(item, color)

def appearance_display(item, show=pythoncom.Empty):

    return _rsf.appearance_display(item, show)

def autosave_file(file=pythoncom.Empty):

    return _rsf.autosave_file(file)

def autosave_interval(minutes=pythoncom.Empty):

    return _rsf.autosave_interval(minutes)

def build_date():

    return _rsf.build_date()

def clear_command_history():

    return _rsf.clear_command_history()

def command(command, echo=pythoncom.Empty):

    return _rsf.command(command, echo)

def command_history():

    return _rsf.command_history()

def default_renderer(renderer=pythoncom.Empty):

    return _rsf.default_renderer(renderer)

def delete_alias(alias):

    return _rsf.delete_alias(alias)

def delete_search_path(folder):

    return _rsf.delete_search_path(folder)

def delete_startup_script(script_file):

    return _rsf.delete_startup_script(script_file)

def display_ole_alerts(display):

    return _rsf.display_ole_alerts(display)

def edge_analysis_color(color=pythoncom.Empty):

    return _rsf.edge_analysis_color(color)

def edge_analysis_mode(mode=pythoncom.Empty):

    return _rsf.edge_analysis_mode(mode)

def enable_autosave(enable=pythoncom.Empty):

    return _rsf.enable_autosave(enable)

def enable_history_recording(enable=pythoncom.Empty):

    return _rsf.enable_history_recording(enable)

def exe_folder():

    return _rsf.exe_folder()

def exit():

    return _rsf.exit()

def find_file(filename):

    return _rsf.find_file(filename)

def get_plug_in_object(plug_in):

    return _rsf.get_plug_in_object(plug_in)

def help(topic=pythoncom.Empty):

    return _rsf.help(topic)

def in_command(ignore_runners=pythoncom.Empty):

    return _rsf.in_command(ignore_runners)

def install_folder():

    return _rsf.install_folder()

def is_alias(alias):

    return _rsf.is_alias(alias)

def is_command(command_name):

    return _rsf.is_command(command_name)

def last_command_name():

    return _rsf.last_command_name()

def last_command_result():

    return _rsf.last_command_result()

def last_loaded_script_file():

    return _rsf.last_loaded_script_file()

def locale_i_d():

    return _rsf.locale_i_d()

def ortho(enable=pythoncom.Empty):

    return _rsf.ortho(enable)

def osnap(enable=pythoncom.Empty):

    return _rsf.osnap(enable)

def osnap_dialog(visible=pythoncom.Empty):

    return _rsf.osnap_dialog(visible)

def osnap_mode(mode=pythoncom.Empty):

    return _rsf.osnap_mode(mode)

def planar(enable=pythoncom.Empty):

    return _rsf.planar(enable)

def plug_ins(types=pythoncom.Empty, status=pythoncom.Empty):

    return _rsf.plug_ins(types, status)

def print_(message=pythoncom.Empty):

    return _rsf.print_(message)

def print_ex(message=pythoncom.Empty):

    return _rsf.print_ex(message)

def project_osnaps(enable=pythoncom.Empty):

    return _rsf.project_osnaps(enable)

def prompt(prompt=pythoncom.Empty):

    return _rsf.prompt(prompt)

def registry_key():

    return _rsf.registry_key()

def screen_size():

    return _rsf.screen_size()

def sdk_version():

    return _rsf.sdk_version()

def search_path_count():

    return _rsf.search_path_count()

def search_path_list():

    return _rsf.search_path_list()

def send_keystrokes(keys=pythoncom.Empty, add_return=pythoncom.Empty):

    return _rsf.send_keystrokes(keys, add_return)

def snap(enable=pythoncom.Empty):

    return _rsf.snap(enable)

def startup_script_count():

    return _rsf.startup_script_count()

def startup_script_list():

    return _rsf.startup_script_list()

def status_bar_distance(distance=pythoncom.Empty):

    return _rsf.status_bar_distance(distance)

def status_bar_message(message=pythoncom.Empty):

    return _rsf.status_bar_message(message)

def status_bar_number(number=pythoncom.Empty):

    return _rsf.status_bar_number(number)

def status_bar_point(point=pythoncom.Empty):

    return _rsf.status_bar_point(point)

def template_file(filename=pythoncom.Empty):

    return _rsf.template_file(filename)

def template_folder(folder=pythoncom.Empty):

    return _rsf.template_folder(folder)

def window_handle():

    return _rsf.window_handle()

def working_folder(enable=pythoncom.Empty):

    return _rsf.working_folder(enable)


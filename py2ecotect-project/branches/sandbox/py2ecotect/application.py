import py2ecotect
from py2ecotect import StringUtil

def activate():
    """
    
    Displays the main ECOTECT window and brings it to the front if it is behind 
    any other windows.
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    py2ecotect.conversation.Exec("app.activate")
    
    
def alert(msg, type = ""):
    """
    
    Displays a popup message box displaying the given message and an OK button. 
    You can change the different icons and titles displayed in the dialog using 
    the info, question, warning or error suffixes.
    
    Parameter(s)
    This command takes the following parameters.
    
    type
    If you want an alert dialog, enter "". Otherwise enter info, question, 
    warning or error

    msg 
    A string containing the message to be displayed.
    
    """
    arg_str = StringUtil._convert_args_to_string("app.alert." + type, msg)
    py2ecotect.conversation.Exec(arg_str)
    
def busy(action, message):
    """
    
    Controls the display of the 'Application Busy' dialog box. Use this dialog
    during a complex calculation whose progress is not linear or unsuitable for 
    using the standard progress bar. 

    Parameter(s)
    This command takes the following parameters.

    action 
    This first parameter gives the required action. The open action opens the 
    dialog box and displays the static message provided. The update action 
    refreshes the dynamic message line displayed immediately beneath the static 
    message and is used to keep the user informed of progress. The close action 
    closes and hides the busy dialog. 

    message 
    This parameter provides the message to be displayed within the busy dialog. 
    When used with the open action, the message becomes the static title 
    displayed in bold in the centre. When used with the update action, this 
    parameters is used as the dynamic message line displayed immediately beneath 
    the static message. This parameter is ignored when using the close action. 
    
    """
    arg_str = StringUtil._convert_args_to_string("app.busy" + action, message)
    py2ecotect.conversation.Exec(arg_str)

def center():
    """
    
    Use this command to centre the main Ecotect window withing the current 
    desktop. Its size will remain the same, it will simply move into the centre 
    of the screen. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    py2ecotect.conversation.Exec("app.center")
    
def character(text):
    """   
    
    Use this command to send a stream of characters to the currently focused 
    control. The text parameter is simply a string of characters. Note: this is 
    very experimental and will need to be used in conjunction with the 
    app.mouseevent or app.keyevent commands to first select the required 
    control. 
    
    Parameter(s)
    This command takes the following parameters.

    text 
    A string of characters that are to be 'typed' or sent to the currently 
    selected control. 
    
    """
    arg_str = StringUtil._convert_args_to_string("app.character", text)
    py2ecotect.conversation.Exec(arg_str)

def exit():
    """
    
    This function causes the instance of Ecotect running the script to exit, 
    just as if you had manualy chosen the > Exit menu item. You will need to 
    be careful using this command as it may automatically save any changes you 
    have made to the current model unless you use the model.new function first.
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    py2ecotect.conversation.Exec("app.exit")

def key(keyCode):
    """
    
    Use this command to emulate virtual keyboard events in the currently active 
    window or control. With this command you can simulate TAB and control keys. 
    The key parameter is the virtual key code of the key to be pressed, as 
    given in the following table.
    
    Important Note: Keyboard events are generated directly using the keyboard 
    interrupt, which are then sent to the target application via the Windows 
    message queue. Thus, you must give the program time to complete any tasks 
    that may result from each keystroke. If not, the application may miss the 
    next command and hang the script, meaning that you will have to 
    disconnect/reconnect.
    
    To overcome this, use the Script Manager pause(msec) command immediately 
    after such a keystroke or slow down the execution speed of the script using 
    the script("delay 1000"); command immediately prior to the keystroke. 

    Parameter(s)
    This command takes the following parameters.

    keyCode 
    A value specifying the key code to emulate. Some example values are given 
    in the following table. 
    
    Relevant Data Table(s)
    
    Virtual Key Codes 
    Key Code Value
    VK_CANCEL 3  
    VK_PRINT 42 
    VK_BACK 8  
    VK_EXECUTE 43 
    VK_TAB 9  
    VK_SNAPSHOT 44 
    VK_CLEAR 12  
    VK_INSERT 45 
    VK_RETURN 13  
    VK_DELETE 46 
    VK_SHIFT 16  
    VK_HELP 47 
    VK_CONTROL 17  
    VK_SLEEP 95 
    VK_MENU 18  
    VK_F1 112 
    VK_PAUSE 19  
    VK_F2 113 
    VK_CAPITAL 20  
    VK_F3 114 
    VK_ESCAPE 27  
    VK_F4 115 
    VK_SPACE 32  
    VK_F5 116 
    VK_PRIOR 33  
    VK_F6 117 
    VK_NEXT 34  
    VK_F7 118 
    VK_END 35  
    VK_F8 119 
    VK_HOME 36  
    VK_F9 120 
    VK_LEFT 37  
    VK_F10 121 
    VK_UP 38  
    VK_F11 122 
    VK_RIGHT 39  
    VK_F12 123 
    VK_DOWN 40  
    VK_NUMLOCK 144 
    VK_SELECT 41  
    VK_SCROLL 145 
    
    """
    arg_str = StringUtil._convert_args_to_string("app.key", keyCode)
    py2py2ecotect.conversation.Exec(arg_str)


def maximise(state = 1):
    """
    
    Maximises ECOTECT to fill the entire screen. This can be useful if you need 
    to give an animated presentation or run a demonstration script. 
    
    Parameter(s)
    This command takes the following parameters.

    state 
    An optional parameter that determines whether the application is maximised 
    or restored to its previous state (true to maximise, false to restore). If 
    not given, the command toggles between maximised and normal. This is a 
    boolean value where 1 or true represents the affirmative and 0 or false 
    the negative.
    
    Here is an example:
    
    >>> maximise(1)
    
    """

    arg_str = StringUtil._convert_args_to_string("app.maximise", state)
    py2ecotect.conversation.Exec(arg_str)
    
def menu(command, tag = 0):
    """
    
    This command is a special method to send interactive commands to the 
    ECOTECT application. These are very different from other methods in that 
    they allow you to emulate interactive menu commands and actions. This is 
    useful for direct command line entry and accessing some functions not 
    otherwise available, however you will need to be very careful that you do 
    not include commands that invoke dialog boxes or on-screen prompts if you 
    intend your script to operate unattended.
    
    Parameter(s)
    This command takes the following parameters.

    command 
    The command parameter can be given as either a value or a token selected 
    from the following table. In this case, tokens must be entered in full. 
    
    tag 
    The tag parameter defaults to zero if it is not given and is included 
    mainly for future extensions.
    
    Relevant Data Table(s)
    
    Available Menu Commands 
    
    File Menu 
        file.new 
        file.new.window 
        file.open 
        file.recentfiles 
        file.revert 
        file.save 
        file.saveas 
        file.import.3d 
        file.import 
        file.export.data 
        file.export.external 
        file.export.image 
        file.export 
        file.print.setup 
        file.print 
        file.projectinfo 
        file.preferences 
        file.exit 
        
    Misc File Commands 
        save.results 
        save.grid 
        import.grid 
        export.wrl 
        export.rad 
        export.pov 
        export.dxf 
        export.htb2 
        export.idf 
        export.doe 
        export.sbem 
        export.winair 
        export.fds 
        export.espr 
        export.gbxml
         
    Edit Menu 
        edit.undo 
        edit.repeat 
        edit.redo 
        edit.cut 
        edit.copy 
        edit.paste 
        edit.delete 
        edit.duplicate 
        edit.morph 
        edit.facet 
        edit.offset 
        edit.no.linking 
        edit.no.undo 
        edit.link 
        edit.unlink 
        edit.fix 
        edit.ungroup 
        edit.group 
        
    View Menu 
        view.undo 
        view.set 
        view.plan 
        view.side 
        view.front 
        view.persp 
        view.axon 
        view.zoom.win 
        view.zoom.obj 
        view.zoom.all 
        view.fit.grid 
        view.drag.grid 
        view.context 
        view.copy.bmp 
        view.copy.emf 
        view.copy 
        view.save 
        view.bitmap.show 
        view.bitmap 
        view.recall 
        view.store 
        view.edit 
    Select Menu 
        select.mode 
        select.polar 
        select.measure 
        select.all 
        select.none 
        select.invert 
        select.cells 
        select.adjacent 
        select.previous 
        select.children 
        select.parent 
        select.zone.no 
        select.by.zone 
        select.by.index 
        select.by.material 
        select.by.element 
        select.by.schedule 
        select.by.orientation 
        
    Modify Menu 
        modify.moveto.zone 
        modify.moveto.current 
        modify.xform.move 
        modify.xform.rotate 
        modify.xform.scale 
        modify.xform.mirror 
        modify.xform.extrude 
        modify.xform.vectors 
        modify.xform.cap 
        modify.xform.panel 
        modify.origin.global 
        modify.origin.selection 
        modify.origin.centre 
        modify.origin.reset 
        modify.origin.xform 
        modify.assign.shaded 
        modify.assign.reflector 
        modify.assign.acoustic 
        modify.assign.source 
        modify.cut.assign 
        modify.cut.extend 
        modify.cut.trim 
        modify.insert.node 
        modify.edit.nodes 
        modify.delete.node 
        modify.child.extents 
        modify.render.poly 
        modify.reverse 
        modify.normals.unify 
        modify.normals.flip 
        modify.normals.orient 
        modify.create.lights 
        modify.nodes.float 
        modify.nodes.drop 
        modify.surface.grid 
        modify.subdivide.tiles 
        modify.subdivide.points 
        modify.subdivide.line 
        modify.simplify.count 
        modify.simplify.angle 
        modify.merge.triangles 
        modify.merge.polygons 
        modify.align.grid 
        modify.break 
        modify.intersect 
        modify.join 
        
    Draw Menu 
        draw.point 
        draw.line 
        draw.plane 
        draw.partion 
        draw.zone 
        draw.insert.child 
        draw.child.window 
        draw.child.void 
        draw.child.panel 
        draw.child.door 
        draw.light 
        draw.speaker 
        draw.appliance 
        draw.camera.objects 
        draw.camera.plan 
        draw.camera.windows 
        draw.camera.from 
        draw.camera.inside 
        draw.camera 
        draw.rect.plane 
        draw.rect.prism 
        draw.rect.zone 
        draw.arc 
        draw.bezier 
        draw.spline 
        draw.roof 
        
    Model Menu 
        model.location 
        model.inspector 
        model.zone.manager 
        model.elements 
        model.schedules 
        model.systems 
        model.settings 
        model.moveto.zone 
        model.moveto.current 
        model.make.current 
        model.zone.current 
        model.zone.selected 
        model.zone.all 
        model.zone.hide 
        model.zone.off 
        model.zone.lock 
        
    Display Menu 
        display.model 
        display.shadows 
        display.normals 
        display.sketch 
        display <value> 
        display.attr.1 
        display.attr.2 
        display.attr.3 
        display.attr.values 
        display.attr.numbers 
        display.attr.vectors 
        display.attr.colours 
        display.attr.scale 
        display.attr.properties 
        display.attr <value> 
        display.opengl 
        display.vrml 
        display.grid 
        display.rays 
        display.origin 
        display.bitmap 
        display.normal 
        display.detail.low 
        display.detail.partial 
        display.detail.full 
        display.detail.nodes 
        display.shadow.daily 
        display.shadow.annual 
        display.shadow.footprint 
        display.shadow.outlines 
        display.shadow.ground 
        display.shadow.reverse 
        display.shadow.cast 
        display.shadow.receive 
        display.shadow.selected 
        display.shadow.transparent 
        display.shadow.obstructions 
        display.shadow.reflections 
        display.shadow.shadows 
        display.rays.static 
        display.rays.coverage 
        display.rays.incidence 
        display.rays.particles 
        display.rays.rays 
        display.rays.forwards 
        display.rays.backwards 
        display.rays.cycle 
        display.rays.scale 
        display.rays.clear 
        display.grid.extents 
        display.grid.spacing 
        display.grid.autofit 
        display.grid.volumetric 
        display.grid.triangulate 
        display.grid.properties 
        
    Calculate Menu 
        calculate.volumes 
        calculate.adjacencies 
        calculate.shading.wizard 
        calculate.shading.extrude 
        calculate.shading.potential 
        calculate.shading.hourly 
        calculate.shading.annual 
        calculate.shading.monthly 
        calculate.shading.profile 
        calculate.shading.range 
        calculate.shading.rays 
        calculate.shading.project 
        calculate.shading.view 
        calculate.stereograph 
        calculate.solar.access 
        calculate.solar.exposure 
        calculate.lighting 
        calculate.rightotlight 
        calculate.photoelectric 
        calculate.autonomy 
        calculate.thermal 
        calculate.comfort 
        calculate.regs.uk 
        calculate.acoustic.rays 
        calculate.acoustic.reverb 
        calculate.acoustic.response 
        calculate.visibility 
        calculate.winds 
        calculate.resources 
        calculate.costs 
        calculate.errors 
        calculate.output 
        calculate.analysis.grid 
        calculate.weather 
        calculate.time 
        
    Tools Menu 
        tools.command 
        tools.clearfiles 
        tools.script 
        tools.wizard 
        tools.animation 
        tools.weather 
        tools.world.locations 
        tools.world.map 
        tools.analysis 
        tools.radiance 
        tools.lcaid 
        tools.edit 
        
    Help Menu 
        help.topics 
        help.howdoi 
        help.context 
        help.web.support 
        help.teaching.package 
        help.showarrow 
        help.registration 
        help.about 
        
    Context Menu 
        context.grid.nodes 
        context.grid.hide 
        context.grid.show 
        context.grid.extents 
        context.grid.spacing 
        context.node.type 
        context.node.smooth 
        context.line.render 
        
    Snap Menu 
        snap.none 
        snap.grid 
        snap.align 
        snap.ortho 
        snap.centre 
        snap.point 
        snap.midpt 
        snap.intersect 
        snap.line 
        snap.settings 
        snap <value> 
        
    Here is an example:
    
    >>> menu("file.export.external")
    
    """
    arg_str = StringUtil._convert_args_to_string("app.menu", command,tag)
    py2ecotect.conversation.Exec(arg_str)

def minimise(state = 1):
    """
    
    Minimises ECOTECT to the task bar. This can be useful if you have a long 
    calculation to perform within a script and want to use the computer for 
    other things while it runs.
    
    Parameter(s)
    This command takes the following parameters.

    state 
    An optional parameter that determines whether the application is minimised 
    or restored to its previous state (true to minimise, false to restore). 
    If not given, the command toggles between minimised and normal. This is a 
    boolean value where 1 or true represents the affirmative and 0 or false the 
    negative.
    
    Here is an example:
    
    >>> minimise(1)
    
    """

    arg_str = StringUtil._convert_args_to_string("app.minimise", state)
    py2ecotect.conversation.Exec(arg_str)

def mouseevent(action, x, y):
    """
    
    This is not a command for the faint hearted and is very experimental at 
    this stage (see below). It can be used to emulate user mouse actions. The 
    action tokens are given in the table below whereas the x and y values give 
    the position in screen pixels where the event is to take place, relative to 
    the top left corner of the main application window. If called from methods 
    in the graph, sunpath, opengl or view objects, the pixel values are 
    relative to the top left corner of the graphics canvas in each window.

    This command is actually a leftover from early versions of ECOTECT which 
    had a macro record and playback function. This function seemed to work 
    great - on the same machine - however the complexities of system metrics 
    and user preference settings for font and titlebar sizes was soon 
    discovered when macros were moved from machine to machine. However, when 
    used with care, this command can be so useful in a show-and-tell 
    demonstration on a known machine that I've left it in. Plus, it is 
    currently the only way of physically invoking context menus.
    
    Parameter(s)
    This command takes the following parameters.

    action 
    This parameter specifies the type of action/operation to use with the mouse 
    at the given screen location. See the following table for details. 
    
    x 
    Gives the horizontal X location of the desired mouse operation in pixel 
    coordinates relative to the left corner of the application window. 
    
    y 
    Gives the vertical Y location of the desired mouse operation in pixel 
    coordinates relative to the top corner of the application window.
    
    Relevant Data Table(s)
    
    Available Mouse Actions 
    Token     Description 
    move     move mouse to new position 
    lclick     Left mouse button clicked 
    ldown     Left mouse button pressed 
    lup     Left mouse button released 
    rclick     Right mouse button clicked 
    rdown     Right mouse button pressed 
    rup     Right mouse button released 
    mclick     Middle mouse button clicked 
    mdown     Middle mouse button pressed 
    mup     Middle mouse button released 
    wdown     Mouse wheel pressed 
    wup     Mouse wheel released 
    ldblclick     Left mouse button double-clicked 
    rdblclick     Right mouse button double-clicked 

    Here is an example:
    
    >>> mouseevent("rclick", 100, 150)
    
    """
    arg_str = StringUtil._convert_args_to_string("app.mouseevent", action, x, y)
    py2ecotect.conversation.Exec(arg_str)
 
def progress(percent):
    """
    
    Updates the progress indicator displayed in the application status bar. 

    Parameter(s)
    This command takes the following parameters.

    percent 
    This parameter gives the progress indicator value is given as either a 
    fraction (0-1) or a percentage (1-100). Any value greater than 1 is 
    interpreted as a percentage whereas any value between 0 and 1 as a fraction. 
    A value equal to or less than zero (0) hides the status bar. 
    
    Here is an example:
    
    >>> progress(25)
    
    """
    arg_str = StringUtil._convert_args_to_string("app.progress", percent)
    py2ecotect.conversation.Exec(arg_str)
    
def run(script):
    """
    
    This command instructs ECOTECT to run the specified script file. The 
    current script will pause whilst the new script is run, and will then 
    continue its own execution. If you are running a script from the Script 
    Manager, this command is useful as ECOTECT will run the new script itself, 
    significantly reducing the inter-process communication overhead. You can 
    also use the dofile() LUA command to execute a new script as part of an 
    existing one, however this is simply run as an extra command within the 
    current script environment. 

    Parameter(s)
    This command takes the following parameters.

    script 
    Gives the name of the script to run. If you do not give the full pathname 
    of file, ECOTECT will first search for it in the same directory as the 
    current script, then the current model, then the default model directory 
    and then in subfolders within the Square One installation directory.
    
    Here is an example:
    
    >>> run("AcousticRays.scr")
    
    """
    arg_str = StringUtil._convert_args_to_string("app.run", script)
    py2ecotect.conversation.Exec(arg_str)

def status(msg):
    """
    
    This function displays messages in the main application window's status bar.
    Sometimes you will see two messages in this area; the first specifying what
    action is taking place and the second in the status/progress area saying '
    Please wait...' or similar. To include both messages, simply separate 
    them with the '|' character. 

    Parameter(s)
    This command takes the following parameters.

    msg 
    This parameter gives the message to be displayed. If this message contains 
    the '|' character, it will be split with the first shown in the action area 
    and the second in the progress area. 
    
    Here is an example:
    
    >>> status("Reading zone data|Please wait...")
    
    """ 

    arg_str = StringUtil._convert_args_to_string("app.status", msg)
    py2ecotect.conversation.Exec(arg_str)

def get_computer():
    """
    
    Returns the system name of the computer the application is currently 
    running on. 

    Parameter(s)
    There are no parameters for this property.

    Return Value(s)
    Getting this property returns the following value(s).

    name 
    A text string containing the computer name. 
    
    """

    val = py2ecotect.conversation.Request("get.app.computer")
    return StringUtil._convert_str_to_type(val, str)

def get_image(type, name = None):
    """
    
    Creates an image of the specified item in the system $TEMP directory and 
    returns the pathname. This command is useful for embedding images in your 
    own HTML reports. 

    Parameter(s)
    This property takes the following parameters.

    type 
    Specify the type of image to create. See the following table for available 
    values for this parameter. 

    [name] 
    If not given, a pseudo-random unique filename will be used for the image. 
    If you provide a name, then this will be used. Either way, image files are 
    always in JPG format and generated within the system $TEMP directory. 
    This is to ensure that they can be saved and that the resulting directory 
    exists irrespective of which computer the script is run on. You can use the 
    'Save As' command within your browser to store a complete copy of the 
    resulting page along with it's images.
     
    Return Value(s)
    Getting this property returns the following value(s).

    imgPath 
    The full path to the image file in the $TEMP directory.
    
    Relevant Data Table(s)
    
    Application Image Types 
    Token # Description 
    view 0 The 3D EDITOR Page 
    opengl 1 The VISUALISE Page 
    sunpath 2 The current SunPath diagram 
    graph 3 The ANALYSIS graph 
    layers 4 The material layer image 
    schedule 5 The current schedule 

    """
    arg_str = StringUtil._convert_args_to_string("get.app.image", type, name)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, str)

def get_menu_tool(index):
    """
    Retrieve the user-defined tool data at the specified position within the 
    Tools menu. Use this command to check for an empty value before adding a 
    new user tool. 

    Parameter(s)
    This property takes the following parameters.

    index 
    An integer value between 1 and 9 representing the index of the user tool 
    required. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    name 
    The name of the item as it is displayed in the menu itself. 
    
    filepath 
    The full pathname to the associated executable file. 

    """
    arg_str = StringUtil._convert_args_to_string("get.app.menu.tool", index)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_list(val, str)  

def get_menu_wizard(index):
    """
    
    Retrieve the user-defined wizard data at the specified position within the 
    Draw > Geometry Wizards submenu. Use this command to check for an empty 
    value before adding a new user wizard. 

    Parameter(s)
    This property takes the following parameters.
    
    index 
    An integer value between 1 and 9 representing the index of the wizard 
    required. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    name 
    The name of the item as it is displayed in the menu itself. 
    
    filepath 
    The full pathname to the associated script file.
    
    """
    arg_str = StringUtil._convert_args_to_string("get.app.menu.wizard", index)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_list(val, str)  

def get_page():
    """
    
    Gets the currently active page in the ECOTECT application window. The 
    returned value will correspond to one of the items in the following table. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    page 
    The numerical index of the current application page. 
    
    Relevant Data Table(s)
    
    Available Application Pages 
    ID Description 
    0 PROJECT Page 
    1 3D EDITOR Page 
    2 VISUALISATION Page 
    3 ANALYSIS Page 
    4 REPORT Page 

    """
    val = py2ecotect.conversation.Request("get.app.page")
    return StringUtil._convert_str_to_type(val, int)

def set_page(page):
    """
    
    Sets the currently active page in the ECOTECT application window. These 
    correspond to the pages with tabs running down the far left side marked as 
    shown in the following table. 

    Parameter(s)
    This property takes the following parameters.

    page 
    The numerical index of the desired application page, as given in the 
    following table. 
    
    Relevant Data Table(s)
    
    Available Application Pages 
    ID Description 
    0 PROJECT Page 
    1 3D EDITOR Page 
    2 VISUALISATION Page 
    3 ANALYSIS Page 
    4 REPORT Page 

    """
    arg_str = StringUtil._convert_args_to_string("set.app.page", page)
    py2ecotect.conversation.Exec(arg_str)

def get_panel():
    """
    Gets the currently active panel in the ECOTECT application window. These 
    correspond to the tabbed panels on the right hand side of the window, as 
    shown in the following table. Getting this value returns the integer value 
    corresponding to each item in the table. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    panel 
    The numerical index of the current application panel. 
    
    Relevant Data Table(s)
    
    Available Application Panels 
    ID Description 
    0 Selection Information 
    1 Zone Management 
    2 Material Assignments 
    3 Display Settings 
    4 Visualisation Settings 
    5 Shadow Settings 
    6 Analysis Grid 
    7 Rays and Particles 
    8 Scripts and Wizards 
    9 Object Transformation 
    10 Export Manager 

    """
    val = py2ecotect.conversation.Request("get.app.panel")
    return StringUtil._convert_str_to_type(val, int)

def set_panel(panel):
    """
    Sets the currently active panel in the ECOTECT application window. These 
    correspond to the tabbed panels on the right hand side of the window, 
    as shown in the following table. 

    Parameter(s)
    This property takes the following parameters.
    
    panel 
    Either a string containing the panel token or the numerical index of the 
    desired application panel. 
    
    Relevant Data Table(s)
    
    Available Application 
    Panels ID Description 
    0 Selection Information 
    1 Zone Management 
    2 Material Assignments 
    3 Display Settings 
    4 Visualisation Settings 
    5 Shadow Settings 
    6 Analysis Grid 
    7 Rays and Particles 
    8 Scripts and Wizards 
    9 Object Transformation 
    10 Export Manager 

    """
    arg_str = StringUtil._convert_args_to_string("set.app.panel", panel)
    py2ecotect.conversation.Exec(arg_str)

def get_path():
    """
    
    Getting this property returns a single text string containing the 
    installation home directory of the ECOTECT application which, by default, 
    is usually 'C:\Program Files\Square One'. This can be useful if you need to 
    locate example or tutorial files in your script. This property is read only. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    path 
    A text string containing the full home directory path.
    
    """
    val = py2ecotect.conversation.Request("get.app.path")
    return StringUtil._convert_str_to_type(val, str)

def get_registry(key):
    """
    
    Use this property to retrieve values from the application's entry within 
    the Windows registry. Such values are stored on a per-user basic and this 
    property only allows access to values local to this application. In ECOTECT, 
    for example, this is located at HKEY_CURRENT_USER\Software\Square One\
    Ecotect\5.60. Registry entries are stored as a series of parameters in the 
    form 'key=value'. 

    Parameter(s)
    This property takes the following parameters.
    
    key 
    The name of an existing key stored in the application's registry entry.
     
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A text string containing the value, if any, associated with the given key.
    
    """
    arg_str = StringUtil._convert_args_to_string("get.app.registry", key)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, str)

def set_registry(keyvalue):
    """
    Use this property to set a value in the application's Windows registry 
    entry. Such values are stored on a per-user basic and this property only 
    allows access to values local to this application. In ECOTECT, for example, 
    this is located at HKEY_CURRENT_USER\Software\Square One\Ecotect\5.60. 
    Registry entries are stored as a series of parameters in the form 
    'key=value'. 

    Parameter(s)
    This property takes the following parameters.
    
    key=value 
    To set a value, you must include both the key name and the value to be set, separated by an equal '=' character. 
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A text string containing the value, if any, associated with the given key.
    
    """
    arg_str = StringUtil._convert_args_to_string("set.app.registry", keyvalue)
    py2ecotect.conversation.Exec(arg_str)
    
def get_screen():
    """
    
    Retrieve the position and size of the main Windows screen area. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    left 
    The position of the left side of the screen in pixels.
     
    top 
    The position of the top side of the screen in pixels.
     
    width 
    The horizontal width of the screen in pixels.
     
    height 
    The vertical height of the screen in pixels.
    
    """
    val = py2ecotect.conversation.Request("get.app.screen")
    return StringUtil._convert_str_to_list(val, int)  

def get_slider_range():
    """
    
    Retrieves the range of the main slider. The range defines the minimum and 
    maximum values over which the slider moves as well as other settings such 
    as the increment/decrement when using the arrow and PageUp/PageDown keys. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    min 
    The value when the slider is at its minimum.
     
    max 
    The value when the slider is at its maximum.
     
    freq 
    The frequency of indicator marks running along the bottom.
     
    lineSize 
    The increment/decrement value when using the arrow keys.
     
    pageSize 
    The increment/decrement value when using the PageUp/PageDown keys. 
    
    """
    val = py2ecotect.conversation.Request("get.app.slider.range")
    return StringUtil._convert_str_to_list(val, int)  

def set_slider_range(min, max, freq, lineSize, pageSize):
    """
    
    Sets the range of the main slider. The range defines the minimum and maximum 
    values over which the slider moves as well as other settings such as the 
    increment/decrement when using the arrow and PageUp/PageDown keys. 

    Parameter(s)
    This property takes the following parameters.
    
    min 
    The value when the slider is at its minimum. This value can be set to 
    anything as long as it is less than the 'max' parameter. 
    
    max 
    The value when the slider is at its maximum. This value can be set to 
    anything as long as it is greater than the 'min' parameter. 
    
    freq 
    The frequency of indicator marks running along the bottom. If this value is 
    set to zero (0) or less, it is ignored and the currently set value is used. 
    
    lineSize 
    The increment/decrement value when using the arrow keys. If this value is 
    set to zero (0) or less, it is ignored and the currently set value is used. 
    
    pageSize 
    The increment/decrement value when using the PageUp/PageDown keys. If this 
    value is set to zero (0) or less, it is ignored and the currently set value 
    is used. 
    
    """
    arg_str = StringUtil._convert_args_to_string("set.app.slider.range", 
                                                 min, max, freq, lineSize, 
                                                 pageSize)
    py2ecotect.conversation.Exec(arg_str)
    
def get_slider_scale():
    """
    
    Retrieves the current scale factor for the main slider and the hover-over 
    hint if it is set. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    scale 
    This scale factor is used to convert the range specfied in the app.slider.
    range setting to a user-readable value (see set.app.slider.scale). 
    
    [hint] 
    This is the popup hint you see when you move the mouse over the top of the 
    slider.
    
    """    
    val = py2ecotect.conversation.Request("get.app.slider.scale")
    return StringUtil._convert_str_to_list(val, float, str)
    
def set_slider_scale(scale, hint=None):
    """
    
    Sets the scale factor for the main slider and, optionally, the hover-over 
    hint value. 

    Parameter(s)
    This property takes the following parameters.
    
    scale 
    This scale factor is used to convert the range specfied in the app.slider.
    range setting to a user-readable value. For example, you may want to display 
    values in percent, but want higher accuracy on the slider values. In this 
    case, you can set range.min=0, range.max=1000, range.freq=1 and then the 
    scale to 0.1. 
    
    [hint] 
    By including this optional value, you can set the hover-over hint for the 
    slider when you move the mouse over the top of it.
    
    """    
    arg_str = StringUtil._convert_args_to_string("set.app.slider.scale", scale, 
                                                 hint)
    py2ecotect.conversation.Exec(arg_str)

def get_slider_title():
    """
    
    Retrieves the current title displayed on the main slider. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    title 
    This is a string value containing the full title.
    
    """
    val = py2ecotect.conversation.Request("get.app.slider.title")
    return StringUtil._convert_str_to_type(val, str)

def set_slider_title(title):
    """
    
    Sets the title to be displayed on the main slider. 

    Parameter(s)
    This property takes the following parameters.
    
    title 
    This is a string value containing the full title.
    
    """
    
    arg_str = StringUtil._convert_args_to_string("set.app.slider.title", title)
    py2ecotect.conversation.Exec(arg_str)

def get_username():
    """
    
    Returns the login name of the currently logged in user on the computer 
    running ECOTECT. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    name 
    A string value containing the user's login name.
    
    """
    val = py2ecotect.conversation.Request("get.app.username")
    return StringUtil._convert_str_to_type(val, str)

def get_web_file(url):
    """
    
    Retrieve the contents of the specified web URL from the internet and stores 
    it as a temporary file on your local hard disk. You must be responsible for 
    cleaning up these files using the remove() command or manually using the 
    Tools >: Clear Temporary File... menu item. 

    Parameter(s)
    This property takes the following parameters.
    
    url 
    The full Universal Resource Locator (URL) of the web page or CGI script you 
    want to retrieve. If you need to send parameters, use the standard 
    'url?key1=value1&key2=value2' format. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    tmpfile 
    The full pathname of the temporary file used to store the downloaded 
    contents. The script will return an error if the download failes.
    
    """
    arg_str = StringUtil._convert_args_to_string("get.app.web.file", url)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, str)

def get_web_line(lineNumber):
    """
    
    Retrieve individual lines of text from the last call to get.web.page.text. 
    There is obviously a limit to the amount of text you can transfer, so it is 
    usually safest to retrieve web text line-by-line. However, if you know the 
    that returned text will be relatively small, you can use a line number of -1 
    to retrieve all the text at once. 

    Parameter(s)
    This property takes the following parameters.
    
    lineNumber 
    The line number to retrieve. You can get the number of lines using get.web.
    lines, the raw text results will have 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A text string containing the value, if any, associated with the given key.
    
    """
    arg_str = StringUtil._convert_args_to_string("get.app.web.line", lineNumber)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, str)

def set_web_login(username = None, password = None):
    """
    
    Many websites require a login name and password in order to authenticate 
    individual users. Use this property before you request your page to set 
    both of these. You should consider using the getUserInput() function rather 
    than hard-coding passwords within your scripts.

    To clear a previously set username and password, call this property with no 
    parameters. 
    
    Parameter(s)
    This property takes the following parameters.
    
    [username] 
    The user name you require to login.
     
    [password] 
    The password you require to login.
    
    """
    arg_str = StringUtil._convert_args_to_string("set.app.web.login", username, 
                                                 password)
    py2ecotect.conversation.Exec(arg_str)

def get_web_page(url, text = False):
    """
    
    Retrieve the contents of the specified web URL from the internet if you 
    have access. As many web-based CGI scripts return a series of parameters 
    in the form 'key=value', by default the downloaded results are parsed into 
    a series of parameter pairs and can be accessed using the get.web.param 
    property. If the url you are accessing returns normal text or some other 
    data format, append the suffix '.text' to avoid the parsing process and 
    access the data using the get.web.line properties. 

    Parameter(s)
    This property takes the following parameters.
    
    url 
    The full Universal Resource Locator (URL) of the web page or CGI script you 
    want to retrieve. If you need to send parameters, use the standard 
    'url?key1=value1&key2=value2' format.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    result 
    The number of parameters parsed or, if just text, the number lines 
    downloaded from the web. For success, this value must be at least 1.
    
    """
    if text:
        arg_str = StringUtil._convert_args_to_string("get.app.web.page.text", url)
    else:
        arg_str = StringUtil._convert_args_to_string("get.app.web.page", url)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, int)

def get_web_param(name = None, index = None):
    """
    
    Many web-based CGI scripts return a series of parameters in the form 
    'key=value'. After you have used the get.web.page property, use this to 
    retrieve any value associated with a particular key. 

    Parameter(s)
    This property takes the following parameters.
    
    name 
    The name of the key returned by the web-based CGI script.
     
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A text string containing the value, if any, associated with the given key. 
    
    Many web-based CGI scripts return a series of parameters in the form 
    'key=value'. If you don't know the names of all the keys, you can use 
    the index of each one to retrieve them. You can only do this after you have 
    used the get.web.page property and stored the number of parameters parsed. 
    
    Parameter(s)
    This property takes the following parameters.
    
    index 
    The integer index of key=value pair to retrieve.
     
    Return Value(s)
    Getting this property returns the following value(s).
    
    key 
    A text string containing the key name.
     
    value 
    A text string containing the value, if any, associated with that key. 
    
    """
    if name:
        arg_str = StringUtil._convert_args_to_string("get.app.web.param", name)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, str)
    elif index:
        arg_str = StringUtil._convert_args_to_string("get.app.web.param.index", 
                                                     index)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, str)

def get_window():
    """
    
    Retrieve the position and size of the main ECOTECT window displayed within 
    your screen. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    left 
    The position of the left side of the window in screen pixels. 
    
    top 
    The position of the top side of the window in screen pixels. 
    
    width 
    The horizontal width of the window in screen pixels. 
    
    height 
    The vertical height of the window in screen pixels.
    
    """
    val = py2ecotect.conversation.Request("get.app.window")
    return StringUtil._convert_str_to_list(val, int)

def set_window(left, top, width, height):
    """
    
    Sets the position and size of the main ECOTECT window displayed within your 
    screen. 

    Parameter(s)
    This property takes the following parameters.
    
    left 
    The position of the left side of the window in screen pixels. If this value 
    is less than zero, the left side of the window will not be changed. 
    
    top 
    The position of the top side of the window in screen pixels. If this value 
    is less than zero, the top of the window will not be changed. 
    
    width 
    The horizontal width of the window in screen pixels. This parameter is 
    optional - if not given or less than zero the width of the window will not 
    be changed. 
    
    height 
    The vertical height of the window in screen pixels. This parameter is 
    optional - if not given or less than zero the height of the window will not 
    be changed.
    
    """
    arg_str = StringUtil._convert_args_to_string("set.app.window", left, 
                                                 top, 
                                                 width, 
                                                 height)
    py2ecotect.conversation.Exec(arg_str)



if __name__ == "__main__":
        #activate()
        alert("Bye",  "warning")
        #busy("open","BUSY")
        #center()
        #character("HHH")
        #exit()
        #key(144)
        #maximise(0)
        #menu("file.export.external")
        #minimise(0)
        #mouseevent("rclick", 100, 150)
        #progress(25)
        #run("AcousticRays.scr")
        #status("Reading zone data|Please wait...")
        #print get_computer()
        #print get_image(0, "MyImage12.jpg")
        #print get_menu_tool(7) 
        #print get_page()
        #set_page(1)
        #print get_panel()
        #set_panel(9)
        #print get_path()
        #print get_screen()
        #get_slider_range()
        #set_slider_range(-180, 180, 15, 1, 30)
        #print get_slider_scale()
        #print get_slider_title()
        #set_slider_title("BYE!!")
        #print get_username()
        #print get_web_file("http://squ1.org/example.cgi?type=ModelData")
        #print get_web_line("9")
        #print get_web_page("http://squ1.org/exampleData?type=wea")
        #print get_window()
        #set_window(50, 25, 640, 480)
        print "Tests completed"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
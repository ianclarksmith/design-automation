popup_menu = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "PopupMenu",
    "output_package_name": "user_interface",
    "output_module_name": "popup_menu",

    "doc_html": """
        Displays a user-defined, context-style popup menu. The popup menu can appear almost anywhere. And, it can be dismissed by either clicking the left or right mouse buttons.
    """,

    "syntax_html": {
        0: ("arrItems", "arrModes", "arrPoint", "strView"),
    },

    "params_html": {
        0: {
            "name": "arrItems",
            "py_name": "items",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Items",
            "doc": """
        An array of string representing the menu items. An empty string, or "", will create a menu separator item.
            """
        },
        1: {
            "name": "arrModes",
            "py_name": "modes",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_int",
            "name_main": "Modes",
            "doc": """
        A array if numbers identifying the display mode of the corresponding menu items. If omitted, all menu items are enabled. Note, display modes are ignored for menu separators. The display modes are a follows:
		0
		The menu item is enabled.
		1
		The menu item is disabled.
		2
		The menu item is checked.
		3
            """
        },
        2: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point where the menu item is to appear. If omitted, the menu item will appear at the current cursor position.
            """
        },
        3: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        If arrPoint is specified, the strView is the view in which the menu is to appear. If arrPoint is specified but strView is omitted, then the menu will be displayed in the active view.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The index of the menu item that was picked."
        },
        1: {
            "type": "number",
            "doc": "-1 if no menu item is picked."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 595,

    "params_com": {
        0: {
            "name": "vaItems",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaModes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


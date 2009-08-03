get_point = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetPoint",
    "output_package_name": "user_interface",
    "output_module_name": "get_point",

    "doc_html": """
        Pauses for user input of a point.
    """,

    "syntax_html": {
        0: ("strMessage", "arrPoint", "dblDistance", "blnPlane"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "py_name": "message",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Point",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying a starting, or base, point.
            """
        },
        2: {
            "name": "dblDistance",
            "py_name": "distance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Distance",
            "doc": """
        A constraining distance.  If a constraining distance is specified, a base point must also be specified.
            """
        },
        3: {
            "name": "blnPlane",
            "py_name": "plane",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Plane",
            "doc": """
        Constrain the point selection to the active construction plane.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A zero-based, one-dimensional array containing three numbers identifying the 3-D point input by the user successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 61,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDistance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


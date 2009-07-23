xform_world_to_screen = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformWorldToScreen",
    "output_package_name": "transformation",
    "output_module_name": "xform_world_to_screen",

    "doc_html": """
        Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.
    """,

    "syntax_html": {
        0: ("arrPoint", "strView", "blnConvert"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point in world coordinates.
            """
        },
        1: {
            "name": "strView",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title of the view.  If omitted, the active view is used.
            """
        },
        2: {
            "name": "blnConvert",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Convert",
            "doc": """
        If omitted or False, the function returns the results as client-area coordinates of the specified view. If True, then the results are returned as screen coordinates.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnConvert is omitted or False, a 2-D point in client-area coordinates if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnConvert is True, a 2-D point in screen coordinates if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 582,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaClientToScreen",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


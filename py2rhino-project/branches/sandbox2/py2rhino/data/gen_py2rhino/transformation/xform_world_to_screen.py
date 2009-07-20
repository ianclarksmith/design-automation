xform_world_to_screen = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_world_to_screen",

    "doc_html": """
        Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.
    """,

    "syntax_html": """
        Rhino.XformWorldToScreen (arrPoint [, strView [, blnConvert]])
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point in world coordinates.
            """
        },
        1: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title of the view.  If omitted, the active view is used.
            """
        },
        2: {
            "name": "Convert",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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


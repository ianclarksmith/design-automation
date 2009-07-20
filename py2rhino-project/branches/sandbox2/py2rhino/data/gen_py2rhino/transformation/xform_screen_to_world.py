xform_screen_to_world = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformScreenToWorld",
    "output_package_name": "transformation",
    "output_module_name": "xform_screen_to_world",

    "doc_html": """
        Transforms either client-area coordinates of a specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point.
    """,

    "syntax_html": """
        Rhino.XformScreenToWorld (arrPoint [, strView [, blnConvert]])
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 2-D point in either client-area coordinates of a specified view or screen coordinates.
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
        If omitted or False, the function assumes arrPoint represents client-area coordinates. If True, then the function assumes arrPoint represents screen coordinates.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A 3-D point in world coordinates if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 581,

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
            "name": "vaScreenToClient",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


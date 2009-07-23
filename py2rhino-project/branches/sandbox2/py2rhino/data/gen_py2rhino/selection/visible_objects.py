visible_objects = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "VisibleObjects",
    "output_package_name": "selection",
    "output_module_name": "visible_objects",

    "doc_html": """
        Returns the identifiers of all objects that are visible in a specified view.
    """,

    "syntax_html": {
        0: ("strView", "blnSelect", "blnIncludeLights", "blnIncludeGrips"),
    },

    "params_html": {
        0: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "blnSelect",
            "py_name": "select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
            "doc": """
        Select the objects.  If omitted, the object is not selected (False).
            """
        },
        2: {
            "name": "blnIncludeLights",
            "py_name": "include_lights",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "IncludeLights",
            "doc": """
        Include light objects.  If omitted, light objects are not returned (False).
            """
        },
        3: {
            "name": "blnIncludeGrips",
            "py_name": "include_grips",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "IncludeGrips",
            "doc": """
        Include grips objects.  If omitted, grips objects are not returned (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 825,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaIncludeLights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaIncludeGrips",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


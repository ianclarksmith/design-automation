last_object = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "LastObject",
    "output_package_name": "selection",
    "output_module_name": "last_object",

    "doc_html": """
        Returns the identifier of the last object in the document.  The last object in the document is the first object created by the user.
    """,

    "syntax_html": {
        0: ("blnSelect", "blnIncludeLights", "blnIncludeGrips"),
    },

    "params_html": {
        0: {
            "name": "blnSelect",
            "py_name": "select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
            "doc": """
        Select the object.  If omitted, the object is not selected (False).
            """
        },
        1: {
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
        2: {
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
            "type": "string",
            "doc": "The identifier of the object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 35,

    "params_com": {
        0: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIncludeLights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaIncludeGrips",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


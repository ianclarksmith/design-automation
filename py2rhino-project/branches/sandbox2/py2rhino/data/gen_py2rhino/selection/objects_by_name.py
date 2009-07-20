objects_by_name = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "ObjectsByName",
    "output_package_name": "selection",
    "output_module_name": "objects_by_name",

    "doc_html": """
        Returns the identifiers of all objects based on the objects' user-assigned name.
    """,

    "syntax_html": """
        Rhino.ObjectsByName (strName [, blnSelect [, blnIncludeLights]])
    """,

    "params_html": {
        0: {
            "name": "Name",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an object or objects.
            """
        },
        1: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the objects.  If omitted, the objects are not selected (False).
            """
        },
        2: {
            "name": "IncludeLights",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Include light objects.  If omitted, light objects are not returned (False).
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

    "id_com": 40,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
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
    },

    "returns_com": "tagVARIANT",

}


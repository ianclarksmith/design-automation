prev_object_grip = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "PrevObjectGrip",
    "output_package_name": "object_grip",
    "output_module_name": "prev_object_grip",

    "doc_html": """
        Returns the previous grip index from a specified grip index of an object.
    """,

    "syntax_html": """
        Rhino.PrevObjectGrip (strObject, intIndex [, intDirection [, blnSelect]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Index",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based grip index from which to get the previous grip index.
            """
        },
        2: {
            "name": "Direction",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction to get the previous grip index, either 0=U or 1=V. The default value is 0. Note, this argument only applies when dealing with surfaces.
            """
        },
        3: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), the previous grip index found will be selected. Otherwise, it will not be selected.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The index of the next grip from the specified grip index."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 559,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDir",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


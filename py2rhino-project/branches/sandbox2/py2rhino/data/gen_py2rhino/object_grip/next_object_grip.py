next_object_grip = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "NextObjectGrip",
    "output_package_name": "object_grip",
    "output_module_name": "next_object_grip",

    "doc_html": """
        Returns the next grip index from a specified grip index of an object.
    """,

    "syntax_html": {
        0: ("strObject", "intIndex", "intDirection", "blnSelect"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "intIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Index",
            "doc": """
        The zero-based grip index from which to get the next grip index.
            """
        },
        2: {
            "name": "intDirection",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Direction",
            "doc": """
        The direction to get the next grip index, either 0=U or 1=V. The default value is 0. Note, this argument only applies when dealing with surfaces.
            """
        },
        3: {
            "name": "blnEnable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Enable",
            "doc": """
        If True (default), the next grip index found will be selected. Otherwise, it will not be selected.
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

    "id_com": 558,

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


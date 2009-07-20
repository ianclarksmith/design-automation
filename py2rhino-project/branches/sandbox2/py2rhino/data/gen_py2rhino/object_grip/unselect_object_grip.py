unselect_object_grip = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "UnselectObjectGrip",
    "output_package_name": "object_grip",
    "output_module_name": "unselect_object_grip",

    "doc_html": """
        Unselects a single grip owned by an object.
    """,

    "syntax_html": """
        Rhino.UnselectObjectGrip (strObject, intIndex)
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
        The zero-based grip index to unselect.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 555,

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
    },

    "returns_com": "tagVARIANT",

}


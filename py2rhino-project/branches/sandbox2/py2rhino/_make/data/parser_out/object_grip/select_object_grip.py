select_object_grip = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "SelectObjectGrip",
    "output_package_name": "object_grip",
    "output_module_name": "select_object_grip",

    "doc_html": """
        Selects a single grip owned by an object. If the object's grips are not turned on, grips will  not be selected.
    """,

    "syntax_html": {
        0: ("strObject", "intIndex"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
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
            "py_name": "index",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Index",
            "doc": """
        The zero-based grip index to select.
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

    "id_com": 554,

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


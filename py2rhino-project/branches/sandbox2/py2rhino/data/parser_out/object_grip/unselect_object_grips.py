unselect_object_grips = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "UnselectObjectGrips",
    "output_package_name": "object_grip",
    "output_module_name": "unselect_object_grips",

    "doc_html": """
        Unselects an object's grips. Note, the grips will not be turned off.
    """,

    "syntax_html": {
        0: ("strObject"),
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
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of grips unselected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 502,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


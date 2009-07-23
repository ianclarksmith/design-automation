select_object_grips = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "SelectObjectGrips",
    "output_package_name": "object_grip",
    "output_module_name": "select_object_grips",

    "doc_html": """
        Selects an object's grips. If the object's grips are not turned on, they will not be selected.
    """,

    "syntax_html": {
        0: ("strObject"),
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
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of grips selected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 501,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


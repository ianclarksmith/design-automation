selected_object_grips = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "SelectedObjectGrips",
    "output_package_name": "object_grip",
    "output_module_name": "selected_object_grips",

    "doc_html": """
        Returns an array of grip indices identifying an object's selected grips.
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
            "type": "array",
            "doc": "An array of zero-based grip indices identifying the selected grips."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 560,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


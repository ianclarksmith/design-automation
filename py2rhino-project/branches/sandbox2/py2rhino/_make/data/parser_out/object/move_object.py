move_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "MoveObject",
    "output_package_name": "object",
    "output_module_name": "move_object",

    "doc_html": """
        Moves a single object.
    """,

    "syntax_html": {
        0: ("strObject", "arrStart", "arrEnd"),
        1: ("strObject", "arrTranslation"),
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
        The identifier of the object to move.
            """
        },
        1: {
            "name": "arrStart",
            "py_name": "start",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Start",
            "doc": """
        The 3-D starting, or base, point of the move operation.
            """
        },
        2: {
            "name": "arrEnd",
            "py_name": "end",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "End",
            "doc": """
        The 3-D ending point of the move operation.
            """
        },
        3: {
            "name": "arrTranslation",
            "py_name": "translation",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Translation",
            "doc": """
        The 3-D translation vector.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "The identifier of the moved object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 270,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


object_names = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectNames",
    "output_package_name": "object",
    "output_module_name": "object_names",

    "doc_html": """
        Returns or modifies the user-definable name of one or more objects.
    """,

    "syntax_html": {
        0: ("arrObjects", "arrNames"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects.
            """
        },
        1: {
            "name": "arrNames",
            "py_name": "names",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Names",
            "doc": """
        An array of strings identifying the new user-definable names. This array must have the same upper bounds as arrObjects.  Each element in arrNames will correspond with each element in arrObjects.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrNames is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null."
        },
        1: {
            "type": "array",
            "doc": "If arrNames is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 639,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNames",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


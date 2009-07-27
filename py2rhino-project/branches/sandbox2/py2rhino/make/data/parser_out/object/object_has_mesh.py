object_has_mesh = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectHasMesh",
    "output_package_name": "object",
    "output_module_name": "object_has_mesh",

    "doc_html": """
        Verifies that an object has custom render mesh parameters.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "Object",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a meshable object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True of the object has custom render mesh parameters, False otherwise."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 867,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


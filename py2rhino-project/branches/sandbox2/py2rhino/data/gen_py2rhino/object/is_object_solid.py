is_object_solid = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "IsObjectSolid",
    "output_package_name": "object",
    "output_module_name": "is_object_solid",

    "doc_html": """
        Verifies that an object is a closed, solid object.
    """,

    "syntax_html": """
        Rhino.IsObjectSolid (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 189,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


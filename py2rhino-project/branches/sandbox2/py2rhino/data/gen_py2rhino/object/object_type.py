object_type = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectType",
    "output_package_name": "object",
    "output_module_name": "object_type",

    "doc_html": """
        Returns the object type.
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
            "doc": "The object type if successful.  The valid object types are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 198,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


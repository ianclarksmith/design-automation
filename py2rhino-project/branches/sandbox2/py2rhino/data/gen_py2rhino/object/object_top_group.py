object_top_group = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectTopGroup",
    "output_package_name": "object",
    "output_module_name": "object_top_group",

    "doc_html": """
        Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.
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
            "type": "string",
            "doc": "The top most group name of the object if successful"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 197,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


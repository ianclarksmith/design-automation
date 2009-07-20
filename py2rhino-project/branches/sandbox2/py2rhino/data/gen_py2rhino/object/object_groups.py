object_groups = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectGroups",
    "output_package_name": "object",
    "output_module_name": "object_groups",

    "doc_html": """
        Returns all of the group names that an object is assigned.
    """,

    "syntax_html": """
        Rhino.ObjectGroups (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of all group names for the object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 193,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


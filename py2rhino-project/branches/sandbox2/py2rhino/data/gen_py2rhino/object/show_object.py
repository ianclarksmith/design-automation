show_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ShowObject",
    "output_package_name": "object",
    "output_module_name": "show_object",

    "doc_html": """
        Shows a previously hidden object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    """,

    "syntax_html": """
        Rhino.ShowObject (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to show.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 201,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


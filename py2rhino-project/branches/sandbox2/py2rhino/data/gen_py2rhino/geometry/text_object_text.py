text_object_text = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "TextObjectText",
    "output_package_name": "geometry",
    "output_module_name": "text_object_text",

    "doc_html": """
        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.
    """,

    "syntax_html": {
        0: ("strObject", "strText"),
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
        1: {
            "name": "strText",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Text",
            "doc": """
        A new character or text string.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a new text string is not specified,  the current string value if successful."
        },
        1: {
            "type": "string",
            "doc": "If a new text string is specified,  the previous string value if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 472,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


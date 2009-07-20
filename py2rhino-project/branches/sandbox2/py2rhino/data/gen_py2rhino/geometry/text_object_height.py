text_object_height = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "TextObjectHeight",
    "output_package_name": "geometry",
    "output_module_name": "text_object_height",

    "doc_html": """
        Returns or modifies the height of a text object.
    """,

    "syntax_html": """
        Rhino.TextObjectHeight (strObject [, dblHeight])
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
        1: {
            "name": "Height",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new text height.  If omitted, the current text height is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a height is not specified, the current text height if successful."
        },
        1: {
            "type": "string",
            "doc": "If a height is specified, the previous text height if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 473,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSize",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


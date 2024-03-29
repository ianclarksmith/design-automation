text_object_font = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "TextObjectFont",
    "output_package_name": "geometry",
    "output_module_name": "text_object_font",

    "doc_html": """
        Returns or modifies the font used by text object.
    """,

    "syntax_html": {
        0: ("strObject", "strFont"),
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
        1: {
            "name": "strFont",
            "py_name": "font",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Font",
            "doc": """
        The new font face name.  If omitted, the current font is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a font is not specified,  the current font face name if successful."
        },
        1: {
            "type": "string",
            "doc": "If a font is specified,  the previous font face name if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 474,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFont",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


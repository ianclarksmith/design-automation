text_object_style = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "TextObjectStyle",
    "output_package_name": "geometry",
    "output_module_name": "text_object_style",

    "doc_html": """
        Returns or modifies the font style of a text object.
    """,

    "syntax_html": {
        0: ("strObject", "intStyle"),
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
            "name": "intStyle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Style",
            "doc": """
        The font style.  If omitted, the current font style is returned.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal.
		1
		Bold.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a style is not specified,  the current font style if successful."
        },
        1: {
            "type": "number",
            "doc": "If a style is specified,  the previous font style if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 475,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


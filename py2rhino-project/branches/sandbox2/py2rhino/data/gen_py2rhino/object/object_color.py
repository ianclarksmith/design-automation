object_color = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectColor",
    "output_package_name": "object",
    "output_module_name": "object_color",

    "doc_html": """
        Returns or modifies the color of an object.  Object colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": {
        0: ("strObject", "lngColor"),
        1: ("arrObjects", "lngColor"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        1: {
            "name": "lngColor",
            "py_name": "color",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "lng",
            "name_main": "Color",
            "doc": """
        The new color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a color value is not specified,  the current color value if successful."
        },
        1: {
            "type": "number",
            "doc": "If a color value is specified, the previous color value if successful."
        },
        2: {
            "type": "number",
            "doc": "If arrObjects is specified, then the number of objects modified if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 191,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


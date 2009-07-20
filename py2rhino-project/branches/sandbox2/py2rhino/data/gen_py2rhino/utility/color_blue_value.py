color_blue_value = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "color_blue_value",

    "doc_html": """
        Retrieves an intensity value for the blue component of a red-green-blue (RGB) value.
    """,

    "syntax_html": """
        Rhino.ColorBlueValue (lngRGB)
    """,

    "params_html": {
        0: {
            "name": "RGB",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The RGB color value.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The blue component if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 882,

    "params_com": {
        0: {
            "name": "vaRGB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


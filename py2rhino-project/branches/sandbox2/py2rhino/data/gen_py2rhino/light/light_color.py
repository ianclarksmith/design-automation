light_color = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "light_color",

    "doc_html": """
        Returns or changes the color of a light.  Light colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": """
        Rhino.LightColor (strObject [, lngColor])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The light object's identifier.
            """
        },
        1: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The new color value.  If omitted, the current light color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a color value  is not specified,  the current light value if successful."
        },
        1: {
            "type": "number",
            "doc": "If a color value is specified, the previous light value if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 167,

    "params_com": {
        0: {
            "name": "vaLight",
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


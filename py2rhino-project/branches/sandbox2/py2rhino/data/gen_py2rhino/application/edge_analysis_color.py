edge_analysis_color = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "edge_analysis_color",

    "doc_html": """
        Returns or modifies edge analysis color displayed by the ShowEdges command.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": """
        Rhino.EdgeAnalysisColor ([lngColor])
    """,

    "params_html": {
        0: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The new color value.  If omitted, the current item color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a lngColor is not specified, the current edge analysis color if successful."
        },
        1: {
            "type": "number",
            "doc": "If a lngColor is specified, the previous edge analysis color if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 449,

    "params_com": {
        0: {
            "name": "vaColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


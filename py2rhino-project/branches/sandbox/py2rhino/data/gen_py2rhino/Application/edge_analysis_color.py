edge_analysis_color = {

    "class": "Application",
    "method": "edge_analysis_color",
    "doc": """
        Returns or modifies edge analysis color displayed by the ShowEdges command.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax": """
        Rhino.EdgeAnalysisColor ([lngColor])
    """,

    "params": {
        0: {
            "name": "color",
            "optional": True,
            "type_vb": "number",
            "type_string": "lng",
            "doc": """
        The new color value.  If omitted, the current item color is returned.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "If a lngColor is not specified, the current edge analysis color if successful."
        },
        1: {
            "type_vb": "Number",
            "doc": "If a lngColor is specified, the previous edge analysis color if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}


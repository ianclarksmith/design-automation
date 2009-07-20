render_color = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderColor",
    "output_package_name": "document",
    "output_module_name": "render_color",

    "doc_html": """
        Returns or sets the render ambient light or background color. Render colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed. See Rhino's DocumentProperties command (Rhino Render window) for details.
    """,

    "syntax_html": """
        Rhino.RenderColor (intItem, [lngColor])
    """,

    "params_html": {
        0: {
            "name": "Item",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The item you wish to either query or change.
		0
		Ambient light color.
		1
            """
        },
        1: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The new color value. If omitted, the curreng intItem color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If lngColor is not specified, the current intItem color if successful."
        },
        1: {
            "type": "number",
            "doc": "If lngColor is specified, the previous intItem color if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 331,

    "params_com": {
        0: {
            "name": "vaItem",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


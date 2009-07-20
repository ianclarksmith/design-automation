render_resolution = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_resolution",

    "doc_html": """
        Returns or sets the render resolution. Resolution is measured in pixels. See Rhino's DocumentProperties command (Rhino Render window) for details. Note, if the render resolution is set to "viewport", then the size of the active viewt is returned.
    """,

    "syntax_html": """
        Rhino.RenderResolution ([arrResolution])
    """,

    "params_html": {
        0: {
            "name": "Resolution",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array containing two numbers identifying the resolution width and height in pixels.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrResolution is not specified, an array containing two numbers identifying the current resolution width and height in pixels if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrResolution is specified, an array containing two numbers identifying the previous resolution width and height in pixels if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 332,

    "params_com": {
        0: {
            "name": "vaSizes",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


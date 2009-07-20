add_rectangular_light = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "add_rectangular_light",

    "doc_html": """
        Adds a new rectangular light object  to the document.
    """,

    "syntax_html": """
        Rhino.AddRectangularLight (arrOrigin, arrWidth, arrHeight)
    """,

    "params_html": {
        0: {
            "name": "Origin",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D origin point of the light.
            """
        },
        1: {
            "name": "Width",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D width and direction point of the light.
            """
        },
        2: {
            "name": "Height",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D height and direction point of the light.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 156,

    "params_com": {
        0: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


add_point_light = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "add_point_light",

    "doc_html": """
        Adds a new point light object  to the document.
    """,

    "syntax_html": """
        Rhino.AddPointLight (arrPoint)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D location point of the light.
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

    "id_com": 155,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


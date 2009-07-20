add_directional_light = {
    "module_name": "light",
    "class_name": "Light",
    "method_name": "add_directional_light",

    "doc_html": """
        Adds a new directional light object  to the document.
    """,

    "syntax_html": """
        Rhino.AddDirectionalLight (arrStartPoint, arrEndPoint)
    """,

    "params_html": {
        0: {
            "name": "StartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D starting point of the light.
            """
        },
        1: {
            "name": "EndPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D ending point and direction of the light.
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

    "id_com": 153,

    "params_com": {
        0: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


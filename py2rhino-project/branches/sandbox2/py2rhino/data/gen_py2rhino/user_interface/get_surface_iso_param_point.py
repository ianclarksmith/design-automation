get_surface_iso_param_point = {
    "module_name": "user_interface",
    "class_name": "UserInterface",
    "method_name": "get_surface_iso_param_point",

    "doc_html": """
        Pauses for user input of a point constrained to a surface object.
    """,

    "syntax_html": """
        Rhino.GetSurfaceIsoParamPoint (strObject [, strMessage])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The surface object's identifier.
            """
        },
        1: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of selection information if successful. The elements of the array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 775,

    "params_com": {
        0: {
            "name": "vaBrep",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


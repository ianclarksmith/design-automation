get_point_coordinates = {
    "module_name": "selection",
    "class_name": "Selection",
    "method_name": "get_point_coordinates",

    "doc_html": """
        Prompts the user to pick or select one or more point objects. Unlike GetObjects, this function does not return an array of point object identifiers. Rather, it returns an array of 3-D point coordinates - one for each selected point object. Note, the array returned is not in any sorted order.
    """,

    "syntax_html": """
        Rhino.GetPointCoordinates ([strMessage [, blnPreSelect]])
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "PreSelect",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points, one for each selected point object, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 645,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPreSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


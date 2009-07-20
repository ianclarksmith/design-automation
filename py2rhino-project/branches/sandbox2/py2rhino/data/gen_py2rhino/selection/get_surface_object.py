get_surface_object = {
    "module_name": "selection",
    "class_name": "Selection",
    "method_name": "get_surface_object",

    "doc_html": """
        Prompts the user to pick, or select, a single surface object.
    """,

    "syntax_html": """
        Rhino.GetSurfaceObject ([strMessage [, blnPreSelect [, blnSelect ]]])
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
        2: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the picked objects.  If omitted, the objects that are picked are not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of selection information if successful. The array will contain the following information:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 576,

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
        2: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


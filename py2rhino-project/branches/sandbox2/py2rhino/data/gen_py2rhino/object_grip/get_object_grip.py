get_object_grip = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "get_object_grip",

    "doc_html": """
        Prompts the user to pick or select a single object grip.
    """,

    "syntax_html": """
        Rhino.GetObjectGrip ([strMessage [, blnPreSelect [, blnSelect]]])
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
        Allow for the selection of a pre-selected object grip.  If omitted, pre-selected object grips are not accepted (False).
            """
        },
        2: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the picked object grip.  If omitted, the object grip that is  picked is not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A one-dimensional array containing the following three elements if successful:"
        },
        1: {
            "type": "string",
            "doc": "The identifier of the object that owns the grip."
        },
        2: {
            "type": "number",
            "doc": "The zero-based index value of the grip."
        },
        3: {
            "type": "array",
            "doc": "A 3-D point identifying the location of the grip."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 561,

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


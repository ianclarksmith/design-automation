get_object_grips = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "GetObjectGrips",
    "output_package_name": "object_grip",
    "output_module_name": "get_object_grips",

    "doc_html": """
        Prompts the user to pick or select one or more object grips from one or more objects.
    """,

    "syntax_html": """
        Rhino.GetObjectGrips ([strMessage [, blnPreSelect [, blnSelect]]])
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
        Allow for the selection of a pre-selected object grips.  If omitted, pre-selected object grips are not accepted (False).
            """
        },
        2: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the picked object grips.  If omitted, the object grips that are picked is not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A one-dimensional array containing one or more object grip records if successful. An object grip record itself is a one-dimensional array that contains the following three elements:"
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

    "id_com": 562,

    "params_com": {
        0: {
            "name": "vaPrompt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPreSelect",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaSelect",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


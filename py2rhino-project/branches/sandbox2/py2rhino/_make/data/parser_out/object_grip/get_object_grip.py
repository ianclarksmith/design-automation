get_object_grip = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "GetObjectGrip",
    "output_package_name": "object_grip",
    "output_module_name": "get_object_grip",

    "doc_html": """
        Prompts the user to pick or select a single object grip.
    """,

    "syntax_html": {
        0: ("strMessage", "blnPreSelect", "blnSelect"),
    },

    "params_html": {
        0: {
            "name": "strMessage",
            "py_name": "message",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Message",
            "doc": """
        A prompt or message.
            """
        },
        1: {
            "name": "blnPreSelect",
            "py_name": "pre_select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "PreSelect",
            "doc": """
        Allow for the selection of a pre-selected object grip.  If omitted, pre-selected object grips are not accepted (False).
            """
        },
        2: {
            "name": "blnSelect",
            "py_name": "select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
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


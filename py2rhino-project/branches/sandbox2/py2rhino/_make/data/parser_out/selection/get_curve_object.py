get_curve_object = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "GetCurveObject",
    "output_package_name": "selection",
    "output_module_name": "get_curve_object",

    "doc_html": """
        Prompts the user to pick, or select, a single curve object.
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
        Allow for the selection of pre-selected objects.  If omitted, pre-selected objects are not accepted (False).
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

    "id_com": 575,

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


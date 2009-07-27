get_point_coordinates = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "GetPointCoordinates",
    "output_package_name": "selection",
    "output_module_name": "get_point_coordinates",

    "doc_html": """
        Prompts the user to pick or select one or more point objects. Unlike GetObjects, this function does not return an array of point object identifiers. Rather, it returns an array of 3-D point coordinates - one for each selected point object. Note, the array returned is not in any sorted order.
    """,

    "syntax_html": {
        0: ("strMessage", "blnPreSelect"),
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


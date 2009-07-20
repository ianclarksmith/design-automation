get_distance = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetDistance",
    "output_package_name": "user_interface",
    "output_module_name": "get_distance",

    "doc_html": """
        Pauses for user input of a distance.
    """,

    "syntax_html": """
        Rhino.GetDistance ([arrPoint [, dblDistance [, strMessage1 [, strMessage2]]]])
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A zero-based, one-dimensional array containing three numbers identifying the first distance point.
            """
        },
        1: {
            "name": "Distance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A default distance value.
            """
        },
        2: {
            "name": "Message1",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message for the first distance point.
            """
        },
        3: {
            "name": "Message2",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt or message for the second distance point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The distance input by the user if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 66,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDefault",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPrompt1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaPrompt2",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


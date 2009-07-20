get_point_on_curve = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetPointOnCurve",
    "output_package_name": "user_interface",
    "output_module_name": "get_point_on_curve",

    "doc_html": """
        Pauses for user input of a point constrained to a curve object.
    """,

    "syntax_html": """
        Rhino.GetPointOnCurve (strObject [, strMessage])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
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
            "doc": "The 3-D point selected by the user if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 147,

    "params_com": {
        0: {
            "name": "vaObject",
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


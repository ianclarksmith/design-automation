get_color = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetColor",
    "output_package_name": "user_interface",
    "output_module_name": "get_color",

    "doc_html": """
        Displays the Rhino color picker dialog box allowing the user to select an RGB color value.
    """,

    "syntax_html": """
        Rhino.GetColor ([lngColor])
    """,

    "params_html": {
        0: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        A default RGB color value.  If omitted, the default color is black, or RGB(0,0,0).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The RGB color value selected by the user if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 65,

    "params_com": {
        0: {
            "name": "vaColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


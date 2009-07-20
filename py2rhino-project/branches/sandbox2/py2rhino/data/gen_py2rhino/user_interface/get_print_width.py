get_print_width = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "GetPrintWidth",
    "output_package_name": "user_interface",
    "output_module_name": "get_print_width",

    "doc_html": """
        Displays a dialog box prompting the user to select a print width.
    """,

    "syntax_html": """
        Rhino.GetPrintWidth ([dblPrintWidth])
    """,

    "params_html": {
        0: {
            "name": "PrintWidth",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The print width to select.  If omitted, the default print width will be selected.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The value of the selected print width if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 674,

    "params_com": {
        0: {
            "name": "vaPrintWidth",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


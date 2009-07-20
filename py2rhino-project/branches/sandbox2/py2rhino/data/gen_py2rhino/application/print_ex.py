print_ex = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "PrintEx",
    "output_package_name": "application",
    "output_module_name": "print_ex",

    "doc_html": """
        Prints a string to Rhino's command window.  Use this method, instead of the Print method, if you are using Visual Basic.
    """,

    "syntax_html": """
        Rhino.PrintEx ([strMessage])
    """,

    "params_html": {
        0: {
            "name": "Message",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        A prompt, message, or value.
            """
        },
    },

    "returns_html": {
    },

    "id_com": 370,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

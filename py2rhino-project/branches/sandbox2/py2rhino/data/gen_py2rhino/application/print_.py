print_ = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "Print",
    "output_package_name": "application",
    "output_module_name": "print_",

    "doc_html": """
        Prints a string to Rhino's command window.  Note, this method cannot be called from Visual Basic.  If you are using Visual Basic, use the PrintEx method.
    """,

    "syntax_html": """
        Rhino.Print ([strMessage])
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

    "id_com": 2,

    "params_com": {
        0: {
            "name": "vaCmd",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

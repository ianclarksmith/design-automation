current_printer = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "CurrentPrinter",
    "output_package_name": "utility",
    "output_module_name": "current_printer",

    "doc_html": """
        Returns or changes the current Windows printer.
    """,

    "syntax_html": """
        Rhino.CurrentPrinter ([strPrinter])
    """,

    "params_html": {
        0: {
            "name": "Printer",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of a Windows printer as returned by this method or by the PrinterNames method.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strPrinter is not specified, the name of the current Windows printer if successful."
        },
        1: {
            "type": "string",
            "doc": "If strPrinter is specified, the name of the previously current Windows printer if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 358,

    "params_com": {
        0: {
            "name": "vaPrinter",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


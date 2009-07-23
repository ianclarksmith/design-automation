spool_to_printer = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "SpoolToPrinter",
    "output_package_name": "utility",
    "output_module_name": "spool_to_printer",

    "doc_html": """
        Spools, or sends, a text file or a print/plot file to a Windows printer.
    """,

    "syntax_html": {
        0: ("strFile", "strPrinter"),
    },

    "params_html": {
        0: {
            "name": "strFile",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "File",
            "doc": """
        The full path to the file to spool
            """
        },
        1: {
            "name": "strPrinter",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Printer",
            "doc": """
        The name of a Windows printer as returned by either the CurrentPrinter or by the PrinterNames method.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the spooled file if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 357,

    "params_com": {
        0: {
            "name": "vaFile",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPrinter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


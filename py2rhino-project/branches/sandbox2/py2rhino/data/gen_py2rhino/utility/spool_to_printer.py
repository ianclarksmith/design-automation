spool_to_printer = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "spool_to_printer",

    "doc_html": """
        Spools, or sends, a text file or a print/plot file to a Windows printer.
    """,

    "syntax_html": """
        Rhino.SpoolToPrinter (strFile, strPrinter)
    """,

    "params_html": {
        0: {
            "name": "File",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The full path to the file to spool
            """
        },
        1: {
            "name": "Printer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
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


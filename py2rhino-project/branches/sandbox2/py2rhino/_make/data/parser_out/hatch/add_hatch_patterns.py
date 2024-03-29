add_hatch_patterns = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "AddHatchPatterns",
    "output_package_name": "hatch",
    "output_module_name": "add_hatch_patterns",

    "doc_html": """
        Adds hatch pattens to the document by importing hatch pattern definitions from a pattern file. For more information on hatch pattern files, see the Rhino help file for the Hatch command.
    """,

    "syntax_html": {
        0: ("strFileName", "blnReplace"),
    },

    "params_html": {
        0: {
            "name": "strFileName",
            "py_name": "file_name",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "FileName",
            "doc": """
        The name of the hatch pattern file to import.
            """
        },
        1: {
            "name": "blnReplace",
            "py_name": "replace",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Replace",
            "doc": """
        If hatch pattern names already in the document match hatch pattern names in the pattern definition file, then the existing hatch patterns will be redefined.  If omitted, existing hatch patterns will not be redefined (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The names of the newly added hatch patterns if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 826,

    "params_com": {
        0: {
            "name": "vaFileName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaReplace",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


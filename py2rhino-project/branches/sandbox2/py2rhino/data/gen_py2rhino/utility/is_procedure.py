is_procedure = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "IsProcedure",
    "output_package_name": "utility",
    "output_module_name": "is_procedure",

    "doc_html": """
        Verifies that a user-defined subroutine or function is resident in RhinoScript's VBScript engine.
    """,

    "syntax_html": {
        0: ("strSubName"),
    },

    "params_html": {
        0: {
            "name": "strSubName",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "SubName",
            "doc": """
        The name of a user-defined subroutine of function.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 287,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


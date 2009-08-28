all_procedures = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "AllProcedures",
    "output_package_name": "utility",
    "output_module_name": "all_procedures",

    "doc_html": """
        Returns the names of the  user-defined subroutines and functions resident in RhinoScript's VBScript engine.
    """,

    "syntax_html": {
        0: ("blnAll"),
    },

    "params_html": {
        0: {
            "name": "blnAll",
            "py_name": "all",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "All",
            "doc": """
        If True (default) the names of all user-defined subroutines and functions are returned. If False, only top-level subroutines are returned. Top level subroutines are subroutines that can be passed to the RunScript command.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of string identifying the names of user-defined procedures."
        },
        1: {
            "type": "null",
            "doc": "If no user-defined procedures are found."
        },
    },

    "id_com": 503,

    "params_com": {
        0: {
            "name": "vaAll",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


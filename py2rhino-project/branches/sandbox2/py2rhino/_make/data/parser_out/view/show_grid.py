show_grid = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ShowGrid",
    "output_package_name": "view",
    "output_module_name": "show_grid",

    "doc_html": """
        Shows or hides a view's construction plane grid.
    """,

    "syntax_html": {
        0: ("strView", "blnShow"),
    },

    "params_html": {
        0: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title or identifier of the view to modify.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "blnShow",
            "py_name": "show",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Show",
            "doc": """
        The grid display state to set.  If omitted, the current grid display state is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnShow is not specified, then the grid display state if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnShow is specified, then the previous grid display state if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 738,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaShow",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


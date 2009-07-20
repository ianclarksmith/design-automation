show_grid = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ShowGrid",
    "output_package_name": "view",
    "output_module_name": "show_grid",

    "doc_html": """
        Shows or hides a view's construction plane grid.
    """,

    "syntax_html": """
        Rhino.ShowGrid ([strView [, blnShow]])
    """,

    "params_html": {
        0: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view to modify.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "Show",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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


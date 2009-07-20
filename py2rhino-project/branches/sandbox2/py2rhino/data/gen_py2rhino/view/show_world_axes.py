show_world_axes = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ShowWorldAxes",
    "output_package_name": "view",
    "output_module_name": "show_world_axes",

    "doc_html": """
        Shows or hides a view's world axes icon.
    """,

    "syntax_html": """
        Rhino.ShowWorldAxes ([strView [, blnShow]])
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
        The world axes icon display state to set.  If omitted, the current world axes icon display state is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnShow is not specified, then the world axes icon display state if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnShow is specified, then the previous world axes icon display state if successful."
        },
        2: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 740,

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


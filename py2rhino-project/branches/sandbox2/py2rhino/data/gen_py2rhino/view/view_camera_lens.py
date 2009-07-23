view_camera_lens = {
    "input_folder_name": "View_Methods",
    "input_file_name": "ViewCameraLens",
    "output_package_name": "view",
    "output_module_name": "view_camera_lens",

    "doc_html": """
        Returns or sets the 35mm camera lens length of the specified perspective projection view.
    """,

    "syntax_html": {
        0: ("strView", "dblLength"),
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
        The title or identifier of the view.  If omitted, the current active view is used.
            """
        },
        1: {
            "name": "dblLength",
            "py_name": "length",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Length",
            "doc": """
        The new 35mm camera lens length.  If omitted, the previous 35mm camera lens length is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a lens length is not specified, the current lens length if successful."
        },
        1: {
            "type": "number",
            "doc": "If a lens length is specified, the previous lens length is successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 262,

    "params_com": {
        0: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


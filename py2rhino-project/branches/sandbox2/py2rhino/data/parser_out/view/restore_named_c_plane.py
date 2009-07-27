restore_named_c_plane = {
    "input_folder_name": "View_Methods",
    "input_file_name": "RestoreNamedCPlane",
    "output_package_name": "view",
    "output_module_name": "restore_named_c_plane",

    "doc_html": """
        Restores a named construction plane to the specified view.
    """,

    "syntax_html": {
        0: ("strName", "strView"),
    },

    "params_html": {
        0: {
            "name": "strName",
            "py_name": "name",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Name",
            "doc": """
        The name of the named construction plane to restore.
            """
        },
        1: {
            "name": "strView",
            "py_name": "view",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "View",
            "doc": """
        The title or identifier of the view to restore the construction plane.  If omitted, the current active view is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the restored named construction plane if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 282,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


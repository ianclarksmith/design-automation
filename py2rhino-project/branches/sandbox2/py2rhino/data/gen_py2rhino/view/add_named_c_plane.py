add_named_c_plane = {
    "input_folder_name": "View_Methods",
    "input_file_name": "AddNamedCPlane",
    "output_package_name": "view",
    "output_module_name": "add_named_c_plane",

    "doc_html": """
        Adds a new named construction plane to the document.
    """,

    "syntax_html": """
        Rhino.AddNamedCPlane (strName [, strView])
    """,

    "params_html": {
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the newly created named construction plane if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 280,

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


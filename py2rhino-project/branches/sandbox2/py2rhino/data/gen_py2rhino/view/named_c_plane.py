named_c_plane = {
    "input_folder_name": "View_Methods",
    "input_file_name": "NamedCPlane",
    "output_package_name": "view",
    "output_module_name": "named_c_plane",

    "doc_html": """
        Returns the plane geometry of the specified named construction plane.
    """,

    "syntax_html": """
        Rhino.NamedCPlane (strName)
    """,

    "params_html": {
        0: {
            "name": "Name",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of a named construction plane.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the plane. The elements of a construction plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 286,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


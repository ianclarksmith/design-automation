add_edge_srf = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddEdgeSrf",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_edge_srf",

    "doc_html": """
        Creates a surface from 2, 3, or 4 edge curves.
    """,

    "syntax_html": {
        0: ("arrObjects"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of 2, 3, or 4 curve object identifiers.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 203,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


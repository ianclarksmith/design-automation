join_surfaces = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "JoinSurfaces",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "join_surfaces",

    "doc_html": """
        Joins two or more surface or polysurface object together to form one polysurface object.
    """,

    "syntax_html": {
        0: ("arrObjects", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        An ordered array of strings identifying the surfaces or polysurfaces objects to join.
            """
        },
        1: {
            "name": "blnDelete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete input objects after joining.  The default is not to delete objects (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the newly created polysurface object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 487,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


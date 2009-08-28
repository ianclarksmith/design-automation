explode_polysurfaces = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExplodePolysurfaces",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "explode_polysurfaces",

    "doc_html": """
        Explodes, or un-joins,  one more polysurface objects.  Polysurfaces will be exploded into separate surfaces.
    """,

    "syntax_html": {
        0: ("strObject", "blnDelete"),
        1: ("arrObjects", "blnDelete"),
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
        An array of strings identifying the polysurface objects to explode.
            """
        },
        1: {
            "name": "blnDelete",
            "py_name": "delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete input objects after exploding.  The default is not to delete objects (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created surface objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 447,

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


explode_polysurfaces = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExplodePolysurfaces",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "explode_polysurfaces",

    "doc_html": """
        Explodes, or un-joins,  one more polysurface objects.  Polysurfaces will be exploded into separate surfaces.
    """,

    "syntax_html": """
        Rhino.ExplodePolysurfaces (strObject [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the polysurface objects to explode.
            """
        },
        1: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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


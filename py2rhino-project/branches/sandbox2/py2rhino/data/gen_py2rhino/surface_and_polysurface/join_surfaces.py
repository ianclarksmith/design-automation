join_surfaces = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "join_surfaces",

    "doc_html": """
        Joins two or more surface or polysurface object together to form one polysurface object.
    """,

    "syntax_html": """
        Rhino.JoinSurfaces (arrObjects [,blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "str",
            "doc": """
        An ordered array of strings identifying the surfaces or polysurfaces objects to join.
            """
        },
        1: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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


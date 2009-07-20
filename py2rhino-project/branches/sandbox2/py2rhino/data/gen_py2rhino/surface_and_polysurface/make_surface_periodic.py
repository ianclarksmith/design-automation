make_surface_periodic = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "MakeSurfacePeriodic",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "make_surface_periodic",

    "doc_html": """
        Makes an existing surface a periodic NURBS surface.
    """,

    "syntax_html": """
        Rhino.MakeSurfacePeriodic (strObject, intDirection [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction to make periodic, either 0 = U, or 1 = V.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete input surface.  If omitted, the input surface will not be deleted (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If blnDelete is False, the identifier of the new object if successful."
        },
        1: {
            "type": "string",
            "doc": "If blnDelete is True, the identifier of the modified object if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 445,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDir",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


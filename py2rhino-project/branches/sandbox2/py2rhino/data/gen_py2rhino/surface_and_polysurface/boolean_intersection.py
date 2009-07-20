boolean_intersection = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "BooleanIntersection",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "boolean_intersection",

    "doc_html": """
        Performs a Boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.BooleanIntersection (arrInput0, arrInput1 [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Input0",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the surfaces or polysurfaces.
            """
        },
        1: {
            "name": "Input1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the surfaces or polysurfaces.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete all input objects. The default is to delete all input objects (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the newly created objects, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 507,

    "params_com": {
        0: {
            "name": "vaInBreps0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaInBreps1",
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


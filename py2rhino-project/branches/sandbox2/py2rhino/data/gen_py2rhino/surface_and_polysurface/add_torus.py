add_torus = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddTorus",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_torus",

    "doc_html": """
        Adds a torus-shaped revolved surface to the document.
    """,

    "syntax_html": """
        Rhino.AddTorus (arrBase, dblMajorRadius, dblMinorRadius [, arrDirection])
    """,

    "params_html": {
        0: {
            "name": "Base",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D origin point of the torus.
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The base plane of the torus.
            """
        },
        2: {
            "name": "MajorRadius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The major radius of the torus.  The major radius must be larger than the minor radius.
            """
        },
        3: {
            "name": "MinorRadius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The minor radius of the torus.  The minor radius must be greater than zero.
            """
        },
        4: {
            "name": "Direction",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A point that defines the direction of the torus.  If omitted, a torus that is parallel to the world XY plane is created.
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

    "id_com": 74,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRadius2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaDirection",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


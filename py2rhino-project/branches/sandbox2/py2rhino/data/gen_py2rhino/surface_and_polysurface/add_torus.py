add_torus = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddTorus",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_torus",

    "doc_html": """
        Adds a torus-shaped revolved surface to the document.
    """,

    "syntax_html": {
        0: ("arrBase", "dblMajorRadius", "dblMinorRadius", "arrDirection"),
        1: ("arrPlane", "dblMajorRadius", "dblMinorRadius"),
    },

    "params_html": {
        0: {
            "name": "arrBase",
            "py_name": "base",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Base",
            "doc": """
        The 3-D origin point of the torus.
            """
        },
        1: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Plane",
            "doc": """
        The base plane of the torus.
            """
        },
        2: {
            "name": "dblMajorRadius",
            "py_name": "major_radius",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "MajorRadius",
            "doc": """
        The major radius of the torus.  The major radius must be larger than the minor radius.
            """
        },
        3: {
            "name": "dblMinorRadius",
            "py_name": "minor_radius",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "MinorRadius",
            "doc": """
        The minor radius of the torus.  The minor radius must be greater than zero.
            """
        },
        4: {
            "name": "arrDirection",
            "py_name": "direction",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Direction",
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


intersect_breps = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "IntersectBreps",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "intersect_breps",

    "doc_html": """
        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.
    """,

    "syntax_html": {
        0: ("strBrep1", "strBrep2", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "strBrep1",
            "py_name": "brep1",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Brep1",
            "doc": """
        The first brep object's identifier.
            """
        },
        1: {
            "name": "strBrep2",
            "py_name": "brep2",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Brep2",
            "doc": """
        The second  brep object's identifier.
            """
        },
        2: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created intersection curve and point objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 544,

    "params_com": {
        0: {
            "name": "vaBrep0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBrep1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


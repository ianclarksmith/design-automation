add_srf_section_crvs = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "add_srf_section_crvs",

    "doc_html": """
        Adds planar curves resulting from the intersection of a defined cutting plane through a surface or a polysurface. For more information, see the Rhino help file for details on the Section command.
    """,

    "syntax_html": """
        Rhino.AddSrfSectionCrvs (strObject, arrPlane)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a surface or polysurface object.
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A plane that defines the cutting plane.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created section curves if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 803,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


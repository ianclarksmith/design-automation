project_curve_to_surface = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "project_curve_to_surface",

    "doc_html": """
        Projects one or more points onto one or more surfaces or polysurfaces.
    """,

    "syntax_html": """
        Rhino.ProjectCurveToSurface (strCurve, strSurface, arrDirection)
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "str",
            "doc": """
        The identifier of a curve object to project.
            """
        },
        1: {
            "name": "Curves",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of one or more curve objects to project.
            """
        },
        2: {
            "name": "Surface",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface or polysurface object to project onto.
            """
        },
        3: {
            "name": "Surfaces",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the surface or polysurface objects to project onto.
            """
        },
        4: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The direction (3-D vector) to project the points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the newly created, projected curve objects, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 891,

    "params_com": {
        0: {
            "name": "vaCurves",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSurfaces",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDirection",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


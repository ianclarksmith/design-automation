project_curve_to_surface = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ProjectCurveToSurface",
    "output_package_name": "curve",
    "output_module_name": "project_curve_to_surface",

    "doc_html": """
        Projects one or more points onto one or more surfaces or polysurfaces.
    """,

    "syntax_html": {
        0: ("strCurve", "strSurface", "arrDirection"),
        1: ("strCurve", "arrSurfaces", "arrDirection"),
        2: ("arrCurves", "strSurface", "arrDirection"),
        3: ("arrCurves", "arrSurfaces", "arrDirection"),
    },

    "params_html": {
        0: {
            "name": "arrCurves",
            "py_name": "curves",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Curves",
            "doc": """
        The identifiers of one or more curve objects to project.
            """
        },
        1: {
            "name": "arrSurfaces",
            "py_name": "surfaces",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Surfaces",
            "doc": """
        The identifiers of the surface or polysurface objects to project onto.
            """
        },
        2: {
            "name": "arrDirection",
            "py_name": "direction",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Direction",
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


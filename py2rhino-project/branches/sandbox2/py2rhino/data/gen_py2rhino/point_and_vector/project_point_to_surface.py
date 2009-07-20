project_point_to_surface = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "project_point_to_surface",

    "doc_html": """
        Projects one or more points onto one or more surfaces or polysurfaces.
    """,

    "syntax_html": """
        Rhino.ProjectPointToSurface (arrPoint, strSurface, arrDirection)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point to project.
            """
        },
        1: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points to project.
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
            "doc": "An array of 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 892,

    "params_com": {
        0: {
            "name": "vaPoints",
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


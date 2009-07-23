project_point_to_surface = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "ProjectPointToSurface",
    "output_package_name": "point_and_vector",
    "output_module_name": "project_point_to_surface",

    "doc_html": """
        Projects one or more points onto one or more surfaces or polysurfaces.
    """,

    "syntax_html": {
        0: ("arrPoint", "strSurface", "arrDirection"),
        1: ("arrPoint", "arrSurfaces", "arrDirection"),
        2: ("arrPoints", "strSurface", "arrDirection"),
        3: ("arrPoints", "arrSurfaces", "arrDirection"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Points",
            "doc": """
        An array of 3-D points to project.
            """
        },
        1: {
            "name": "arrSurfaces",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Surfaces",
            "doc": """
        The identifiers of the surface or polysurface objects to project onto.
            """
        },
        2: {
            "name": "arrDirection",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Direction",
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


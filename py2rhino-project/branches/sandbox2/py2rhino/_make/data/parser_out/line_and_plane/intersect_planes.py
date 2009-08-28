intersect_planes = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "IntersectPlanes",
    "output_package_name": "line_and_plane",
    "output_module_name": "intersect_planes",

    "doc_html": """
        Calculates the intersection of three planes.
    """,

    "syntax_html": {
        0: ("arrPlane1", "arrPlane2", "arrPlane3"),
    },

    "params_html": {
        0: {
            "name": "arrPlane1",
            "py_name": "plane_1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane1",
            "doc": """
        The first plane to intersect.
            """
        },
        1: {
            "name": "arrPlane2",
            "py_name": "plane_2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane2",
            "doc": """
        The second plane to intersect.
            """
        },
        2: {
            "name": "arrPlane3",
            "py_name": "plane_3",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane3",
            "doc": """
        The third plane to intersect.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D point of intersection is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 745,

    "params_com": {
        0: {
            "name": "vaPlaneA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlaneB",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPlaneC",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


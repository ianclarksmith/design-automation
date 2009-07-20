intersect_planes = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "IntersectPlanes",
    "output_package_name": "line_and_plane",
    "output_module_name": "intersect_planes",

    "doc_html": """
        
    """,

    "syntax_html": """
        Rhino.IntersectPlanes (arrPlane1, arrPlane2, arrPlane3)
    """,

    "params_html": {
        0: {
            "name": "Plane1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first plane to intersect.
            """
        },
        1: {
            "name": "Plane2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The second plane to intersect.
            """
        },
        2: {
            "name": "Plane3",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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


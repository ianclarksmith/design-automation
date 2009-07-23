line_line_intersection = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LineLineIntersection",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_line_intersection",

    "doc_html": """
        Calculates the intersection of two non-parallel.  Note, the two lines do not have to intersect for an intersection to be found.
		The default operation of this function assumes that the two lines are co-planar.  Thus, the return value is the intersection point of the two lines.
		But, two lines in three dimensions generally do not intersect at a point. They may be parallel (no intersections) or they may be coincident (infinite intersections). But, most often only their projection onto a plane intersects. When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3-D.
    """,

    "syntax_html": {
        0: ("arrLineA", "arrLineB", "blnPlanar"),
    },

    "params_html": {
        0: {
            "name": "arrLineA",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "LineA",
            "doc": """
        Two 3-D points identifying the starting and ending points of the first line.
            """
        },
        1: {
            "name": "arrLineB",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "LineB",
            "doc": """
        Two 3-D points identifying the starting and ending points of the second line.
            """
        },
        2: {
            "name": "blnPlanar",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Planar",
            "doc": """
        Assume that the two lines are co-planar. The default value is True.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnPlanar is omitted or True, then a single 3-D intersection point if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnPlanar is False, then an array containing a point on the first line and a point on the second line if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 736,

    "params_com": {
        0: {
            "name": "vaLine0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLine1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPlanar",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


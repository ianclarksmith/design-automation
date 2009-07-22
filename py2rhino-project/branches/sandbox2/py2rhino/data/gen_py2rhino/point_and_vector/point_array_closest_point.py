point_array_closest_point = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "PointArrayClosestPoint",
    "output_package_name": "point_and_vector",
    "output_module_name": "point_array_closest_point",

    "doc_html": """
        Finds the point in an array of 3-D points that is closest to a test point.
    """,

    "syntax_html": """
        Rhino.PointArrayClosestPoint (arrPoints, arrPoint)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array of 3-D points to test.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D test point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The index of the element in the point array that is closest to the test point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 742,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


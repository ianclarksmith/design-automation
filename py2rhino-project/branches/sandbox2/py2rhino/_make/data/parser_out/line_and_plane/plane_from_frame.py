plane_from_frame = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlaneFromFrame",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_from_frame",

    "doc_html": """
        Construct a plane from a point, and two vectors in the plane.
    """,

    "syntax_html": {
        0: ("arrOrigin", "arrXaxis", "arrYaxis"),
    },

    "params_html": {
        0: {
            "name": "arrOrigin",
            "py_name": "origin",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Origin",
            "doc": """
        A 3-D point identifying the origin of the plane.
            """
        },
        1: {
            "name": "arrXaxis",
            "py_name": "xaxis",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Xaxis",
            "doc": """
        A non-zero 3-D vector in the plane that determines the X axis direction.
            """
        },
        2: {
            "name": "arrYaxis",
            "py_name": "yaxis",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Yaxis",
            "doc": """
        A non-zero 3-D vector not parallel to arrXaxis that is used to determine the Y axis direction. Note, arrYaxis does not have to be perpendicular to arrXaxis.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 627,

    "params_com": {
        0: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


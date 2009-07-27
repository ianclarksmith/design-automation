surface_closest_point = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceClosestPoint",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_closest_point",

    "doc_html": """
        Returns the UV parameter of the point on a surface that is closest to a test point.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoint"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The test, or sampling, point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the U,V parameters of the closest point on the surface if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 215,

    "params_com": {
        0: {
            "name": "vaObject",
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


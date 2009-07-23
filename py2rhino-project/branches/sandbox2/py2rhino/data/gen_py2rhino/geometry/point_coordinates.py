point_coordinates = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "PointCoordinates",
    "output_package_name": "geometry",
    "output_module_name": "point_coordinates",

    "doc_html": """
        Returns or modifies the X, Y, and Z coordinates of a point object.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoint"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a point object.
            """
        },
        1: {
            "name": "arrPoint",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A new 3-D point location.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrPoint is not specified, the current 3-D point location if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrPoint is specified, the previous 3-D point location if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 130,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaNewPt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


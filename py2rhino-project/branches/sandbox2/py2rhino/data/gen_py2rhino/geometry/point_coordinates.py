point_coordinates = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "PointCoordinates",
    "output_package_name": "geometry",
    "output_module_name": "point_coordinates",

    "doc_html": """
        Returns or modifies the X, Y, and Z coordinates of a point object.
    """,

    "syntax_html": """
        Rhino.PointCoordinates (strObject [, arrPoint])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a point object.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
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


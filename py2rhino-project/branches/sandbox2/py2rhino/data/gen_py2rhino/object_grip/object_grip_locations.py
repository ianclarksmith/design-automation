object_grip_locations = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "ObjectGripLocations",
    "output_package_name": "object_grip",
    "output_module_name": "object_grip_locations",

    "doc_html": """
        Returns or modifies the location of all grips owned by an object. The locations of the grips are returned in an array of 3-D points with each position in the array corresponding to that grip's index. To modify the locations of grips, you must provide an array of 3-D points that contains the same number of points at grips.
    """,

    "syntax_html": """
        Rhino.ObjectGripLocations (strObject [, arrPoints])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Points",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        An array of 3-D points identifying the new locations of the grips.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrPoints is not specified, the current location of all grips if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrPoints is specified, the previous location of all grips if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 557,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


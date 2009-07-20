point_cloud_points = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "PointCloudPoints",
    "output_package_name": "geometry",
    "output_module_name": "point_cloud_points",

    "doc_html": """
        Returns the points of a point cloud object.
    """,

    "syntax_html": """
        Rhino.PointCloudPoints (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a point cloud object.
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

    "id_com": 129,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


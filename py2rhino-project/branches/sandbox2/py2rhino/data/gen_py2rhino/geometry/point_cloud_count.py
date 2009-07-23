point_cloud_count = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "PointCloudCount",
    "output_package_name": "geometry",
    "output_module_name": "point_cloud_count",

    "doc_html": """
        Returns the point count of a point cloud object.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a point cloud object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of points if successful"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 128,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


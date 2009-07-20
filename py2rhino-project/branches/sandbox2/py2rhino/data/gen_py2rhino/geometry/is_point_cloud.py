is_point_cloud = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "IsPointCloud",
    "output_package_name": "geometry",
    "output_module_name": "is_point_cloud",

    "doc_html": """
        Verifies an object is a point cloud object.
    """,

    "syntax_html": """
        Rhino.IsPointCloud (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if successful, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 121,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


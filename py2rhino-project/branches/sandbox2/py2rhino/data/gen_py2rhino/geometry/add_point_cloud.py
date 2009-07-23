add_point_cloud = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddPointCloud",
    "output_package_name": "geometry",
    "output_module_name": "add_point_cloud",

    "doc_html": """
        Adds a point cloud object to the document.
    """,

    "syntax_html": {
        0: ("arrPoints"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "py_name": "points",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Points",
            "doc": """
        An array of 3-D points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 69,

    "params_com": {
        0: {
            "name": "vaCloud",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


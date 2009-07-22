add_point_cloud = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddPointCloud",
    "output_package_name": "geometry",
    "output_module_name": "add_point_cloud",

    "doc_html": """
        Adds a point cloud object to the document.
    """,

    "syntax_html": """
        Rhino.AddPointCloud (arrPoints)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
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


project_point_to_mesh = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "ProjectPointToMesh",
    "output_package_name": "point_and_vector",
    "output_module_name": "project_point_to_mesh",

    "doc_html": """
        Projects one or more points onto one or more meshes.
    """,

    "syntax_html": {
        0: ("arrPoint", "strMesh", "arrDirection"),
        1: ("arrPoint", "arrMeshes", "arrDirection"),
        2: ("arrPoints", "strMesh", "arrDirection"),
        3: ("arrPoints", "arrMeshes", "arrDirection"),
    },

    "params_html": {
        0: {
            "name": "arrPoints",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Points",
            "doc": """
        An array of 3-D points to project.
            """
        },
        1: {
            "name": "arrMeshes",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Meshes",
            "doc": """
        The identifiers of the mesh objects to project onto.
            """
        },
        2: {
            "name": "arrDirection",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Direction",
            "doc": """
        The direction (3-D vector) to project the points.
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

    "id_com": 912,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMeshes",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDirection",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


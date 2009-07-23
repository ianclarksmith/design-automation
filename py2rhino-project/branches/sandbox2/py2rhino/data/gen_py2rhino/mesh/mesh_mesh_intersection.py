mesh_mesh_intersection = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshMeshIntersection",
    "output_package_name": "mesh",
    "output_module_name": "mesh_mesh_intersection",

    "doc_html": """
        Calculates the intersection of a mesh object with another mesh object.
    """,

    "syntax_html": {
        0: ("strMesh1", "strMesh2", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "strMesh1",
            "py_name": "mesh1",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Mesh1",
            "doc": """
        The identifier of the first mesh object.
            """
        },
        1: {
            "name": "strMesh2",
            "py_name": "mesh2",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Mesh2",
            "doc": """
        The identifier of the second mesh object.
            """
        },
        2: {
            "name": "dblTolerance",
            "py_name": "tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The intersection tolerance. Of omitted, Rhino's internal zero tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D point arrays that identify the vertices of the intersection curves (polylines) if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 749,

    "params_com": {
        0: {
            "name": "vaMesh0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMesh1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


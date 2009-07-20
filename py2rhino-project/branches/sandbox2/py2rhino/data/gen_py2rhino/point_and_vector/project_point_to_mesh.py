project_point_to_mesh = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "project_point_to_mesh",

    "doc_html": """
        Projects one or more points onto one or more meshes.
    """,

    "syntax_html": """
        Rhino.ProjectPointToMesh (arrPoint, strMesh, arrDirection)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point to project.
            """
        },
        1: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points to project.
            """
        },
        2: {
            "name": "Mesh",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the mesh object to project onto.
            """
        },
        3: {
            "name": "Meshes",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the mesh objects to project onto.
            """
        },
        4: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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


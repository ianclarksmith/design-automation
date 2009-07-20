disjoint_mesh_count = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "disjoint_mesh_count",

    "doc_html": """
        Returns the number of meshes that could be created by calling SplitDisjointMesh.
    """,

    "syntax_html": """
        Rhino.DisjointMeshCount (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a mesh object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of meshes that could be created if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 721,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


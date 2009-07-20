mesh_vertices = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_vertices",

    "doc_html": """
        Returns the vertices of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshVertices (strObject)
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
            "type": "array",
            "doc": "An array of 3-D points that define the vertices of the mesh if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 127,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


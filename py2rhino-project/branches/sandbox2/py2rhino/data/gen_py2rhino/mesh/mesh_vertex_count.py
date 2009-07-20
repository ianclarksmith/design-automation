mesh_vertex_count = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_vertex_count",

    "doc_html": """
        Returns the vertex count of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshVertexCount (strObject)
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
            "doc": "The number of mesh vertices if successful"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 126,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


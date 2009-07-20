mesh_face_vertices = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_face_vertices",

    "doc_html": """
        Returns the vertex indices of all faces of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshFaceVertices (strObject)
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
            "doc": "An array containing arrays of four numbers that define the vertex indices for each face of the mesh if successful.  Both quad and triangle faces are returned. If the third and forth vertex indices of a face are identical, the face is a triangle. Otherwise the face is a quad."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 495,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


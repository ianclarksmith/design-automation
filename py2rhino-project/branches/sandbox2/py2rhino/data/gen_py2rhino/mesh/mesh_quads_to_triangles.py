mesh_quads_to_triangles = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_quads_to_triangles",

    "doc_html": """
        Converts a mesh object's quad faces to triangles.
    """,

    "syntax_html": """
        Rhino.MeshQuadsToTriangles (strObject)
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
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 352,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


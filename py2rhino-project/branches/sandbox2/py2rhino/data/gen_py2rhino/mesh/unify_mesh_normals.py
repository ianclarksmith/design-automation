unify_mesh_normals = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "unify_mesh_normals",

    "doc_html": """
        Fixes inconsistencies in the directions of faces of a mesh object.
    """,

    "syntax_html": """
        Rhino.UnifyMeshNormals (strObject)
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
            "doc": "The number of faces that were modified if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 723,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


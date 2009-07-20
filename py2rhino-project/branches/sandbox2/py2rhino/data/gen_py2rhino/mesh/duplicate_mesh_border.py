duplicate_mesh_border = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "duplicate_mesh_border",

    "doc_html": """
        Creates a curve that duplicates a mesh border.
    """,

    "syntax_html": """
        Rhino.DuplicateMeshBorder (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the mesh object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the new curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 853,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


explode_meshes = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "explode_meshes",

    "doc_html": """
        Explodes a mesh object, or mesh objects,  into submeshes.  A submesh is a collection of mesh faces that are contained within a closed loop of unwelded mesh edges.  Unwelded mesh edges are edges where the mesh faces that share the edge have unique mesh vertices (not mesh topology vertices) at both ends of the edge.
    """,

    "syntax_html": """
        Rhino.ExplodeMeshes (strObject [, blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the mesh object to explode.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the mesh objects to explode.
            """
        },
        2: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Delete input objects after exploding.  The default is not to delete objects (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created mesh objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 903,

    "params_com": {
        0: {
            "name": "vaMeshes",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


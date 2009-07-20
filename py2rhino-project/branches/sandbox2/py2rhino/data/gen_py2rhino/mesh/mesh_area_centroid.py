mesh_area_centroid = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_area_centroid",

    "doc_html": """
        Calculates the area centroid of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshAreaCentroid (strObject)
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
            "doc": "A 3-D point identifying the area centroid if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 477,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


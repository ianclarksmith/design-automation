mesh_texture_coordinates = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "mesh_texture_coordinates",

    "doc_html": """
        Returns the normalized 2-D texture coordinates of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshTextureCoordinates (strObject)
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
            "doc": "An array of 2-D points that define the texture coordinates of the mesh if successful.  Each 2-D point is normalized, that is, each coordinate component ranges in value between 0 and 1.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the texture coordinate for each vertex return by MeshVertices."
        },
        1: {
            "type": "null",
            "doc": "If the mesh does not contain texture coordinates, if not successful, or on error."
        },
    },

    "id_com": 425,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


mesh_face_normals = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshFaceNormals",
    "output_package_name": "mesh",
    "output_module_name": "mesh_face_normals",

    "doc_html": """
        Returns the face unit normal for each face of a mesh object.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a mesh object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D vectors that define the face unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the unit normals for each face return by MeshFaces."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 569,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


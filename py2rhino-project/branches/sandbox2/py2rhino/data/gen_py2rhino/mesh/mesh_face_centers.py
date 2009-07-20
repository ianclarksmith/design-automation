mesh_face_centers = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshFaceCenters",
    "output_package_name": "mesh",
    "output_module_name": "mesh_face_centers",

    "doc_html": """
        Returns the center point of each face of a mesh object.
    """,

    "syntax_html": """
        Rhino.MeshFaceCenters (strObject)
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
            "doc": "An array of 3-D points that define the face center points of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the center points for each face return by MeshFaces."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 570,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


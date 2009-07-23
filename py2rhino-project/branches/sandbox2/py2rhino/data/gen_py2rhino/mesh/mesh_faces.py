mesh_faces = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "MeshFaces",
    "output_package_name": "mesh",
    "output_module_name": "mesh_faces",

    "doc_html": """
        Returns the face vertices of a mesh object.
    """,

    "syntax_html": {
        0: ("strObject", "blnFaceType"),
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
        1: {
            "name": "blnFaceType",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "FaceType",
            "doc": """
        The face type to be returned.  If omitted, both triangles and quads are returned (True)
		Value
		Description
		True
		Both triangles and quads.
		False
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points that define the face vertices of the mesh if successful.  If blnFaceType is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If blnFaceType is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 125,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaQuads",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


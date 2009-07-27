curve_mesh_intersection = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "CurveMeshIntersection",
    "output_package_name": "mesh",
    "output_module_name": "curve_mesh_intersection",

    "doc_html": """
        Calculates the intersection of a curve object and a mesh object.
    """,

    "syntax_html": {
        0: ("strCurve", "strMesh", "blnReturnFaces"),
    },

    "params_html": {
        0: {
            "name": "strCurve",
            "py_name": "curve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The identifier of the curve to intersect.
            """
        },
        1: {
            "name": "strMesh",
            "py_name": "mesh",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Mesh",
            "doc": """
        The identifier of the mesh to intersect.
            """
        },
        2: {
            "name": "blnReturnFaces",
            "py_name": "return_faces",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "ReturnFaces",
            "doc": """
        Return both intersection points and face indices.  If omitted or False, then just the intersection points are returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnReturnFaces is either omitted or False, then an array intersection points, if successful."
        },
        1: {
            "type": "array",
            "doc": "If blnReturnFaces is True, then a one-dimensional array containing information about each intersection if successful.  Each array element is a one-dimensional array that contains the following two elements:"
        },
        2: {
            "type": "array",
            "doc": "The 3-D intersection point."
        },
        3: {
            "type": "number",
            "doc": "The mesh face index on which the intersection point lies."
        },
        4: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 842,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaReturnFaces",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


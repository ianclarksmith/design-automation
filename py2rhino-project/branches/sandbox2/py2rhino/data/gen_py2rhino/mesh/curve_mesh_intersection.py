curve_mesh_intersection = {
    "module_name": "mesh",
    "class_name": "Mesh",
    "method_name": "curve_mesh_intersection",

    "doc_html": """
        Calculates the intersection of a curve object and a mesh object.
    """,

    "syntax_html": """
        Rhino.CurveMeshIntersection (strCurve, strMesh [, blnReturnFaces])
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve to intersect.
            """
        },
        1: {
            "name": "Mesh",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the mesh to intersect.
            """
        },
        2: {
            "name": "ReturnFaces",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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


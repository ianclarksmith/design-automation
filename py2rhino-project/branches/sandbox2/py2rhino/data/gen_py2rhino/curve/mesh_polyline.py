mesh_polyline = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "mesh_polyline",

    "doc_html": """
        Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.
    """,

    "syntax_html": """
        Rhino.MeshPolyline (strPolyline)
    """,

    "params_html": {
        0: {
            "name": "Polyline",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the polyline curve object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new polygon mesh object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 546,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


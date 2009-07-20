duplicate_edge_curves = {
    "module_name": "surface_and_polysurface",
    "class_name": "SurfaceAndPolysurface",
    "method_name": "duplicate_edge_curves",

    "doc_html": """
        Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.
    """,

    "syntax_html": """
        Rhino.DuplicateEdgeCurves (strObject [, blnSelect])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the surface or polysurface object.
            """
        },
        1: {
            "name": "Select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Select the duplicated edge curves.  The default is not to select (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 657,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


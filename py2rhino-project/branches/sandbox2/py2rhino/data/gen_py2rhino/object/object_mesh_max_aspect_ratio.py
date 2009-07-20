object_mesh_max_aspect_ratio = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_mesh_max_aspect_ratio",

    "doc_html": """
        Returns or modifies an object's custom render mesh parameter's maximum aspect ratio property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.ObjectMeshMaxAspectRatio (strObject [, dblRatio])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "Object",
            "type_string": "str",
            "doc": """
        The identifier of an object that has custom render mesh parameters.
            """
        },
        1: {
            "name": "Ratio",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If dblRatio is not specified, the current render mesh maximum aspect ratio if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If dblRatio is specified, the previous render mesh maximum aspect ratio if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 860,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRatio",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


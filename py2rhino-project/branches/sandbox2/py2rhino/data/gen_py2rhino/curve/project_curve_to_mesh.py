project_curve_to_mesh = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "project_curve_to_mesh",

    "doc_html": """
        Projects one or more points onto one or more meshes.
    """,

    "syntax_html": """
        Rhino.ProjectCurveToMesh (strCurve, strMesh, arrDirection)
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "str",
            "doc": """
        The identifier of a curve object to project.
            """
        },
        1: {
            "name": "Curves",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of one or more curve objects to project.
            """
        },
        2: {
            "name": "Mesh",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the mesh object to project onto.
            """
        },
        3: {
            "name": "Meshes",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The identifiers of the mesh objects to project onto.
            """
        },
        4: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The direction (3-D vector) to project the points.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the newly created, projected curve objects, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 911,

    "params_com": {
        0: {
            "name": "vaCurves",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMeshes",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDirection",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


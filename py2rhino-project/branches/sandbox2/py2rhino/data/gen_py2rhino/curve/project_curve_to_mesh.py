project_curve_to_mesh = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ProjectCurveToMesh",
    "output_package_name": "curve",
    "output_module_name": "project_curve_to_mesh",

    "doc_html": """
        Projects one or more points onto one or more meshes.
    """,

    "syntax_html": {
        0: ("strCurve", "strMesh", "arrDirection"),
        1: ("strCurve", "arrMeshes", "arrDirection"),
        2: ("arrCurves", "strMesh", "arrDirection"),
        3: ("arrCurves", "arrMeshes", "arrDirection"),
    },

    "params_html": {
        0: {
            "name": "arrCurves",
            "py_name": "curves",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Curves",
            "doc": """
        The identifiers of one or more curve objects to project.
            """
        },
        1: {
            "name": "arrMeshes",
            "py_name": "meshes",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Meshes",
            "doc": """
        The identifiers of the mesh objects to project onto.
            """
        },
        2: {
            "name": "arrDirection",
            "py_name": "direction",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Direction",
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


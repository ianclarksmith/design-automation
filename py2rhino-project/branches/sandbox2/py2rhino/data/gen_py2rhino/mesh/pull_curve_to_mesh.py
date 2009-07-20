pull_curve_to_mesh = {
    "input_folder_name": "Mesh_Methods",
    "input_file_name": "PullCurveToMesh",
    "output_package_name": "mesh",
    "output_module_name": "pull_curve_to_mesh",

    "doc_html": """
        Pulls a curve object to a mesh object. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the mesh.  Then it "connects the points" so  that you have a polyline on the mesh.
    """,

    "syntax_html": """
        Rhino.PullCurveToMesh (strMesh, strCurve)
    """,

    "params_html": {
        0: {
            "name": "Mesh",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the mesh object that pulls.
            """
        },
        1: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve object to pull.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new curve object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 719,

    "params_com": {
        0: {
            "name": "vaMesh",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


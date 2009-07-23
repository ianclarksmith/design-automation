explode_curves = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "ExplodeCurves",
    "output_package_name": "curve",
    "output_module_name": "explode_curves",

    "doc_html": """
        Explodes, or un-joins,  one more curve objects.  Polycurves will be exploded into curve segments.  Polylines will be exploded into line segments.  ExplodeCurves will return the curves in
		topological order.
    """,

    "syntax_html": {
        0: ("strObject", "blnDelete"),
        1: ("arrObjects", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_???",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the curve objects to explode.
            """
        },
        1: {
            "name": "blnDelete",
            "py_name": "delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete input objects after exploding.  The default is not to delete objects (False).
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

    "id_com": 446,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


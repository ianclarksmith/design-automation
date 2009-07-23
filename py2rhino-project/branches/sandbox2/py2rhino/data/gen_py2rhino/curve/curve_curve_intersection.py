curve_curve_intersection = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveCurveIntersection",
    "output_package_name": "curve",
    "output_module_name": "curve_curve_intersection",

    "doc_html": """
        Calculates the intersection of two curve objects.
    """,

    "syntax_html": {
        0: ("strObject1", "strObject2", "dblTolerance"),
    },

    "params_html": {
        0: {
            "name": "strObject1",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object1",
            "doc": """
        The identifier of the first curve object.
            """
        },
        1: {
            "name": "strObject2",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object2",
            "doc": """
        The identifier of the second curve object.  If omitted, the a self-intersection test will be performed on strObject1.
            """
        },
        2: {
            "name": "dblTolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Tolerance",
            "doc": """
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:"
        },
        1: {
            "type": "number",
            "doc": "The intersection event type, either Point (1) or Overlap (2)."
        },
        2: {
            "type": "number",
            "doc": "If the event type is Point (1), then the first curve parameter."
        },
        3: {
            "type": "number",
            "doc": "If the event type is Point (1), then the first curve parameter."
        },
        4: {
            "type": "number",
            "doc": "If the event type is Point (1), then the second curve parameter."
        },
        5: {
            "type": "number",
            "doc": "If the event type is Point (1), then the second curve parameter."
        },
        6: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 423,

    "params_com": {
        0: {
            "name": "vaCrvA",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCrvB",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


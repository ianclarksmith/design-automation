curve_area = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "CurveArea",
    "output_package_name": "curve",
    "output_module_name": "curve_area",

    "doc_html": """
        Returns that area of closed planar curves. The results are based on the current drawing units.
    """,

    "syntax_html": """
        Rhino.CurveArea (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a closed, planar curve object.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings containing the identifiers of one or more closed, planar curve objects.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of area information if successful.  The array will contain the following information:"
        },
        1: {
            "type": "number",
            "doc": "The area. If more than one curve was specified, the value will be the cumulative area."
        },
        2: {
            "type": "number",
            "doc": "The absolute (+/-) error bound for the area."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 643,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

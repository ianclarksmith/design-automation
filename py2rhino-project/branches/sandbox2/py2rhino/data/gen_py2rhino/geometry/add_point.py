add_point = {
    "module_name": "geometry",
    "class_name": "Geometry",
    "method_name": "add_point",

    "doc_html": """
        Adds a point object to the document.
    """,

    "syntax_html": """
        Rhino.AddPoint (arrPoint)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 68,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


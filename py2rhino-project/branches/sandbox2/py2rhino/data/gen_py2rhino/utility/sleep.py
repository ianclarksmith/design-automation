sleep = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "sleep",

    "doc_html": """
        Suspends the execution of a running script for the specified interval.
    """,

    "syntax_html": """
        Rhino.Sleep (lngMilliseconds)
    """,

    "params_html": {
        0: {
            "name": "Milliseconds",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The duration in milliseconds.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "If successful, or on error."
        },
    },

    "id_com": 248,

    "params_com": {
        0: {
            "name": "vaTime",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


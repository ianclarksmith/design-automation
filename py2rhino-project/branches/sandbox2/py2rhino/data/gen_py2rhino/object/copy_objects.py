copy_objects = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "copy_objects",

    "doc_html": """
        Copies one or more objects from one location to another, or in-place.
    """,

    "syntax_html": """
        Rhino.CopyObjects (arrObjects [, arrStart , arrEnd])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to copy.
            """
        },
        1: {
            "name": "Start",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D starting, or base, point of the copy operation.  If omitted, the objects are copied in-place.
            """
        },
        2: {
            "name": "End",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D ending point of the copy operation.
            """
        },
        3: {
            "name": "Translation",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D translation vector.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the copied objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 295,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


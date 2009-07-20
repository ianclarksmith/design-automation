copy_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "CopyObject",
    "output_package_name": "object",
    "output_module_name": "copy_object",

    "doc_html": """
        Copies a single object from one location to another, or in-place.
    """,

    "syntax_html": """
        Rhino.CopyObject (strObject [, arrStart , arrEnd])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to copy.
            """
        },
        1: {
            "name": "Start",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
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
            "type": "string",
            "doc": "The identifier of the copied object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 184,

    "params_com": {
        0: {
            "name": "vaObject",
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


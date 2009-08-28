object_name = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectName",
    "output_package_name": "object",
    "output_module_name": "object_name",

    "doc_html": """
        Returns or modifies the user-definable name of an object.
    """,

    "syntax_html": {
        0: ("strObject", "strName"),
        1: ("arrObjects", "strName"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        1: {
            "name": "strName",
            "py_name": "name",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Name",
            "doc": """
        The new object name.  If omitted, the current object name is returned.  Note, if arrObjects is specified, strName is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If an object name is not specified,  the current object name if successful."
        },
        1: {
            "type": "string",
            "doc": "If an object name is specified,  the previous object name if successful."
        },
        2: {
            "type": "number",
            "doc": "If arrObjects is specified, then the number of objects modified if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 196,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


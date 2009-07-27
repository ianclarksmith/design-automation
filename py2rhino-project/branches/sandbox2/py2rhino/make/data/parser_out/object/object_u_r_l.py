object_u_r_l = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectURL",
    "output_package_name": "object",
    "output_module_name": "object_u_r_l",

    "doc_html": """
        Returns or modifies the user-definable URL of an object.
    """,

    "syntax_html": {
        0: ("strObject", "strURL"),
        1: ("arrObjects", "strURL"),
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
            "name": "strURL",
            "py_name": "u_r_l",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "URL",
            "doc": """
        The new object URL.  If omitted, the current object URL is returned.  Note, if arrObjects is specified, strURL is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If an object URL is not specified,  the current object URL if successful."
        },
        1: {
            "type": "string",
            "doc": "If an object URL is specified,  the previous object URL if successful."
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

    "id_com": 199,

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


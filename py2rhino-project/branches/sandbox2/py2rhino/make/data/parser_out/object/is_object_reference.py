is_object_reference = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "IsObjectReference",
    "output_package_name": "object",
    "output_module_name": "is_object_reference",

    "doc_html": """
        Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.
    """,

    "syntax_html": {
        0: ("strObject"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of an object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 271,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


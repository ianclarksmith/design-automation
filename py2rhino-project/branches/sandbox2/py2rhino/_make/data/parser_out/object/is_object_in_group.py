is_object_in_group = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "IsObjectInGroup",
    "output_package_name": "object",
    "output_module_name": "is_object_in_group",

    "doc_html": """
        Verifies that an object is a member of a specified group.
    """,

    "syntax_html": {
        0: ("strObject", "strGroup"),
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
        1: {
            "name": "strGroup",
            "py_name": "group",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Group",
            "doc": """
        The name of a group.  If omitted, the function verifies that the object is a member of any group.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 188,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaGroup",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


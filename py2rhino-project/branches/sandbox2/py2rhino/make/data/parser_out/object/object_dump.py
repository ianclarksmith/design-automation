object_dump = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectDump",
    "output_package_name": "object",
    "output_module_name": "object_dump",

    "doc_html": """
        Returns a detailed description of an object.
    """,

    "syntax_html": {
        0: ("strObject", "intType"),
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
        The identifier of the object.
            """
        },
        1: {
            "name": "intType",
            "py_name": "type",
            "opt_or_req": "Optional",
            "type": "The type of dump",
            "name_prefix": "int",
            "name_main": "Type",
            "doc": """
        The acceptable values are as follows:
		Value
		Description
		0 (Default)
		Returns both geometry and attribute details. This is equivalent to the results of the What command.
		1
		Returns geometry details.
		2
		Returns attribute details.
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "A detailed description of the object is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 705,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaType",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


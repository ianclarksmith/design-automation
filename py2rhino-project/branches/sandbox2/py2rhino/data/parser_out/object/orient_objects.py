orient_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "OrientObjects",
    "output_package_name": "object",
    "output_module_name": "orient_objects",

    "doc_html": """
        Orients one or more objects based on input points.
    """,

    "syntax_html": {
        0: ("arrObjects", "arrReference", "arrTarget", "intFlags"),
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
        An array of strings identifying the objects to orient.
            """
        },
        1: {
            "name": "arrReference",
            "py_name": "reference",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Reference",
            "doc": """
        An array of 3-D reference points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
            """
        },
        2: {
            "name": "arrTarget",
            "py_name": "target",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Target",
            "doc": """
        An array of 3-D target points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
            """
        },
        3: {
            "name": "intFlags",
            "py_name": "flags",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Flags",
            "doc": """
        The orient flags.  Values can be added together to specify multiple options.
		Value
		Description
		1
		Copy object.  The default is not to copy the objects.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the oriented objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 391,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFrom",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaTo",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaFlags",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


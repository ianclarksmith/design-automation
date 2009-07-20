orient_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "orient_object",

    "doc_html": """
        Orients a single object based on input points.
    """,

    "syntax_html": """
        Rhino.OrientObject (strObject, arrReference, arrTarget [, intFlags])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to orient.
            """
        },
        1: {
            "name": "Reference",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D reference points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
            """
        },
        2: {
            "name": "Target",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D target points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
            """
        },
        3: {
            "name": "Flags",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The orient flags.  Values can be added together to specify multiple options.
		Value
		Description
		1
		Copy object.  The default is not to copy the object.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the oriented object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 390,

    "params_com": {
        0: {
            "name": "vaObject",
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


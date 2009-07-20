object_mesh_settings = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_mesh_settings",

    "doc_html": """
        Returns or sets the render mesh settings of an object's custom render mesh parameters.
    """,

    "syntax_html": """
        Rhino.ObjectMeshSettings (strObject [, intSettings])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "Object",
            "type_string": "str",
            "doc": """
        The identifier of an object that has custom render mesh parameters.
            """
        },
        1: {
            "name": "Settings",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 15.  The bit values are as follows:
		Value
		Description
		0
		No settings enabled.
		1
		Refine mesh enabled.
		2
		Jagged seams enabled.
		4
		Simple planes enabled.
		8
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If intSettings is not specified, the current render mesh settings if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If intSettings is specified, the previous render mesh settings if successful."
        },
        2: {
            "type": "null",
            "doc": "If the object does not have custom render mesh parameters, or on error."
        },
    },

    "id_com": 865,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFlags",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


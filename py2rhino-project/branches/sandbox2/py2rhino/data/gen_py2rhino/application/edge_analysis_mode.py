edge_analysis_mode = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "edge_analysis_mode",

    "doc_html": """
        Returns or modifies edge analysis mode displayed by the ShowEdges command.
    """,

    "syntax_html": """
        Rhino.EdgeAnalysisMode ([intMode])
    """,

    "params_html": {
        0: {
            "name": "Mode",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The new display mode.  If omitted, the current display mode is returned.  The available mores are as follows:
		0
		Display all edges.
		1
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a intMode is not specified, the current edge analysis display mode if successful."
        },
        1: {
            "type": "number",
            "doc": "If a intMode is specified, the previous edge analysis display mode if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 448,

    "params_com": {
        0: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


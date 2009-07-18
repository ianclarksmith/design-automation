edge_analysis_mode = {

    "class": "Application",
    "method": "edge_analysis_mode",
    "doc": """
        Returns or modifies edge analysis mode displayed by the ShowEdges command.
    """,

    "syntax": """
        Rhino.EdgeAnalysisMode ([intMode])
    """,

    "params": {
        0: {
            "name": "mode",
            "optional": True,
            "type_vb": "number",
            "type_string": "int",
            "doc": """
        The new display mode.  If omitted, the current display mode is returned.  The available mores are as follows:
		0
		Display all edges.
		1
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Number",
            "doc": "If a intMode is not specified, the current edge analysis display mode if successful."
        },
        1: {
            "type_vb": "Number",
            "doc": "If a intMode is specified, the previous edge analysis display mode if successful."
        },
        2: {
            "type_vb": "Null",
            "doc": "If not successful, or on error."
        },
    }

}


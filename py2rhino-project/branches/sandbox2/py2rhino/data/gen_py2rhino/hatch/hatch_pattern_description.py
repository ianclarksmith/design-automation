hatch_pattern_description = {
    "module_name": "hatch",
    "class_name": "Hatch",
    "method_name": "hatch_pattern_description",

    "doc_html": """
        Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions for descriptions are optional.
    """,

    "syntax_html": """
        Rhino.HatchPatternDescription (strHatch)
    """,

    "params_html": {
        0: {
            "name": "Hatch",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing hatch pattern.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If hatch pattern's description if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 829,

    "params_com": {
        0: {
            "name": "vaHatch",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


unit_custom_unit_system = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "unit_custom_unit_system",

    "doc_html": """
        Sets the document's units system to a user-defined system.  This overrides the units system set using the UnitSystem method.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": """
        Rhino.UnitCustomUnitSystem (dblUnits [, blnScale [, strName]])
    """,

    "params_html": {
        0: {
            "name": "Units",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The number of units per meter.
            """
        },
        1: {
            "name": "Scale",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Scale existing geometry based on the new unit system.  If not specified, any existing geometry is not scaled (False).
            """
        },
        2: {
            "name": "Name",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new unit system.  If not specified, the name "Custom" will be assigned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The previous units system if successful.  See UnitSystem for details."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 326,

    "params_com": {
        0: {
            "name": "vaValue",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaScale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaName",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


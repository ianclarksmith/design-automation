unit_custom_unit_system = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitCustomUnitSystem",
    "output_package_name": "document",
    "output_module_name": "unit_custom_unit_system",

    "doc_html": """
        Sets the document's units system to a user-defined system.  This overrides the units system set using the UnitSystem method.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": {
        0: ("dblUnits", "blnScale", "strName"),
    },

    "params_html": {
        0: {
            "name": "dblUnits",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Units",
            "doc": """
        The number of units per meter.
            """
        },
        1: {
            "name": "blnScale",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Scale",
            "doc": """
        Scale existing geometry based on the new unit system.  If not specified, any existing geometry is not scaled (False).
            """
        },
        2: {
            "name": "strName",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Name",
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


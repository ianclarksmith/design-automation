object_print_width_source = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_print_width_source",

    "doc_html": """
        Returns or modifies the print width source of an object.  The width used to print objects is specified in one of three ways:
		1. Print width from layer.  Use the print width assigned to the object's layer.
		2. Print width from object.  Use the print width that is assigned to the object.
		3. Print width from parent.  For objects with parents, like objects in block instances, use parent's print width.  If no parent, treats as print width from layer.
    """,

    "syntax_html": """
        Rhino.ObjectPrintWidthSource (strObject [, intSource])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        2: {
            "name": "Source",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The new print width source.  If omitted, the current print width source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Print width by layer.
		1
		Print width by object.
		2
		<unused>
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a print width source is not specified,  the current width source if successful."
        },
        1: {
            "type": "number",
            "doc": "If a print width source is specified, the previous width source if successful."
        },
        2: {
            "type": "number",
            "doc": "If arrObjects is specified, then the number of objects modified if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 808,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSource",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


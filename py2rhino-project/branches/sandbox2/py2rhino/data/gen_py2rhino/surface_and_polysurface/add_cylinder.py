add_cylinder = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddCylinder",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_cylinder",

    "doc_html": """
        Adds a cylinder-shaped polysurface to the document.
    """,

    "syntax_html": """
        Rhino.AddCylinder (arrBase, arrHeight, dblRadius [, blnCap])
    """,

    "params_html": {
        0: {
            "name": "Base",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D base point of the cylinder.
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The base plane of the cylinder.
            """
        },
        2: {
            "name": "Height",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D height point of the cylinder.  The height point defines the height and direction of the cylinder.
            """
        },
        3: {
            "name": "Height",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The height of the cylinder.
            """
        },
        4: {
            "name": "Radius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The radius of the cylinder.
            """
        },
        5: {
            "name": "Cap",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Cap the ends of the cylinder.  If omitted, the ends of the cylinder will be capped (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 73,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaHeight",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCap",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


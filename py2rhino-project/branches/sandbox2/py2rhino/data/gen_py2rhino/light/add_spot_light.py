add_spot_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "AddSpotLight",
    "output_package_name": "light",
    "output_module_name": "add_spot_light",

    "doc_html": """
        Adds a new spot light object  to the document.
    """,

    "syntax_html": """
        Rhino.AddSpotLight (arrOrigin, dblRadius, arrApex)
    """,

    "params_html": {
        0: {
            "name": "Origin",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D origin point of the light.
            """
        },
        1: {
            "name": "Radius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The radius of the cone.
            """
        },
        2: {
            "name": "Apex",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D apex point of the light.
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

    "id_com": 157,

    "params_com": {
        0: {
            "name": "vaBase",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaApex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


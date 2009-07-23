add_spot_light = {
    "input_folder_name": "Light_Methods",
    "input_file_name": "AddSpotLight",
    "output_package_name": "light",
    "output_module_name": "add_spot_light",

    "doc_html": """
        Adds a new spot light object  to the document.
    """,

    "syntax_html": {
        0: ("arrOrigin", "dblRadius", "arrApex"),
    },

    "params_html": {
        0: {
            "name": "arrOrigin",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Origin",
            "doc": """
        The 3-D origin point of the light.
            """
        },
        1: {
            "name": "dblRadius",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
            "doc": """
        The radius of the cone.
            """
        },
        2: {
            "name": "arrApex",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Apex",
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


objects_by_color = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "ObjectsByColor",
    "output_package_name": "selection",
    "output_module_name": "objects_by_color",

    "doc_html": """
        Returns the identifiers of all objects based on the objects' color.  Object colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": {
        0: ("lngColor", "blnSelect", "blnIncludeLights"),
    },

    "params_html": {
        0: {
            "name": "lngColor",
            "py_name": "color",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "lng",
            "name_main": "Color",
            "doc": """
        An RGB color value.
            """
        },
        1: {
            "name": "blnSelect",
            "py_name": "select",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
            "doc": """
        Select the objects.  If omitted, the objects are not selected (False).
            """
        },
        2: {
            "name": "blnIncludeLights",
            "py_name": "include_lights",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "IncludeLights",
            "doc": """
        Include light objects.  If omitted, light objects are not returned (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 37,

    "params_com": {
        0: {
            "name": "vaColor",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaIncludeLights",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}


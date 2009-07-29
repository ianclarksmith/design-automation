            
def w(f, text, tabs = 0, nls=0, nle=1):
    if isinstance(text, tuple):
        text = list(text)
    if not isinstance(text, list):
        text = [text]
    if tabs != 0:
        tab_str = ["    " * tabs]
        text = tab_str + text
    if nls != 0:
        nls_str = ["\n" * nls]
        text =  nls_str + text          
    if nle != 0:
        nle_str = ["\n" * nle]
        text = text + nle_str
    f.writelines(text)


def camel_to_underscore(name_cc):
    name_us = ""
    #get list of letters
    for i in range(len(name_cc)):
        if (name_cc[i].isupper() or name_cc[i].isdigit()):
            name_us += "_"
            name_us += name_cc[i].lower()
        else:
            name_us += name_cc[i]
    #check we are not starting with an underscore
    if name_us.startswith("_"):
        name_us = name_us[1:]
    return name_us

def underscore_to_camel(name_us):
    return ''.join(map(lambda i: i.capitalize(), name_us.split("_")))

#type map for params
string_to_type_map = {
    "bln":"Boolean",
    "int":"Integer",        
    "lng":"Integer",
    "dbl":"Double",
    "str":"String",
    "array_of bln":"Array of Booleans",
    "array_of int":"Array of Integers",
    "array_of lng":"Array of Integers",        
    "array_of dbl":"Array of Doubles",
    "array_of str":"Array of Strings",       
    "array_of any":"Array of Generic Objects",
    #"array_of ???":"Array of ???", 
    "va":"Variant",
    "n":"Integer",
    #"arr":"Array of ????"
}

#mapping from type to magic numbers
#VT_I2 = 2 = signed short
#VT_I4 = 3 = signed long
#VT_R4 = 4 = signed float
#VT_R8 = 5 = signed double  
string_to_magic_map = {
    "bln":"VT_BOOL",
    "int":"VT_I2",        
    "lng":"VT_I4",
    "dbl":"VT_R8",
    "str":"VT_BSTR",
    "array_of bln":"VT_ARRAY + VT_BOOL",
    "array_of int":"VT_ARRAY + VT_I2",
    "array_of lng":"VT_ARRAY + VT_I4",  
    "array_of dbl":"VT_ARRAY + VT_R8",
    "array_of str":"VT_VARIANT",
    "array_of any":"VT_VARIANT",       
    #"array_of ???":"VT_VARIANT",               
    "va":"VT_VARIANT",
    "n":"VT_I2",
    #"arr":"VT_VARIANT"
}
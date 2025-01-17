first_transform =\
"""    Transform [
        0.482906 0 0 0
        0 0.482906 0 0
        0 0 0.482906 0
        0.0571719 0.213656 0.0682078 1
        ]
"""

second_transform =\
"""    Transform [
        0.482906 0 0 0
        0 0.482906 0 0
        0 0 0.482906 0
        0.156382 0.777229 0.161698 1  ]
"""

third_transform =\
"""    Transform [
        0.482906 0 0 0
        0 0.482906 0 0
        0 0 0.482906 0
        0.110507 0.494301 0.126194 1  ]
"""


attribute_begin = "AttributeBegin\n"
attribute_end = "AttributeEnd\n"

def generate(translate, first_material_name, second_material_name):
    first_object =\
        'NamedMaterial "{}"\n'.format(first_material_name) +\
        attribute_begin + first_transform + attribute_begin +\
        translate +\
        '    Shape "plymesh"\n' +\
        '        "string filename" [ "models/Mesh001.ply" ]\n'+\
        attribute_end +\
        attribute_end + '\n'

    second_object =\
        attribute_begin + second_transform + attribute_begin +\
        translate +\
        '    Shape "plymesh"\n' +\
        '        "string filename" [ "models/Mesh002.ply" ]\n'+\
        attribute_end +\
        attribute_end + '\n'

    third_object =\
        'NamedMaterial "{}"\n'.format(second_material_name) +\
        attribute_begin + third_transform + attribute_begin +\
        translate +\
        '    Shape "plymesh"\n' +\
        '        "string filename" [ "models/Mesh000.ply" ]\n'+\
        attribute_end +\
        attribute_end + '\n'

    return first_object + second_object + third_object


for token in [\
    ("-5 0 -5\n", "ShareMaterialCoatedDiffuse", "Stand"),\
    ("0 0 0\n", "ShareMaterialConductor", "Stand"),\
    ("5 0 5\n", "ShareMaterialCoatedDiffuse", "Stand"),\
    ]:
    coord, first_material, second_material = token
    translate = "    Translate " + coord
    print(generate(translate, first_material, second_material))



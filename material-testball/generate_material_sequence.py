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

unit_y = 4.5
unit_x = 3

def generate_coord(x):
    up   = [-x * unit_x - unit_y, 0, unit_x * x - unit_y]
    mid  = [-x * unit_x,          0, unit_x * x  ]
    down = [-x * unit_x + unit_y, 0, unit_x * x + unit_y]

    return [up, mid, down]

diffuse_row = [\
    (generate_coord(-2.5)[0], "DiffuseAlpha", "GreyStand"),
    (generate_coord(-2.5)[1], "DiffuseBeta", "GreyStand"),
    (generate_coord(-2.5)[2], "DiffuseDelta", "GreyStand"),
]

diffuse_transmission_row = [\
    (generate_coord(-2)[0], "DiffuseTransmissionAlpha", "GreyStand"),
    (generate_coord(-2)[1], "DiffuseTransmissionBeta", "GreyStand"),
    (generate_coord(-2)[2], "DiffuseTransmissionDelta", "GreyStand"),
]

coated_diffuse_row = [\
    (generate_coord(-1)[0], "CoatedDiffuseAlpha", "GreyStand"),
    (generate_coord(-1)[1], "CoatedDiffuseBeta", "GreyStand"),
    (generate_coord(-1)[2], "CoatedDiffuseDelta", "GreyStand"),
]

dielectric_row = [\
    (generate_coord(0)[0], "DielectricAlpha", "RedStand"),
    (generate_coord(0)[1], "DielectricBeta", "BlueStand"),
    (generate_coord(0)[2], "DielectricDelta", "GreenStand"),
]

conductor_row = [\
    (generate_coord(1)[0], "Copper", "GreyStand"),
    (generate_coord(1)[1], "Silver", "GreyStand"),
    (generate_coord(1)[2], "Gold",   "GreyStand"),
]

coated_conductor_row = [\
    (generate_coord(2)[0], "CoatedCopper", "GreyStand"),
    (generate_coord(2)[1], "CoatedSilver", "GreyStand"),
    (generate_coord(2)[2], "CoatedGold",   "GreyStand"),
]


for token in  diffuse_transmission_row + coated_diffuse_row + dielectric_row + conductor_row + coated_conductor_row:
    coord, first_material, second_material = token
    x, y, z = coord
    translate = "    Translate {} {} {}\n".format(x, y, z)
    print(generate(translate, first_material, second_material))

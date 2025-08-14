second_transform =\
"""    Transform [
        0.482906 0 0 0
        0 0.482906 0 0
        0 0 0.482906 0
        0.156382 0.777229 0.161698 1  ]
"""

attribute_begin = "AttributeBegin\n"
attribute_end = "AttributeEnd\n"

'''
Material "interface"
MediumInterface "fog" ""

Shape "sphere"
    "float radius" [ 90 ]
'''

def make_medium(id, sigma_a, sigma_s):
    return \
    'MakeNamedMedium "{}"\n'.format(id) +\
        '"string type" [ "homogeneous" ]\n' +\
        '"float scale" [ 1 ]\n' +\
        '"rgb sigma_a" [ {0} {0} {0} ]\n'.format(sigma_a) +\
        '"rgb sigma_s" [ {0} {0} {0} ]\n'.format(sigma_s)

def generate_sphere(translate, id, sigma_a, sigma_s):
    silver =\
        attribute_begin + second_transform + attribute_begin +\
        translate +\
        make_medium(id, sigma_a, sigma_s) +\
        '    Material "interface"\n' +\
        '    MediumInterface "{}" ""\n'.format(id) +\
        '    Shape "sphere"\n' +\
        '        "float radius" [ 1.3 ]\n' +\
        attribute_end +\
        attribute_end

    return silver

unit_y = 3.2
unit_x = 2.8

offset = -0.5

def generate_coord(x, y):
    return [offset -x * unit_x  + y * unit_y, 0, offset + unit_x * x  + y * unit_y]

x_size = 5
y_size = 5

counter = 0;
for x in range(x_size):
    for y in range(y_size):
        coord = generate_coord(x-2, y-2)
        translate = "    Translate {} {} {}\n".format(coord[0], coord[1], coord[2])
        name = "fog_{}".format(counter)
        #sigma_a = (1.0 - float(x) / x_size) * 3
        sigma_a = (float(x) / x_size) * 3
        sigma_s = (1.0 - float(y) / y_size )* 3
        print(generate_sphere(translate, name, sigma_a, sigma_s))
        counter += 1

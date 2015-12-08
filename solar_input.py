# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):


    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue 
            object_type = line.split()[0].lower()
            if object_type == "star":  
                star = Star()
                parse_star_p(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_p(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects

def parse_star_p(line, star):

    p = line.split(" ")
    if p[0] == "Star":
        star.R = float(p[1])
        star.color = str(p[2])
        star.m = float(p[3])
        star.x = float(p[4])
        star.y = float(p[5])
        star.Vx = float(p[6])
        star.Vy = float(p[7])
        print(star.x, star.y)

def parse_planet_p(line, planet):

    parameters = line.split(" ")
    if parameters[0] == "Planet":
        planet.R = float(p[1])
        planet.color = str(p[2])
        planet.m = float(p[3])
        planet.x = float(p[4])
        planet.y = float(p[5])
        planet.Vx = float(p[6])
        planet.Vy = float(p[7])


def write_space_objects_data_to_file(output_filename, space_objects):

    with open("output_filename", 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %f %s %f %f %f %f %f" % (obj.type,obj.R,obj.color, obj.m, obj.x,obj.y,obj.Vx,obj.Vy ))
           


if __name__ == "__main__":
    print("This module is not for direct call!")




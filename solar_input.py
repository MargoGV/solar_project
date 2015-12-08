# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: я отфиксил
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):

    parameters = line.split(" ")
    if parameters[0] == "Star":
        star.R = float(parameters[1])
        star.color = str(parameters[2])
        star.m = float(parameters[3])
        star.x = float(parameters[4])
        star.y = float(parameters[5])
        star.Vx = float(parameters[6])
        star.Vy = float(parameters[7])
        print(star.x, star.y)


def parse_planet_parameters(line, planet):

    parameters = line.split(" ")
    if parameters[0] == "Planet":
        planet.R = float(parameters[1])
        planet.color = str(parameters[2])
        planet.m = float(parameters[3])
        planet.x = float(parameters[4])
        planet.y = float(parameters[5])
        planet.Vx = float(parameters[6])
        planet.Vy = float(parameters[7])



def write_space_objects_data_to_file(output_filename, space_objects):

    with open("output_filename", 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %f %s %f %f %f %f %f" % (obj.type,obj.R,obj.color, obj.m, obj.x,obj.y,obj.Vx,obj.Vy ))


if __name__ == "__main__":
    print("This module is not for direct call!")




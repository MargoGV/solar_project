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
                parse_star_parameters(line, star)
                objects.append(star)
            object_type = line.split()[0].lower()
            if object_type == "planet":  
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
	A = line.split()
	star.r= int(A[1])
	star.color= A[2]
	star.m= float(A[3])
	star.x= float(A[4])
	star.y= float(A[5])
	star.Vx= float(A[6])
	star.Vy= float(A[7])


def parse_planet_parameters(line, planet):
	A = line.split()
	planet.r= int(A[1])
	planet.color= A[2]
	planet.m= float(A[3])
	planet.x= float(A[4])
	planet.y= float(A[5])
	planet.Vx= float(A[6])
	planet.Vy= float(A[7])



def write_space_objects_data_to_file(output_filename, space_objects):
    with open(output_filename, 'w') as out_file:
        for obj in objects:
            print(out_file,(obj.type, obj.r, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))#iDon'tknow,howtoFIXthisBUG,yet.


if __name__ == "__main__":
    print("This module is not for direct call!")





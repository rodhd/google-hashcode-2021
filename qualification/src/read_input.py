def read_header(param):
    split = param.split(' ')
    return {
        'duration': int(split[0]),
        'no_of_intersections': int(split[1]),
        'no_of_streets': int(split[2]),
        'no_of_cars': int(split[3]),
        'score_bonus': int(split[4])
    }


def read_streets(param):
    split = param.split(' ')
    return {
        'start': int(split[0]),
        'end': int(split[1]),
        'name': split[2],
        'length': int(split[3])
    }


def read_cars(param):
    split = param.split(' ')
    return {
        'no_of_streets': int(split[0]),
        'path': list(map(lambda x: x.replace('\n', ''), split[1:]))
    }


def get_intersections(streets):
    intersections = dict()
    for s in streets:
        if(s['start'] not in intersections):
            intersections[s['start']] = {
                'inbound': list(),
                'outbound': list()
            }
        if (s['end'] not in intersections):
            intersections[s['end']] = {
                'inbound': list(),
                'outbound': list()
            }
        intersections[s['start']]['outbound'].append(s['name'])
        intersections[s['end']]['inbound'].append(s['name'])
    return intersections


def read_problem(file_path):
    with open(file_path) as reader:
        lines = reader.readlines()
    header = read_header(lines[0])
    streets = list(map(lambda x: read_streets(x), lines[1:1+header["no_of_streets"]]))
    cars = list(map(lambda x: read_cars(x), lines[1+header["no_of_streets"]:]))
    intersections = get_intersections(streets)
    return {
        'header': header,
        'streets': streets,
        'cars': cars,
        'intersections': intersections
    }


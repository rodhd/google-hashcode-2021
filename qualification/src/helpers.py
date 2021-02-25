def naive_solution(intersections, output):
    with open(f"./out/{output}.out", 'w') as out:
        out.write(f"{len(intersections)}\n")

        for key, value in intersections.items():
            out.write(f"{key}\n")
            out.write(f"{len(value.get('inbound'))}\n")

            for i in value.get('inbound'):
                out.write(f"{i} 1\n")


def dead_streets_solution(context, output):
    traversed_streets = set()
    for c in context.get('cars'):
        for s in c.get('path'):
            traversed_streets.add(s)
    intersections = context.get('intersections')

    for key, value in intersections.items():
        value['active_intersections'] = intersect(value['inbound'], traversed_streets)

    active_intersections = len(list(filter(lambda x: len(x[1].get('active_intersections')), intersections.items())))

    with open(f"./out/{output}.out", 'w') as out:
        out.write(f"{active_intersections}\n")

        for key, value in intersections.items():
            if len(value.get('active_intersections')) > 0:
                out.write(f"{key}\n")
                out.write(f"{len(value.get('active_intersections'))}\n")

                for i in value.get('active_intersections'):
                    out.write(f"{i} 1\n")


def intersect(lst1, lst2):
    return list(set(lst1) & set(lst2))


def most_traversed_weighted(context, output):
    traversed_streets = set()
    for c in context.get('cars'):
        for s in c.get('path'):
            traversed_streets.add(s)
    intersections = context.get('intersections')

    for key, value in intersections.items():
        value['active_intersections'] = intersect(value['inbound'], traversed_streets)

    active_intersections = len(list(filter(lambda x: len(x[1].get('active_intersections')), intersections.items())))

    cars = context.get('cars')
    streets = context.get('streets')

    for s in streets:
        traffic = len(list(filter(lambda c: s['name'] in c['path'], cars)))
        s['traffic'] = traffic

    sorted_streets = sorted(streets, key=lambda x: x.get('traffic'))
    n_s = int(round(len(streets)/2))
    upper_half = list(map(lambda x: x.get('name'), sorted_streets[n_s:]))

    with open(f"./out/{output}.out", 'w') as out:
        out.write(f"{active_intersections}\n")

        for key, value in intersections.items():
            if len(value.get('active_intersections')) > 0:
                out.write(f"{key}\n")
                out.write(f"{len(value.get('active_intersections'))}\n")

                for i in value.get('active_intersections'):
                    if i in upper_half:
                        out.write(f"{i} 2\n")
                    else:
                        out.write(f"{i} 1\n")
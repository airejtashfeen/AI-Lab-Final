def is_valid(region, neighbors, color, assignment):

    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor]==color:
            return False
    return True

def solve_map_coloring(assignment, regions, colors, neighbors):
 if len(assignment)==len(regions):
     return True
 
 #checking the solution that satisfies constraints

 for region in regions:
    if region not in assignment:
        for color in colors:
            if is_valid(region, neighbors, color, assignment):
                 assignment[region]= color
                 if solve_map_coloring(assignment, regions, colors, neighbors):
                     return True
                 del assignment[region]
        return False
 return False
 


def main():

    regions = [
        "Western Australia",
        "Northern Territory",
        "South Australia",
        "Queensland",
        "New South Wales",
        "Victoria",
        "Tasmania",
    ]

    colors = ["red", "green", "blue"]

#dictionary of neighbors
    neighbors = {
        "Western Australia": ["Northern Territory", "South Australia"],
        "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
        "South Australia": [
            "Western Australia",
            "Northern Territory",
            "Queensland",
            "New South Wales",
            "Victoria",
        ],
        "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
        "New South Wales": ["Queensland", "South Australia", "Victoria"],
        "Victoria": ["South Australia", "New South Wales", "Tasmania"],
        "Tasmania": ["Victoria"],
    }

    assignment = {}
    if solve_map_coloring(assignment, regions, colors, neighbors):
        print(assignment)
    else:
        print("No solution exists.")


main()

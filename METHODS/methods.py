import json

from CLASSES.point import *
from CLASSES.line import *
from CLASSES.conic import *
from CLASSES.construction import *

def extract_information(file_location):
    '''Extracts incidence information from cjs file'''
    
    #Basic formatting
    file = open(file_location)
    teststring = file.read()
    x = teststring.replace("deselect();", "")
    x = x.replace("reset();", "")
    x = x.replace("update();", "")
    x = x.replace("recalcall();", "")
    x = x.replace(" ", "")
    x = x.replace("\n", "")
    x = x.replace("gslp=", "")
    x = x[0:-1]

    #Now only a json file is left
    geom_array = json.loads(x)

    #initialize lists of geometric objects
    points = []
    lines = []
    conics = []
    incidences = {}
    name_dict = {}

    #iterate through all geometric objects given in the cjs file and add them to the correct list
    for geom_object in geom_array:
        #points have type P
        if geom_object['type'] =='P':
            name = geom_object['name']
            homog = geom_object['pos']
            #create point object
            new_point = Point(name, homog)
            #add translation between object and its name in the cjs file
            name_dict[name] = new_point
            points.append(new_point)
        #lines have type L
        if geom_object['type'] =='L':
            name = geom_object['name']
            homog = geom_object['pos']
            #create line object
            new_line = Line(name, homog)
            #add translation between object and its name in the cjs file
            name_dict[name] = new_line
            lines.append(new_line)
        #conics have type C
        if geom_object['type'] =='C':
            name = geom_object['name']
            params = geom_object['pos']
            #create conic object
            new_conic = Conic(name, params)
            #add translation between object and its name in the cjs file
            name_dict[name] = new_conic
            conics.append(new_conic)

    #now that we have all geometric objects, we need to find all incidences between them.
    #some are given by the 'incidences' entry, but e.g. joins, meets and points on lines have their incidences given as 'args'
    for geom_object in geom_array:
        try:
            match geom_object['alg']:
                case 'Free':
                    incids = geom_object["incidences"]
                    incid_array = []
                    for incid in incids:
                        incid_array.append(name_dict[incid])
                    incidences[name_dict[geom_object['name']]] = incid_array
                case 'Join':
                    pass
                case 'Meet':
                    pass
                case 'PointOnLine':
                    incids = set(geom_object["incidences"]).union(set())
                    incid_array = []
                    for incid in incids:
                        incid_array.append(name_dict[incid])
                    incidences[name_dict[geom_object['name']]] = incid_array
                case _:
                    pass
        except:
            pass
        
    return Construction(points, lines, conics, incidences)
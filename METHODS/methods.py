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

                ### POINTS ###

                #Free points
                case 'Free':
                    #only incidences are those given by incidences
                    incids = geom_object["incidences"]
                    incid_array = []
                    for incid in incids:
                        incid_array.append(name_dict[incid])
                    incidences[name_dict[geom_object['name']]] = incid_array
                
                #meets of two lines
                case 'Meet':
                    #incident to the two meeting lines and their incidences
                    incids = list(set(geom_object["incidences"]).union(set(geom_object["args"])))
                    incid_array = []
                    for incid in incids:
                        incid_array.append(name_dict[incid])
                    incidences[name_dict[geom_object['name']]] = incid_array

                    #also add this point as incidence of the lines it lies on
                    ref_line1 = name_dict[geom_object['args'][0]]
                    incidences[ref_line1] = list(set(incidences[ref_line1]).union({name_dict[geom_object['name']]}))
                    ref_line2 = name_dict[geom_object['args'][1]]
                    incidences[ref_line2] = list(set(incidences[ref_line2]).union({name_dict[geom_object['name']]}))

                #Points defined on a line
                case 'PointOnLine':
                    #incident to the line they are defined on and their other incidences
                    incids = list(set(geom_object["incidences"]).union(set(geom_object["args"])))
                    incid_array = []
                    for incid in incids:
                        incid_array.append(name_dict[incid])
                    incidences[name_dict[geom_object['name']]] = incid_array

                    #also add this point as incidence of the line it lies on
                    ref_line = name_dict[geom_object['args'][0]]
                    incidences[ref_line] = list(set(incidences[ref_line]).union({name_dict[geom_object['name']]}))

                ### LINES ###

                #joins of two points
                case 'Join':
                    #these lines are incident to the points spanning them and their other incidences
                    #also they are incident to the points on lines defined on it, and the meets of it with other lines (these will be added when the respective points are treated)
                    try:
                        #try to get incids, they might not exist
                        incids1 = set(geom_object["incidences"])
                    except:
                        incids1 = set()
                    #transform to set to get union and then transform back to list
                    incids = list(incids1.union(set(geom_object["args"])))
                    incid_array = []
                    for incid in incids:
                        incid_array.append(name_dict[incid])
                    incidences[name_dict[geom_object['name']]] = incid_array
                case _:
                    pass
        except:
            pass
        
    return Construction(points, lines, conics, incidences)
class Construction:
    def __init__(self, points, lines, conics, incidences):
        self.points = points
        self.lines = lines
        self.conics = conics
        self.incidences = incidences

    def print_points(self):
        """Print a string containing all the points"""
        point_string = ""
        for point in self.points:
            point_string = point_string + point.name + ", "
        if point_string == "":
            print("There are no conics in this construction.")
        else:
            print("The points in this construction are: " + point_string[0:-2] + ".")

    def print_lines(self):
        """Print a string containing all the lines"""
        line_string = ""
        for line in self.lines:
            line_string = line_string + line.name + ", "
        if line_string == "":
            print("There are no lines in this construction.")
        else:
            print("The lines in this construction are: " + line_string[0:-2] + ".")

    def print_conics(self):
        """Print a string containing all the conics"""
        conic_string = ""
        for conic in self.conics:
            conic_string = conic_string + conic.name + ", "
        if conic_string == "":
            print("There are no conics in this construction.")
        else:
            print("The conics in this construction are: " + conic_string[0:-2] + ".")

    def print_objects(self):
        """Prints all objects"""
        self.print_points()
        self.print_lines()
        self.print_conics()

    def print_incidences(self):
        """Prints all incidences starting with points, then lines, then conics TODO"""
        print("Listing incidences...")

        if len(self.points) > 0:
            print("-> Points:")
            for point in self.points:
                pointname = point.name
                incidences = ""
                for incidence in self.incidences[point]:
                    incidences = incidences + incidence.name + ", "
                print("--> Point " + pointname + " is incident to " + incidences[0:-2])
        else:
            print("-> There are no points in this construction")
        
        if len(self.lines) > 0:
            print("-> Lines:")
            for line in self.lines:
                linename = line.name
                incidences = ""
                for incidence in self.incidences[line]:
                    incidences = incidences + incidence.name + ", "
                print("--> Line " + linename + " is incident to " + incidences[0:-2])
        else:
            print("-> There are no lines in this construction")

    def calculate_point_non_degeneracies(self):
        """Uses the given positions to calculate point-triples that are NOT collinear and can thus be used in binomial proofs as non-degeneracy conditions"""
        pass

    def calculate_line_non_degeneracies(self):
        """Uses the given positions to calculate line-triples that are NOT collinear and can thus be used in binomial proofs as non-degeneracy conditions"""
        pass

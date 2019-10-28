class Beer(object):

    def __init__(self, value, title, degree, species, size):
        self.value = value
        self.title = title
        self.degree = degree
        self.species = species
        self.size = size

    def __str__(self):
        return "Цена = " + str(self.value) + "; Название - " + str(self.title) + "; Крепость алкоголя = " + str \
            (self.degree) + "; Вид: " + str(self.species) + "; Размер = " + str(self.size)

    def __repr__(self):
        return "Цена = " + str(self.value) + "; Название - " + str(self.title) + "; Крепость алкоголя = " + str \
            (self.degree) + "; Вид: " + str(self.species) + "; Размер = " + str(self.size)

    def get_value(self):
        return self.value

    def get_title(self):
        return self.title

    def get_degree(self):
        return self.degree

    def get_species(self):
        return self.species

    def get_size(self):
        return self.size

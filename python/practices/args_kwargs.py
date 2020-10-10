class Property:
    def __init__(self, square_feet = '', beds = '', bath='', **kwargs):
        self.square_feet = square_feet
        self.beds = beds
        self.bath = bath
        super().__init__(**kwargs)

property = Property(demo = "luan")

print(property.demo)
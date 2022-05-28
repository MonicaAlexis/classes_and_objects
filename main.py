class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        change_name = input("Enter new name: ")
        print("Name updated from", self.name, "to", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        change_age = input("Enter new age: ")
        print("Age updated from", self.age, "to", change_age)

    def add_tracks(self, add_tracks):
        self.add_tracks = add_tracks
        add_tracks = input("Add a new track: ")
        print("Successful! ", add_tracks, "Track added")

    def get_score(self, get_score):
        self.get_score = get_score
        print("You score",get_score)

    
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score(50.0)

class Student:
    def __init__(self, name, __score):
        self.name = name
        self.__score = __score

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
        else:
            print("Baho noto'g'ri")


s1 = Student("Ali", 85)

print(s1.name)
print(s1.get_score())

s1.set_score(90)
print(s1.get_score())

s1.set_score(150)

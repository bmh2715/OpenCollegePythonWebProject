#__init__함수는 constructor입니다.
class Human:
    def __init__(self, name, age, gender, height, blood):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.blood=blood

    def introduceMyself(self):
        print("제 이름은", self.name, "이고 나이는", self.age, "입니다.")

dohanKim=Human("김도한",20, "Male", 179, "AB")
yusunJung=Human("정유선", 31, "Female", 168, "0")

dohanKim.introduceMyself()
yusunJung.introduceMyself()
class Car:
    def __init__(self, company, model, color):
        self.company=company
        self.model=model
        self.color=color
        self.fuel=1000

    def forward(self):
        self.fuel=self.fuel-50
        print(self.company, self.model, self.color, "차량이 전진 중입니다. 현재 기름양은", self.fuel,"입니다.")

    def reverse(self):
        self.fuel = self.fuel - 30
        print(self.company, self.model, self.color, "차량이 후진 중입니다. 현재 기름양은", self.fuel, "입니다.")
car1=Car("BMW", "420i", "White")
car2=Car("Hyundai", "avante", "black")
car3=Car("Kia", "stringer", "Red")


car1.forward()
car1.reverse()
car2.forward()
car2.reverse()
car3.forward()
car3.reverse()
class Car:
    def __init__(self, model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        return(f"You can drive {self.model} {self.year} {self.color}.")


    def stop(self):
        return(f"You can stop {self.model} {self.year} {self.color}.")


    def describe(self):
        return(f"{self.model}\n {self.year}\n {self.color}")


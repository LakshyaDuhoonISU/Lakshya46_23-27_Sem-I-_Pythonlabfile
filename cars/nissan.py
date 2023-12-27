class Nissan:
    def __init__(self, model):
        self.model = model
    def start_engine(self):
        print(f"Nissan {self.model} engine started.")
    def drive(self):
        print(f"Driving the Nissan {self.model}.")
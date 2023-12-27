class BMW:
    def __init__(self, model):
        self.model = model
    def start_engine(self):
        print(f"BMW {self.model} engine started.")
    def drive(self):
        print(f"Driving the BMW {self.model}.")
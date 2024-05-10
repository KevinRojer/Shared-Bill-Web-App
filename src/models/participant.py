class Participant:
    def __init__(self, bill_id, name, units) -> None:
        self.participant_id = None
        self.bill_id = bill_id
        self.name = name
        self.units = units

    def calculate_amount_owed(self, cost_per_unit):
        pass
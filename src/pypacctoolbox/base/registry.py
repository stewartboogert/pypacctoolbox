class registry :

    def __init__(self):
        self.expressions = {}

    def add_expression(self, topic, label, symbol, expression, comment):

        if topic not in self.expressions:
            self.expressions[topic] = {}

        self.expressions[topic][label] = (symbol, expression, comment)


registry = registry()
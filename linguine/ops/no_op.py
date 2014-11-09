#A null operation
#Useful for unit testing or acting as a placeholder

class NoOp:

    def run(self, data):
        if len(data) > 0:
            return data[0].to_dict()
        else:
            return ""

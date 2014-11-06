#A null operation
#Useful for unit testing or acting as a placeholder

class no_op:

    def run(self, data):
        if len(data) > 0:
            return data[0]
        else:
            return ""

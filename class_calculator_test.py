# Program to size a 3 port valve using a class

import math

class Valve_3P:

    def __init__(self, name, flow_rate, load_PD):
        self.name = name
        self.flow_rate = flow_rate
        self.load_PD = load_PD
    
def validation_check(user_input): # function to return True or False depending on if a number
    try:
        float(user_input)
        return True
    except:
        print(f"The input '{user_input}' is not a valid number.Try again!")
        return False

def main():
    valves = []
    #class_name = "cv1"
    cv1 = Valve_3P("CV1", 1.5, 10.2)
    valves.append(cv1)

    #class_name = "cv2"
    cv2 = Valve_3P("CV2", 10.7, 55.89)
    valves.append(cv2)

    for obj in valves:
        print(obj.name, obj.flow_rate, obj.load_PD, sep = ", ")

    cv1.manufacturer = "Belimo"
    cv1.model = "R322"
    cv2.manufacturer = "Siemens"
    cv2.model = "TR768"
    valves.append(cv1)
    valves.append(cv2)

    for obj in valves:
        print(obj.name, obj.flow_rate, obj.load_PD, obj.manufacturer, obj.model, sep = ", ")

if __name__ == '__main__':
    main()
# Program to size a 3 port valve using a class

from class_valve_3P import Valve_3P
import math

def validation_check(user_input): # function to return True or False depending on if a number
    try:
        float(user_input)
        return True
    except:
        print(f"The input '{user_input}' is not a valid number.Try again!")
        return False
    
def actual_kvs(flow_rate, load_PD): # function to calculate the actual kvs of the valve
    act_kvs = (float(flow_rate) * 3.6) / (math.sqrt(float(load_PD) * 0.01))
    return round(act_kvs, 2)

def valve_PD(flow_rate, valve_selected_kv): # function to calculate the valve pressure drop
    valve_pressure_drop = (((float(flow_rate) * 3.6)**2) / (float(valve_selected_kv)**2)) * 100
    return valve_pressure_drop

def authority_function(valve_PD, load_PD): # function to calculate the authority of the valve
    authority = (float(valve_PD) / (float(load_PD) + float(valve_PD))) * 100
    return authority

def menu():
    print("\n******************************")
    print("3 Port Valve Sizing App")
    print("")
    print("1. Add a Valve")
    print("2. Show Valve(s)")
    print("3. Edit a Valve")
    print("4. Delete a Valve")
    print("5. Exit App")
    print("\n******************************\n")

    # Enter the selection complete with validation
    valid_check = False
    while valid_check == False:
        selection = input("Enter the selection (1-5): ")
        valid_check = validation_check(selection)
        if valid_check == True and int(selection) >= 1 and int(selection) <= 5:
            return selection
        else:
            print(f"The input '{selection}' is not between 1-5.Try again!")
            valid_check = False
    
def add_valve():
    valve_ref = input("\nEnter the valve reference: ")

    # Enter the flow rate complete with validation
    valid_check = False
    while valid_check == False:
        flow_rate = input("Enter the flow rate (l/s): ")
        valid_check = validation_check(flow_rate)

    # Enter the pressure drop for the valve with validation
    valid_check = False
    while valid_check == False:
        load_PD = input("Enter the pressure drop (kPa): ")
        valid_check = validation_check(load_PD)

    act_kvs = actual_kvs(flow_rate, load_PD)

    print("")
    print(f"The valve reference is: {valve_ref}")
    print(f"The flow rate is {flow_rate}l/s")
    print(f"The load pressure drop is {load_PD}kPa")
    print(f"The actual kvs is {act_kvs:.2f}")

    # Enter the manufacturers data with validation
    valid_check = False
    while valid_check == False:
        man_kv = input("Enter the manufacturers kv value to match the actual kvs value: ")
        valid_check = validation_check(man_kv)

    manufacturer = input("Enter the manufacturer: ")
    model = input("Enter the model reference: ")
    valve_pressure_drop = valve_PD(flow_rate, man_kv)
    authority = authority_function(valve_pressure_drop, load_PD)

    print("")
    print(f"The valve pressure drop is {valve_pressure_drop:.2f}kPa")
    print(f"The valve authority is {authority:.2f}%")
    print(f"The manufacturer is {manufacturer} and the model is {model}.")

    valve_ref = Valve_3P(valve_ref, flow_rate, load_PD, man_kv, act_kvs, manufacturer, model, valve_pressure_drop, authority)
    return valve_ref
    
def show_valves(valves_list):
    for obj in valves_list:
        print(f"\nValve Ref.: {obj.name}, Flow Rate: {obj.flow_rate}l/s, Load PD: {obj.load_PD}kPa, Manuafcturer's kv: {obj.man_kv}, Actual kvs: {obj.act_kvs}, Authority: {obj.authority:.2f}%, Manufacturer: {obj.manufacturer}, Model: {obj.model}")

def edit_valve():
    pass

def delete_valve():
    pass

def main():
    main_check = True
    valves_list = []
    while main_check == True:
        selection = menu()
        selection = int(selection)

        match selection:
            case 1:
                valve = add_valve()
                valves_list.append(valve)
            case 2:
                show_valves(valves_list)
            case 3:
                pass
            case 4:
                pass
            case 5:
                main_check = False
            case _:
                pass

if __name__ == "__main__":
    main()

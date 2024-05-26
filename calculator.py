# Program to size a 3 port valve

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
    return act_kvs

def valve_PD(flow_rate, valve_selected_kv): # function to calculate the valve pressure drop
    valve_pressure_drop = (((float(flow_rate) * 3.6)**2) / (float(valve_selected_kv)**2)) * 100
    return valve_pressure_drop

def authority_function(valve_PD, load_PD): # function to calculate the authority of the valve
    authority = (float(valve_PD) / (float(load_PD) + float(valve_PD))) * 100
    return authority

valve_ref = input("Enter the valve reference: ")

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

# save results to a .txt file, add in menu for edit, print out, delete.
# save results to a database, same functions as above.
# GUI with user add for multiple lines, same options as above.

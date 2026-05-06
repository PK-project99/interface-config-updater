import csv
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': 'puneet.work',
    'password': 'Em4v-TzM0n7v_n',
    'port': 22,
}


def read_csv(filename):
    # read the CSV and return a list of dictionaries

    intList=[]
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for i in reader:
            intList.append(i)
    return intList



def build_commands(interface_details):

    commands=[f"interface {interface_details["interface"]}", f"description {interface_details["vlan_id"]}_{interface_details["description"]}"]

    return commands
        
            
def push_configs(connection, interfaceList):

    for interface in interfaceList:
        command = build_commands(interface)
        op=connection.send_config_set(command)
        connection.commit()

    return


try:
    interfaces_list=read_csv("interfaces.csv")
    connection = ConnectHandler(**device)
    print("Connected!")

    push_configs(connection,interfaces_list)
    connection.exit_config_mode()

    output = connection.send_command('show interfaces description')
    print(output)


    connection.disconnect()
    print("\nDisconnected")

except Exception as e:
    print(f"{e}")
import obd
import pandas as pd
from datetime import datetime
import os

def connect_to_obd():
    try:
        connection = obd.OBD()
        if connection.is_connected():
            print("Connected to OBD interface.")
            return connection
        else:
            print("Failed to connect to OBD interface.")
            return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def get_all_commands():
    return [cmd for cmd in obd.commands if cmd.mode != 9]

basic_commands = [
    obd.commands.RPM,
    obd.commands.SPEED,
    obd.commands.THROTTLE_POS,
    obd.commands.ENGINE_LOAD,
    obd.commands.INTAKE_TEMP,
    obd.commands.MAF,
    obd.commands.COOLANT_TEMP,
    obd.commands.FUEL_LEVEL,
    obd.commands.FUEL_PRESSURE
]
fuel_oxygen_commands = [
    obd.commands.LONG_FUEL_TRIM_1,
    obd.commands.SHORT_FUEL_TRIM_1,
    obd.commands.O2_SENSORS,
    obd.commands.O2_B1S1,
    obd.commands.O2_B1S2
]
advanced_optional_commands =[
    obd.commands.TIMING_ADVANCE,
    obd.commands.EVAP_PRESSURE,
    obd.commands.CATALYST_TEMP_B1_S1
]

def read_all_obd_data(connection):
    data = {}
    all_commands = basic_commands + fuel_oxygen_commands + advanced_optional_commands
    for cmd in all_commands:
        try:
            response = connection.query(cmd)
            if not response.is_null():
                data[cmd.name] = str(response.value)
            else:
                data[cmd.name] = "N/A"
        except Exception as e:
            data[cmd.name] = f"ERROR"
    return data

def get_dtc(connection):
    try:
        dtcs = connection.query(obd.commands.GET_DTC)
        return dtcs.value if dtcs and not dtcs.is_null() else "No codes"
    except Exception as e:
        return f"ERROR: {e}"

def clear_dtc(connection):
    try:
        response = connection.query(obd.commands.CLEAR_DTC)
        return "DTCs cleared." if response else "Clear failed."
    except Exception as e:
        return f"ERROR: {e}"

def save_to_csv(car_name, data, filename="obd.csv"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = {"Car": car_name, "Timestamp": timestamp}
    row.update(data)

    file_exists = os.path.isfile(filename)
    df = pd.DataFrame([row])

    if file_exists:
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)

    print(f"Data saved to '{filename}'.")

def main():
    car_name = input("Enter car name: ").strip()

    connection = connect_to_obd()
    if not connection:
        return

    print("Reading OBD-II data...")
    data = read_all_obd_data(connection)
    save_to_csv(car_name, data)

    print("Reading diagnostic trouble codes...")
    dtcs = get_dtc(connection)
    print(f"DTCs: {dtcs}")

    clear = input("Do you want to clear DTCs? (y/n): ").strip().lower()
    if clear == "y":
        result = clear_dtc(connection)
        print(result)

    print("Process completed.")

if __name__ == "__main__":
    main()
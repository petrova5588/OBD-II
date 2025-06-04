OBD-II Data Logger (Python)

This project reads real-time vehicle data via an ELM327 OBD-II adapter using Python. It also reads and clears diagnostic trouble codes (DTCs), and saves the data to a CSV file.

 Required Libraries
	•	obd
	•	pandas
 Features
	•	Connects to OBD-II port
	•	Reads live engine & sensor data
	•	Reads and clears DTCs (diagnostic trouble codes)
	•	Saves all data to a CSV file with timestamps

⸻

 Data Collected

Basic Engine Data:
	•	RPM
	•	SPEED
	•	THROTTLE_POS
	•	ENGINE_LOAD
	•	INTAKE_TEMP
	•	MAF
	•	COOLANT_TEMP
	•	FUEL_LEVEL
	•	FUEL_PRESSURE

Fuel & Oxygen System Data:
	•	LONG_FUEL_TRIM_1
	•	SHORT_FUEL_TRIM_1
	•	TIMING_ADVANCE
	•	INTAKE_PRESSURE

Advanced / Optional Sensors (not supported on all vehicles):
	•	CATALYST_TEMP_B1S1
	•	O2_B1S1
	•	O2_B1S2

Unsupported commands will return “N/A” or “ERROR” instead of stopping the script.

⸻

▶ How to Use
	1.	Plug the ELM327 device into the vehicle’s OBD-II port.
	2.	Connect the device to your computer (Bluetooth or USB).
  3.	Run the Python script:
  python obd_final.py
  4.	When asked, enter the name of the car (e.g. Ford_Focus).
	5.	The script will:
	•	Connect to the car
	•	Read sensor data
	•	Save to obd.csv
	•	Show DTCs
	•	Ask if you want to clear them

⸻

 Output: obd.csv

Each row contains:
	•	Car name
	•	Timestamp
	•	All the sensor values

If the file exists, new data will be appended to it automatically.

⸻

 File List
	•	obd_final.py → Main script
	•	obd.csv → Automatically created log file
	•	README.md → Project info (this file)

⸻

 Author

Dilan Çakır
Artificial Intelligence Engineering Student
Python Developer – Automotive Diagnostics

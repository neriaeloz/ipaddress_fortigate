# FortiGate CLI Generator

This Python script allows you to interactively input IP addresses and automatically generate FortiGate CLI commands to:

- Create firewall address objects
- Append those objects to a specified address group

The generated commands are saved to a plain text file (`fortigate_commands.txt`) for easy copy-paste into the FortiGate CLI.

---

## 📦 Features

- Simple and interactive input
- Auto-formats object names from IPs (e.g. `192.168.1.10` → `192.168.1.10`)
- Handles `/` in CIDR format by converting it to `-` in object names
- Saves a ready-to-use CLI script

---

## 🛠 Requirements

- Python 3.x installed

---

## 🚀 Usage

1. Clone this repository or copy the script to your local machine.
2. Run the script using:

   ```bash
   python generate_fortigate.py

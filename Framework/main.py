import typer
from VendorLookup import mac_addr_vendor_lookup
from MonitorMode import switch_monitor_mode
from RestartNetwork import restart_network_services
from WPA_Handshake import wpa_capture_password_cracking
from ConnectCrackedNetwork import connect_to_cracked_network
from CommandList import list_defined_modules
from HostDiscovery import device_discovery
from ARP_Spoofing import man_in_middle_attack
from TelloControl import take_flight_control

# Create a Typer object for command-line interface (CLI) application
app = typer.Typer()

# Command-line commands decorated with @typer.command()


# Command to switch to monitor mode
@app.command()
def modemon():
    """
    Switch to monitor mode.
    """
    switch_monitor_mode()


# Command to restart network services
@app.command()
def restartnetwork():
    """
    Restart network services.
    """
    restart_network_services()


# Command to perform WPA2 handshake password cracking
@app.command()
def wpa2handshake():
    """
    Perform WPA2 handshake password cracking.
    """
    wpa_capture_password_cracking()


# Command to connect to a cracked network
@app.command()
def connectnetwork():
    """
    Connect to a cracked network.
    """
    connect_to_cracked_network()


# Command to list defined modules
@app.command()
def list():
    """
    List defined modules.
    """
    list_defined_modules()


# Command to perform network scanning
@app.command()
def network_scan():
    """
    Perform network scanning.
    """
    device_discovery()


# Command to perform MAC address vendor lookup
@app.command()
def vendorlookup():
    """
    Perform MAC address vendor lookup.
    """
    mac_addr_vendor_lookup()


# Command to perform ARP spoofing
@app.command()
def arp_spoofing():
    """
    Perform ARP spoofing.
    """
    man_in_middle_attack()


# Command to control drone motion
@app.command()
def drone_motion_control():
    """
    Control drone motion.
    """
    take_flight_control()


# Main function to execute the Typer object
def main():
    app()


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

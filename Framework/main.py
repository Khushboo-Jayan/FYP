import typer
from VendorLookup import mac_addr_vendor_lookup
from MonitorMode import switch_monitor_mode
from RestartNetwork import restart_network_services
from WPA_Handshake import wpa_capture_password_cracking
from ConnectCrackedNetwork import connect_to_cracked_network
from CommandList import list_defined_modules
from HostDiscovery import device_discovery
from ARP_Spoofing import man_in_middle_attack
from testCV import show_image


# create an object using typer
app = typer.Typer()


# add a decorator @typer.command() before a function declaration to designate that function as a command in CLI application.
@app.command()
def modemon():
    switch_monitor_mode()


# restart network services
@app.command()
def restartnetwork():
    restart_network_services()

@app.command()
def wpa2handshake():
    wpa_capture_password_cracking()


@app.command()
def vendorlookup():
    mac_addr_vendor_lookup()


@app.command()
def connectnetwork():
    connect_to_cracked_network()

# Define the callback function for listing commands
@app.command()
def list():
    list_defined_modules()


@app.command()
def network_scan():
    device_discovery()


@app.command()
def arp_spoofing():
    man_in_middle_attack()


@app.command()
def print_image():
    show_image()

# at the start of the python application we are calling the object
def main():
    app()


if __name__ == "__main__":
    main()

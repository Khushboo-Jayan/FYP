import typer
from vendorlookup import mac_addr_vendor_lookup
from monitormode import switch_monitor_mode
from restartNetwork import restart_network_services
from wpahandshake import wpa_capture_password_cracking
from connectCrackedNetwork import connect_to_cracked_network
from commands import list_defined_modules
import os

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


# at the start of the python application we are calling the object
def main():
    app()


if __name__ == "__main__":
    main()

from rich.console import Console
from rich.table import Table

def list_defined_modules():
    """
    Display list of available commands
    """
    table = Table(title="SentinelGuard Framework module list")

    table.add_column("Command", justify="right", style="cyan", no_wrap=True)
    table.add_column("Function", style="magenta")

    table.add_row("modemon", "Switch the network adptor to a monitor mode")
    table.add_row("vendorlookup", "Pass the mac address and identify the vendor lookup")
    table.add_row("wpa2handshake", "Capture file creation for password cracking")
    table.add_row("restartnetwork", "Restarts the network manager from command line")

    console = Console()
    console.print(table)
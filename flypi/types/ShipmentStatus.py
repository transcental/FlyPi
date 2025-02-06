from dataclasses import dataclass


@dataclass
class ShipmentStatus:
    """Class for storing all the necessary information about a package"""

    tracking_number: str
    url: str
    courier: str
    status: str

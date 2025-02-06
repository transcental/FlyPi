import aiohttp

from flypi.types import CourierFetcher
from flypi.types import ShipmentStatus
from flypi.utils import env


class Asendia(CourierFetcher):
    @staticmethod
    async def fetch(tracking_number: str) -> ShipmentStatus:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://a1reportapi.asendiaprod.com/api/A1/TrackingBranded/Tracking?trackingKey=AE654169-0B14-45F9-8498-A8E464E13D26&trackingNumber={tracking_number}",
                headers={
                    "accept": "application/json",
                    "authorization": f"Basic {env.asendia_api_key}",
                    "content-type": "application/json",
                    "x-asendiaone-apikey": "32337AB0-45DD-44A2-8601-547439EF9B55",
                },
                data=None,
            ) as response:
                data = await response.json()
                return data

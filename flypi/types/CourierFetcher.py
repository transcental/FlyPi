from flypi.types import ShipmentStatus


class CourierFetcher:
    @staticmethod
    async def fetch(tracking_number: str) -> ShipmentStatus:
        raise NotImplementedError()

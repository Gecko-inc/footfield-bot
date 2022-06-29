import aiohttp


URL = "http://127.0.0.1:8000/api/"


async def get_config() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}get_config/") as response:
            return await response.json()


async def get_all_fields_api() -> list:
    """Получение всех полей"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}all_fields/") as response:
            return await response.json()


async def get_images() -> list:
    """Получение всех фотографий"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}images/") as response:
            return await response.json()


async def filter_area(area: str) -> list:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}filter_area/{area}") as response:
            return await response.json()


async def filter_size(size: str) -> list:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}filter_size/{size}") as response:
            return await response.json()

import json
import asyncio
from aiohttp import ClientSession, ClientConnectorError

class AsyncRequests:
    @staticmethod
    async def fetch_json(url, session, **kwargs):
        try:
            resp = await session.request("GET", url, **kwargs)
        except ClientConnectorError:
            return (None,)
        return (resp, resp.status)

    @staticmethod
    async def make_requests(urls, **kwargs):
        async with ClientSession() as session:
            tasks = []
            meta = []
            for count, url in enumerate(urls):
                resp = await AsyncRequests.fetch_json(url, session, **kwargs)
                if resp[0] is None or resp[1]!=200:
                    return False
                else:
                    tasks.append(resp[0].json(loads=json.loads))
                meta.append((resp[1], count))
            results = await asyncio.gather(*tasks)

            collated_results = []
            for result, metas in zip(results, meta):
                collated_results.append((result, *metas))

            return collated_results
    
    @staticmethod
    def run(urls, **kwargs):
        results = asyncio.run(AsyncRequests.make_requests(urls, **kwargs))
        return results
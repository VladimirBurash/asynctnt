import asyncio

from asynctnt import Iterator
from asynctnt import Response
from asynctnt.exceptions import TarantoolSchemaError
from tests import BaseTarantoolTestCase
from tests.util import get_complex_param


class UpsertTestCase(BaseTarantoolTestCase):
    async def _fill_data(self):
        data = [
            [0, 'a', 1],
            [1, 'b', 0],
        ]
        for t in data:
            await self.conn.insert(self.TESTER_SPACE_ID, t)

        return data

    async def test__upsert_empty_one_assign(self):
        data = [0, 'hello', 1]

        res = await self.conn.upsert(self.TESTER_SPACE_ID,
                                     data, [['=', 2, 2]])
        self.assertIsInstance(res, Response, 'Got response')
        self.assertEqual(res.code, 0, 'success')
        self.assertGreater(res.sync, 0, 'sync > 0')
        self.assertListEqual(res.body, [], 'Body ok')

        res = await self.conn.select(self.TESTER_SPACE_ID, [0])
        self.assertListEqual(res.body, [data], 'Body ok')

    async def test__upsert_update_one_assign(self):
        data = [0, 'hello', 1]

        await self.conn.insert(self.TESTER_SPACE_ID, data)
        res = await self.conn.upsert(self.TESTER_SPACE_ID,
                                     data, [['=', 2, 2]])
        self.assertIsInstance(res, Response, 'Got response')
        self.assertEqual(res.code, 0, 'success')
        self.assertGreater(res.sync, 0, 'sync > 0')
        self.assertListEqual(res.body, [], 'Body ok')

        res = await self.conn.select(self.TESTER_SPACE_ID, [0])
        data[2] = 2
        self.assertListEqual(res.body, [data], 'Body ok')

    async def test__upsert_by_name(self):
        data = [0, 'hello', 1]

        await self.conn.upsert(self.TESTER_SPACE_NAME,
                               data, [['=', 2, 2]])

        res = await self.conn.select(self.TESTER_SPACE_ID, [0])
        self.assertIsInstance(res, Response, 'Got response')
        self.assertEqual(res.code, 0, 'success')
        self.assertGreater(res.sync, 0, 'sync > 0')
        self.assertListEqual(res.body, [data], 'Body ok')

    async def test__upsert_by_name_no_schema(self):
        await self.tnt_reconnect(fetch_schema=False)

        with self.assertRaises(TarantoolSchemaError):
            await self.conn.upsert(self.TESTER_SPACE_NAME,
                                   [0, 'hello', 1], [['=', 2, 2]])

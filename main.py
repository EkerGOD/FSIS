import asyncio

import rind
from rind.engine import main

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # asyncio.run(main())
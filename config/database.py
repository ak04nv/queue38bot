from motor.motor_asyncio import AsyncIOMotorClient


def get_database(conf):
    client = AsyncIOMotorClient(conf.DB_HOST,
                                conf.DB_PORT,
                                maxPoolSize=conf.DB_MAX_POOL_SIZE)
    return client.get_database(conf.DB_NAME)

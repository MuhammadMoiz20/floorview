from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
app = FastAPI(title='FloorView API', lifespan=lifespan)

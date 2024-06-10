from fastapi import FastAPI
app = FastAPI(title='FloorView API')
@app.get('/products/{product_id}/stage')
async def get_product_stage(product_id: int):
    stage = await get_current_stage(product_id)
    return stage
@app.post('/products/{product_id}/transition')
async def transition(product_id: int, transition: StageTransition):
    await transition_stage(product_id, transition.from_stage, transition.to_stage, transition.notes)
    return {'message': 'Transitioned'}
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=['*'])
@app.get('/audit/{product_id}')
async def get_audit_log(product_id: int):
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    logs = await conn.fetch('SELECT * FROM audit_log WHERE product_id = ', product_id)
    await conn.close()
    return logs

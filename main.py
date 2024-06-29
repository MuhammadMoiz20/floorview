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
@app.get('/stages')
async def list_stages():
    stages = await get_all_stages()
    return stages
@app.get('/stages/{stage_id}/products')
async def products_in_stage(stage_id: int):
    products = await get_products_by_stage(stage_id)
    return products
@app.get('/dashboard/stats')
async def dashboard():
    stats = await get_dashboard_stats()
    return stats
@app.post('/products/bulk-update')
async def bulk_update(product_ids: list, status: str):
    await bulk_update_status(product_ids, status)
    return {'message': f'Updated {len(product_ids)} products'}

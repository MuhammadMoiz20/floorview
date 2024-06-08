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

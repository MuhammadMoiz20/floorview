async def get_current_stage(product_id):
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    stage = await conn.fetchrow('''
        SELECT ps.*, s.name as stage_name 
        FROM product_stages ps 
        JOIN stages s ON ps.stage_id = s.id 
        WHERE ps.product_id =  
        ORDER BY ps.updated_at DESC LIMIT 1
    ''', product_id)
    await conn.close()
    return stage
async def transition_stage(product_id, from_stage, to_stage, notes=None, user='system'):
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    await conn.execute('''
        UPDATE product_stages SET status = 'completed', updated_at = NOW()
        WHERE product_id =  AND stage_id = 
    ''', product_id, from_stage)
    await conn.execute('''
        INSERT INTO product_stages (product_id, stage_id, status, notes)
        VALUES (, , 'in_progress', )
    ''', product_id, to_stage, notes)
    await conn.execute('''
        INSERT INTO audit_log (product_id, from_stage, to_stage, changed_by)
        VALUES (, , , )
    ''', product_id, from_stage, to_stage, user)
    await conn.close()
async def get_all_stages():
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    stages = await conn.fetch('SELECT * FROM stages ORDER BY id')
    await conn.close()
    return stages
async def get_products_by_stage(stage_id):
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    products = await conn.fetch('''
        SELECT p.*, ps.status, ps.updated_at 
        FROM products p 
        JOIN product_stages ps ON p.id = ps.product_id 
        WHERE ps.stage_id = 
    ''', stage_id)
    await conn.close()
    return products
async def get_dashboard_stats():
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    total_products = await conn.fetchval('SELECT COUNT(*) FROM products')
    completed = await conn.fetchval("SELECT COUNT(*) FROM product_stages WHERE status = 'completed'")
    in_progress = await conn.fetchval("SELECT COUNT(*) FROM product_stages WHERE status = 'in_progress'")
    await conn.close()
    return {'total': total_products, 'completed': completed, 'in_progress': in_progress}
async def bulk_update_status(product_ids, status):
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    for pid in product_ids:
        await conn.execute('''
            UPDATE product_stages SET status = , updated_at = NOW()
            WHERE product_id = 
        ''', status, pid)
    await conn.close()

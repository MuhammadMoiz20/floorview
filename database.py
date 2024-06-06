import asyncpg
from datetime import datetime
async def init_db():
    conn = await asyncpg.connect('postgresql://user:pass@localhost/floorview')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT,
            sku TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT NOW()
        )
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS stages (
            id SERIAL PRIMARY KEY,
            name TEXT,
            description TEXT
        )
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS product_stages (
            id SERIAL PRIMARY KEY,
            product_id INTEGER REFERENCES products(id),
            stage_id INTEGER REFERENCES stages(id),
            status TEXT,
            updated_at TIMESTAMP DEFAULT NOW(),
            notes TEXT
        )
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS audit_log (
            id SERIAL PRIMARY KEY,
            product_id INTEGER,
            from_stage INTEGER,
            to_stage INTEGER,
            changed_at TIMESTAMP DEFAULT NOW(),
            changed_by TEXT
        )
    ''')
    await conn.close()

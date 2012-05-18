DB_NAME = 'database.db'
DB_PATH = '../database/' + DB_NAME

TABLE_OUTLAWS = """
    CREATE TABLE IF NOT EXISTS outlaws(
    
        outlaw_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        reward REAL NOT NULL,
    );
    """

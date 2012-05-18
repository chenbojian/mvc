DB_NAME = 'database.db'
DB_PATH = '../database/' + DB_NAME

TABLE_OUTLAWS = """
    CREATE TABLE IF NOT EXISTS prisons(
        prison_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """

TABLE_PRISONS = """
    CREATE TABLE IF NOT EXISTS outlaws(
    
        outlaw_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT UNIQUE NOT NULL,
        reward REAL NOT NULL,
        prison_id INTEGER,
    
        FOREIGN KEY(prison_id)
        REFERENCES prisons(prison_id)
    );
    """

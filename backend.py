import sqlite3

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('reels.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the table if it doesn't exist
def create_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reels
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  link TEXT,
                  tag TEXT,
                  tool_name TEXT)''')
    conn.commit()
    conn.close()

# Add a new reel to the database
def add_reel(link, tag, tool_name):
    create_table()  # Ensure the table exists before inserting
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO reels (link, tag, tool_name) VALUES (?, ?, ?)", (link, tag, tool_name))
    conn.commit()
    conn.close()

# Search for tools based on partial matching of the tag
def search_tool(tag):
    conn = get_db_connection()
    c = conn.cursor()
    # Use LIKE to allow partial matching (case-insensitive)
    c.execute("SELECT tool_name, tag FROM reels WHERE tag LIKE ?", ('%' + tag + '%',))
    results = c.fetchall()
    conn.close()

    if results:
        # Format the result to show all matching tags and their corresponding tools
        response = "\n".join([f"Tag: {result['tag']} -> Tool: {result['tool_name']}" for result in results])
        return response
    else:
        return "No tools found for this tag."

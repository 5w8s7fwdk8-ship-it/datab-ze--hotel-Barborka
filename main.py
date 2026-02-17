import sqlite3

class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class BarborkaDB:
    def __init__(self, db_name="barborka.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS guests 
                   (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"""
        self.conn.execute(query)
        self.conn.commit()

    def add_guest(self, guest):
        query = "INSERT INTO guests (name, email) VALUES (?, ?)"
        self.conn.execute(query, (guest.name, guest.email))
        self.conn.commit()
        print(f"Host {guest.name} byl úspěšně přidán do systému Barborka!")

    def show_all_guests(self):
        cursor = self.conn.execute("SELECT * FROM guests")
        for row in cursor:
            print(f"ID: {row[0]} | Jméno: {row[1]} | Email: {row[2]}")

    def find_guests_by_email_provider(self, provider):
        """Vyhledá hosty podle poskytovatele emailu (ukázka SQL LIKE)."""
        query = "SELECT * FROM guests WHERE email LIKE ?"
        cursor = self.conn.execute(query, (f'%{provider}%',))
        print(f"\nHosté s emailem u {provider}:")
        for row in cursor:
            print(f"- {row[1]} ({row[2]})")

if __name__ == "__main__":
    db = BarborkaDB()
    
    # Přidáme testovací data
    db.add_guest(Guest("Jan Novák", "jan.novak@gmail.com"))
    db.add_guest(Guest("Petr Kolář", "petr@seznam.cz"))
    
    # Ukázka použití nové metody
    db.find_guests_by_email_provider("gmail")

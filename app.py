from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite
def connect_db():
    return sqlite3.connect('chocolate_house.db')

@app.route('/')
def home():
    return render_template('index.html')

# Route: Initialize Database
@app.route('/init', methods=['GET'])
def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flavors (id INTEGER PRIMARY KEY, name TEXT, season TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, ingredient TEXT, quantity INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS suggestions (id INTEGER PRIMARY KEY, flavor_name TEXT, allergy TEXT)''')
    conn.commit()
    conn.close()
    return "Database initialized successfully!"

# Route: Add Seasonal Flavor
@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        flavor_name = request.form.get('flavor_name')
        season = request.form.get('season', 'All Year')  # Default season if not provided
        
        if flavor_name:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO flavors (name, season) VALUES (?, ?)",
                    (flavor_name, season)
                )
                conn.commit()
                conn.close()
                return f"Flavor '{flavor_name}' added successfully!"
            except Exception as e:
                return f"Error adding flavor: {str(e)}", 500
        else:
            return "Error: Flavor name is required!", 400
    else:
        return '''
            <form action="/add_flavor" method="post">
                Flavor Name: <input type="text" name="flavor_name"><br>
                Season: <input type="text" name="season"><br>
                <button type="submit">Add Flavor</button>
            </form>
        '''

# Route: Add Ingredient Inventory
@app.route('/add_inventory', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        ingredient = request.form.get('ingredient')
        quantity = request.form.get('quantity')
        
        if ingredient and quantity:
            try:
                quantity = int(quantity)
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO inventory (ingredient, quantity) VALUES (?, ?)",
                    (ingredient, quantity)
                )
                conn.commit()
                conn.close()
                return f"Ingredient '{ingredient}' with quantity {quantity} added successfully!"
            except ValueError:
                return "Error: Quantity must be an integer!", 400
            except Exception as e:
                return f"Error adding inventory: {str(e)}", 500
        else:
            return "Error: Both ingredient and quantity are required!", 400
    else:
        return '''
            <form action="/add_inventory" method="post">
                Ingredient: <input type="text" name="ingredient"><br>
                Quantity: <input type="number" name="quantity"><br>
                <button type="submit">Add Inventory</button>
            </form>
        '''

@app.route('/add_suggestion', methods=['GET', 'POST'])
def add_suggestion():
    if request.method == 'POST':
        flavor_name = request.form.get('flavor_name')
        allergy = request.form.get('allergy')
        
        if flavor_name and allergy:
            try:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO suggestions (flavor_name, allergy) VALUES (?, ?)",
                    (flavor_name, allergy)
                )
                conn.commit()
                conn.close()
                return f"Suggestion for flavor '{flavor_name}' with allergy concern '{allergy}' added successfully!"
            except Exception as e:
                return f"Error adding suggestion: {str(e)}", 500
        else:
            return "Error: Both flavor name and allergy concern are required!", 400
    else:
        return '''
            <form action="/add_suggestion" method="post">
                Flavor Name: <input type="text" name="flavor_name"><br>
                Allergy Concern: <input type="text" name="allergy"><br>
                <button type="submit">Add Suggestion</button>
            </form>
        '''

# Add a route to populate test data for all tables

@app.route('/get_flavors', methods=['GET'])
def get_flavors():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Get flavors
        cursor.execute("SELECT id, name, season FROM flavors")
        flavor_rows = cursor.fetchall()
        flavors = []
        for row in flavor_rows:
            flavors.append({
                'id': row[0],
                'name': row[1],
                'season': row[2]
            })
        
        # Get inventory
        cursor.execute("SELECT id, ingredient, quantity FROM inventory")
        inventory_rows = cursor.fetchall()
        inventory = []
        for row in inventory_rows:
            inventory.append({
                'id': row[0],
                'ingredient': row[1],
                'quantity': row[2]
            })
        
        # Get suggestions
        cursor.execute("SELECT id, flavor_name, allergy FROM suggestions")
        suggestion_rows = cursor.fetchall()
        suggestions = []
        for row in suggestion_rows:
            suggestions.append({
                'id': row[0],
                'flavor_name': row[1],
                'allergy': row[2]
            })
        
        # Combine all data into one response
        response_data = {
            'flavors': flavors,
            'inventory': inventory,
            'suggestions': suggestions
        }
            
        conn.close()
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

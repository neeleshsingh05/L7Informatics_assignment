# Chocolate House Management System

A Flask-based web application for managing a chocolate house's seasonal flavors, inventory, and customer suggestions with SQLite database integration.

## Features

- Manage seasonal chocolate flavor offerings
- Track ingredient inventory
- Handle customer flavor suggestions and allergy concerns
- Simple and intuitive web interface
- SQLite database for data persistence

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- pip (Python package manager)

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/neeleshsingh05/L7Informatics_assignment.git
cd chocolate-house-management
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
# Start the application and visit this endpoint in your browser
http://localhost:5000/init
```

### Docker Setup

1. Build the Docker image:
```bash
docker build -t chocolate-house .
```

2. Run the container:
```bash
docker run -p 5000:4000 chocolate-house
```

## Usage

1. Start the application:
   - Local: `python app.py`
   - Docker: Application starts automatically in container

2. Access the web interface:
   - Open your browser and navigate to `http://localhost:5000`

3. Available Features:
   - Add new seasonal flavors with the "Add New Flavor" button
   - Manage inventory by adding ingredients and quantities
   - Record customer suggestions and allergy concerns
   - View all entries in an organized dashboard

## API Endpoints

- `GET /` - Home page
- `GET /init` - Initialize database
- `POST /add_flavor` - Add new chocolate flavor
- `POST /add_inventory` - Add inventory item
- `POST /add_suggestion` - Add customer suggestion
- `GET /get_flavors` - Retrieve all data (flavors, inventory, suggestions)

## Database Schema

```sql
CREATE TABLE flavors (
    id INTEGER PRIMARY KEY,
    name TEXT,
    season TEXT
);

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    ingredient TEXT,
    quantity INTEGER
);

CREATE TABLE suggestions (
    id INTEGER PRIMARY KEY,
    flavor_name TEXT,
    allergy TEXT
);
```

## Testing

To validate the application functionality:

1. Database Initialization:
   - Access `/init` endpoint
   - Verify success message

2. Data Management:
   - Add test flavor entries
   - Add inventory items
   - Create customer suggestions
   - Verify data persistence by restarting application

3. Edge Cases:
   - Test empty form submissions
   - Verify duplicate handling
   - Check special character handling in inputs

## File Structure

```
chocolate-house/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Documentation

Code is documented with:
- Function docstrings
- Route descriptions
- Clear variable naming
- Inline comments for complex logic

## Development Guidelines

- Follow PEP 8 Python coding standards
- Document all new features
- Test edge cases before committing
- Keep frontend modifications minimal
- Focus on backend functionality

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License.

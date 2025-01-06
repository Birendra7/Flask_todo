from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set up the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'  # SQLite DB file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable Flask-SQLAlchemy modification tracking
db = SQLAlchemy(app)

# Create Todo model (Database schema)
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Todo({self.sno}, {self.title}, {self.description}, {self.date})"

# Route for home page
@app.route('/')
def index():
    todos = Todo.query.all()  # Fetch all todos from the database
    return render_template('index.html', todos=todos)

# Route for adding a new Todo
@app.route('/add', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        new_todo = Todo(title=title, description=description, date=date)
        
        try:
            db.session.add(new_todo)  # Add the new todo to the database
            db.session.commit()  # Commit the transaction
            return redirect('/')  # Redirect to home page after successful insertion
        except:
            return "There was an issue adding your todo."
    
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

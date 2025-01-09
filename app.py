from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set up the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'  # SQLite DB file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# Todo model (Database schema)
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
    return render_template('index.html', todos=todos, update_todo=None)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Route to add a new Todo
@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']
    new_todo = Todo(title=title, description=description, date=date)
    try:
        db.session.add(new_todo)  # Add to database
        db.session.commit()  # Commit transaction
        return redirect('/')
    except:
        return "There was an issue adding your todo."

# Route to delete a Todo
@app.route('/delete/<int:sno>')
def delete_todo(sno):
    todo = Todo.query.get_or_404(sno)  # Fetch todo by ID
    try:
        db.session.delete(todo)  # Delete from database
        db.session.commit()  # Commit transaction
        return redirect('/')
    except:
        return "There was an issue deleting your todo."

# Route to update a Todo
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update_todo(sno):
    todo = Todo.query.get_or_404(sno)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        todo.date = request.form['date']
        db.session.commit()
        return redirect('/')
    else:
        todos = Todo.query.all()  # Fetch all todos
        return render_template('index.html', todos=todos, update_todo=todo)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)



# **Todo App with Flask**

A simple, user-friendly web application built with **Flask** to manage your daily tasks efficiently. This app includes features to add, update, delete, and view todos, along with pages for an about section, a privacy policy, and a blog.

---

## **Features**
- **Add Todos**: Create tasks with a title and description.
- **Update Todos**: Modify existing tasks seamlessly.
- **Delete Todos**: Remove completed or unnecessary tasks.
- **Blog Section**: Stay updated with the latest productivity tips and app updates.
- **About Page**: Learn about the app and its purpose.
- **Privacy Policy**: Understand how your data is collected and managed.

---

## **Installation**

Follow these steps to set up and run the Todo App locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/Birendra7/Flask_todo.git
cd Flask_todo
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up the Database**
Start the Flask shell:
```bash
flask shell
```
Run the following commands to create the database:
```python
from app import db
db.create_all()
```

### **5. Run the Application**
```bash
flask run
```

Access the app in your browser at `http://127.0.0.1:5000`.

---

## **Project Structure**
```
todo-app/
├── app.py                # Main Flask application
├── templates/            # HTML files for pages
│   ├── index.html        # Main page for todos
│   ├── about.html        # About page
│   ├── privacy.html      # Privacy policy page
│   ├── blog.html         # Blog page
│   ├── update.html       # Page for updating todos
├── static/               # Static files (CSS, JS, images)
│   ├── style.css         # Custom styles (optional)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── todo.db               # SQLite database (generated after setup)
```

---

## **Screenshots**

### **Homepage**
![image](https://github.com/user-attachments/assets/281dd545-9968-4499-b446-325d5238832a)

### **Add Todo**
![image](https://github.com/user-attachments/assets/edbb6514-6b59-47ee-ba9b-2d9b152eb3ce)
![image](https://github.com/user-attachments/assets/fbedf71d-8655-456f-b571-1c31c07397ac)



### **Blog Section**
![image](https://github.com/user-attachments/assets/a1776897-37d7-407d-b59b-53b905acd8bf)

---

## **Routes**
| URL Path         | Description                          |
|------------------|--------------------------------------|
| `/`              | View all todos                      |
| `/add`           | Add a new todo                      |
| `/update/<id>`   | Update an existing todo             |
| `/delete/<id>`   | Delete a todo                       |
| `/about`         | About the app                       |
| `/privacy`       | Privacy policy                      |
| `/blog`          | Blog page with productivity tips    |

---

## **Built With**
- **Flask**: Python microframework for backend development.
- **Bootstrap**: Responsive front-end framework for design.
- **SQLite**: Lightweight database for storing todos.
- **HTML/CSS**: For structuring and styling pages.

---

## **Contributing**
Contributions are welcome! If you have ideas or improvements, please:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
For questions or support, contact us at:
- Email: support@todoapp.com
- Website: [Todo App](https://todoapp.com)

---

This README file includes all essential details for users and contributors to understand, install, and use the application effectively. Let me know if you want further adjustments or if you'd like to include any additional information!

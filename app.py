    # app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def get_posts():
    # Simulates 100 posts
    posts = [{"id": i, "title": f"Post {i}"} for i in range(1, 101)]
    return jsonify(posts), 200

@app.route('/users', methods=['GET'])
def get_users():
    # Simulates 10 users
    users = [{"id": i, "name": f"User {i}"} for i in range(1, 11)]
    return jsonify(users), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    # Simulates 200 todos
    todos = [{"id": i, "task": f"Todo {i}", "completed": False} for i in range(1, 201)]
    return jsonify(todos), 200

@app.route('/comments', methods=['GET'])
def get_comments():
    # Simulates 500 comments
    comments = [{"id": i, "body": f"Comment {i}"} for i in range(1, 501)]
    return jsonify(comments), 200

if __name__ == '__main__':
    app.run(debug=True)
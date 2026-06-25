from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Root endpoint showing the overview of available resources."""
    return jsonify({
        "message": "Welcome to the REST API",
        "resources": {
            "/posts": "100 posts",
            "/comments": "500 comments",
            "/albums": "100 albums",
            "/photos": "5000 photos",
            "/todos": "200 todos",
            "/users": "10 users"
        }
    }), 200

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = [{"id": i, "title": f"Post Title {i}"} for i in range(1, 101)]
    return jsonify(posts), 200

@app.route('/comments', methods=['GET'])
def get_comments():
    comments = [{"id": i, "body": f"Comment body {i}"} for i in range(1, 501)]
    return jsonify(comments), 200

@app.route('/albums', methods=['GET'])
def get_albums():
    albums = [{"id": i, "title": f"Album Title {i}"} for i in range(1, 101)]
    return jsonify(albums), 200

@app.route('/photos', methods=['GET'])
def get_photos():
    photos = [{"id": i, "title": f"Photo {i}", "url": f"https://via.placeholder.com/{i}"} for i in range(1, 5001)]
    return jsonify(photos), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = [{"id": i, "task": f"Task {i}", "completed": False} for i in range(1, 201)]
    return jsonify(todos), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = [{"id": i, "username": f"user_{i}", "email": f"user{i}@example.com"} for i in range(1, 11)]
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)
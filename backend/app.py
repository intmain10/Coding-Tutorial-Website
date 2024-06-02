from flask import Flask, jsonify, send_from_directory
import os
import pickle

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/tutorials')
def tutorials():
    tutorials = [
        {
            'id': 1,
            'title': 'HTML Basics',
            'description': 'Learn the basics of HTML, the essential language for creating web pages.',
            'link': '/tutorials/html',
            'image': 'assets/images/html.jpg'
        },
        {
            'id': 2,
            'title': 'CSS Fundamentals',
            'description': 'Master the basics of CSS and learn how to style your web pages.',
            'link': '/tutorials/css',
            'image': 'assets/images/css.jpg'
        },
        {
            'id': 3,
            'title': 'JavaScript Essentials',
            'description': 'Get started with JavaScript, the programming language of the web.',
            'link': '/tutorials/javascript',
            'image': 'assets/images/js.jpg'
        }
    ]
    return jsonify(tutorials)

@app.route('/api/model')
def get_model():
    model_path = os.path.join('models', 'example_model.pkl')
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
    except FileNotFoundError:
        return jsonify({'error': 'Model file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'model': str(model)})

if __name__ == '__main__':
    app.run(debug=True)

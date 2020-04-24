from flask import Flask, render_template, jsonify, request

app = Flask("__main__")


COURSES = [
    {
        'title': 'Title 1',
        'author': 'JL',
        'paperback': True
    },
    {
        'title': 'Title 2',
        'author': 'JL2',
        'paperback': False    
    },
    {
        'title': 'Title 3',
        'author': 'JL3',
        'paperback': True
    }
]

@app.route("/")
def my_index():
    return render_template("index.html", username="Jennifer Li")
    # return "Hello World"

@app.route('/about')
def about():
    return render_template("about.html", username="Jennifer Li")

@app.route('/courses', methods=['GET', 'POST'])
def all_courses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        COURSES.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'paperback': post_data.get('paperback')
        })
        response_object['message'] = 'Course added!'
    else:
        response_object['courses'] = COURSES
    return jsonify(response_object)

app.run(debug=True)

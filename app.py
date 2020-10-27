from flask import Flask, render_template

app = Flask(__name__)

names = ['Andrea', 'Elena', 'Edoardo', 'Francesco']
posts=[
    {
        'author': 'Mohammad',
        'title': 'Flask session title 1',
        'content': 'please continue.... this is a test',
        'date_posted': '19 Oct. 2020'
    },
    {
        'author': 'Andrea',
        'title': 'Flask session title 2',
        'content': 'please continue.... to verify that\'s',
        'date_posted': '19 Oct. 2020'
    },
    {
        'author': 'Edoardo',
        'title': 'Flask session title 3',
        'content': 'please continue.... everything\'s working fine',
        'date_posted': '19 Oct. 2020'
    },
    {
        'author': 'Sina',
        'title': 'Flask session title 4',
        'content': 'please continue.... to write',
        'date_posted': '19 Oct. 2020'
    }
]


@app.route('/user/<id>')
def name(id):
    id = int(id)
    if id > len(names):
        return render_template('404.html'), 404
    return render_template('student.html', id=id, name=names[id])


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts, name_website='IS LAB tests')


@app.route('/blog_layout')
def blog_layout():
    return render_template('blog2.html', posts=posts, name_website='IS LAB tests')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)

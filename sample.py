from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'flask'

school_dict = {'Art 🎨': ['Art', 'Dance', 'Design', 'Fashion Design',
                          'Film, Television and Multimedia', 'Fine Art', 'Theatre'],
               'Biotechnology and Bioengineering 🌱': ['Bio-Mechatronic Engineering', 'Food Science and Biotechnology', 'Integrative Biotechnology'],
               'Business 💵': ['Business Administration', 'Entrepreneurship & Innovation',
                               'Global Business Administration'],
               'Computing 💻': ['Computer Science and Engineering'],
               'Confucian Studies & Eastern philosophy': ['Confucian and Oriental Studies'],
               'Economics': ['Economics', 'Global Economics', 'International Trade an Policy', 'Statistics'],
               'Education 🏫': ['Computer Education', 'Education', 'Education in Classical Chinese',
                                'Mathematics Education'],
               'Engineering ⚙️': ['Advanced Materials Science and Engineering', 'Architecture', 'Chemical Engineering',
                                  'Civil, Architectural Engineering and Landscape Architecture',
                                  'Culture and Technology',
                                  'Mechanical Engineering', 'Systems Management Engineering'],
               'Information and Communication Engineering ⚡': ['Electronic and Eletical Engineering',
                                                               'Information and Communication Engineering',
                                                               'Semiconductor Systems Engineering'],
               'Institute for Convergence 🌎': ['Biomedical Engineering', 'Culture and Technology', 'Data Science',
                                                'Applied Artificial Intelligence'],
               'International Office': ['Korean Studies'],
               'Liberal Arts 📖': ['Chinese Language and Literature', 'Classics', 'Cross-cultural Studies',
                                   'English Language and Literature', 'French Language and Literature',
                                   'German Language and Literature', 'History', 'Humanistic Future Studies',
                                   'Interdisciplinary Linguistics', 'Japanology', 'Korean Language and Literature',
                                   'Korean Literature in Classical Chinese', 'Library and Information Science',
                                   'Philosophy', 'Russian Language and Literature',
                                   'Studies of Glocal-Cultural Contents'],
               'Medicine 🏥': ['Medicine'],
               'Pharmacy 💊': ['Pharmacy'],
               'Science 🔬': ['Biological Sciences', 'Chemistry', 'Mathematics', 'Physics'],
               'Social Sciences': ['Child Psychology and Education', 'College of Social Sciences',
                                   'Consumer and Family Sciences', 'Contracts and Rights', 'Media & Communication',
                                   'Political Science and Diplomacy', 'Psychology', 'Public Administration',
                                   'Public Affairs', 'Social Welfare', 'Sociology'],
               'Sport Science 🏃': ['Sport Science'],
               'Sungkyun Convergence Institute': ['Major of Energy Science']
               }


@app.route('/')
def hello():
    return '<h1>Hello world!</h1>'


@app.route('/main')
def mainpage():
    return render_template('mainpage.html', school_dict=school_dict)


@app.route('/bootstrap')
def bootstrap():
    return render_template('temp.html')


@app.route('/major/<major>')
def user(major):
    return render_template('major.html', major=major)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

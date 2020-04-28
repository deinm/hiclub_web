from flaskapp import app
from flask import render_template
from flaskapp.data_parser import *

school_id_dict = {'Dance': 'SKD', 'Design': 'DES', 'Fashion Design': 'FDM',
                  'Film, Television and Multimedia': 'FTM', 'Fine Art': 'ART', 'Theatre': 'DAT',

                  'Bio-Mechatronic Engineering': 'EBM', 'Food Science and Biotechnology': 'FBT',
                  'Integrative Biotechnology': 'IBT',

                  'Business Administration': 'BUS', 'Entrepreneurship & Innovation': 'EPN',
                  'Global Business Administration': 'GBA',

                  'Computer Science and Engineering': 'SWE',

                  'Confucian and Oriental Studies': 'COS',

                  'Economics': 'ECO', 'Global Economics': 'GEC',
                  'International Trade an Policy': 'INT', 'Statistics': 'STA',

                  'Computer Education': 'COM', 'Education': 'EDU',
                  'Education in Classical Chinese': 'HAN', 'Mathematics Education': 'MAE',

                  'Advanced Materials Science and Engineering': 'EAM', 'Architecture': 'ADD',
                  'Chemical Engineering': 'ECH',
                  'Civil, Architectural Engineering and Landscape Architecture': 'CAL',
                  'Mechanical Engineering': 'EME', 'Systems Management Engineering': 'ESM',

                  'Electronic and Eletical Engineering': 'EEE',
                  'Information and Communication Engineering': 'ICE',
                  'Semiconductor Systems Engineering': 'SSE',

                  'Biomedical Engineering': 'GBE', 'Culture and Technology': 'CNT',
                  'Data Science': 'DSC', 'Applied Artificial Intelligence': 'AAI',

                  'Korean Studies': 'IKS',

                  'Chinese Language and Literature': 'CHI', 'Classics': 'CLA',
                  'Cross-cultural Studies': 'CCS', 'English Language and Literature': 'ENG',
                  'French Language and Literature': 'FRE', 'German Language and Literature': 'GER',
                  'History': 'HIS', 'Humanistic Future Studies': 'HFS',
                  'Interdisciplinary Linguistics': 'ILI', 'Japanology': 'JAP',
                  'Korean Language and Literature': 'DKL', 'Korean Literature in Classical Chinese': 'KLC',
                  'Library and Information Science': 'LIS', 'Philosophy': 'PHL',
                  'Russian Language and Literature': 'RUS',
                  'Studies of Glocal-Cultural Contents': 'GCC',

                  'Medicine': 'MED',

                  'Pharmacy': 'PHR',

                  'Biological Sciences': 'BIO', 'Chemistry': 'CHY', 'Mathematics': 'MTH',
                  'Physics': 'PHY',

                  'Child Psychology and Education': 'KID', 'College of Social Sciences': 'USS',
                  'Consumer and Family Sciences': 'CON', 'Contracts and Rights': 'PIL',
                  'Media & Communication': 'MCJ', 'Political Science and Diplomacy': 'PSD',
                  'Psychology': 'PSY', 'Public Administration': 'PAD',
                  'Public Affairs': 'GLD', 'Social Welfare': 'SWF', 'Sociology': 'SOC',

                  'Sport Science': 'SPT'}

school_dict = {'Art 🎨': ['Dance', 'Design', 'Fashion Design',
                          'Film, Television and Multimedia', 'Fine Art', 'Theatre'],
               'Biotechnology and Bioengineering 🌱': ['Bio-Mechatronic Engineering', 'Food Science and Biotechnology',
                                                       'Integrative Biotechnology'],
               'Business 💵': ['Business Administration', 'Entrepreneurship & Innovation',
                               'Global Business Administration'],
               'Computing 💻': ['Computer Science and Engineering'],
               'Confucian Studies & Eastern philosophy 💭': ['Confucian and Oriental Studies'],
               'Economics 📉': ['Economics', 'Global Economics', 'International Trade an Policy', 'Statistics'],
               'Education 🏫': ['Computer Education', 'Education', 'Education in Classical Chinese',
                                'Mathematics Education'],
               'Engineering ⚙️': ['Advanced Materials Science and Engineering', 'Architecture',
                                  'Chemical Engineering',
                                  'Civil, Architectural Engineering and Landscape Architecture',
                                  'Culture and Technology',
                                  'Mechanical Engineering', 'Systems Management Engineering'],
               'Information and Communication Engineering ⚡': ['Electronic and Eletical Engineering',
                                                               'Information and Communication Engineering',
                                                               'Semiconductor Systems Engineering'],
               'Institute for Convergence 🌎': ['Biomedical Engineering', 'Culture and Technology', 'Data Science',
                                                'Applied Artificial Intelligence'],
               'International Office 🇰🇷': ['Korean Studies'],
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
               'Social Sciences 👨‍👩‍👧‍👦': ['Child Psychology and Education', 'College of Social Sciences',
                                               'Consumer and Family Sciences', 'Contracts and Rights',
                                               'Media & Communication',
                                               'Political Science and Diplomacy', 'Psychology', 'Public Administration',
                                               'Public Affairs', 'Social Welfare', 'Sociology'],
               'Sport Science 🏃': ['Sport Science']
               }


@app.route('/')
@app.route('/main')
def mainpage():
    return render_template('mainpage.html', school_dict=school_dict, school_id_dict=school_id_dict)


@app.route('/major/<major>')
def user(major):
    major_course_list = data_parser(major)

    return render_template('major.html', major=major, course_list=major_course_list)

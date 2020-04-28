import pandas as pd
import os


def data_parser(major=None):
    data_path = os.path.join(os.path.dirname(__file__), "data/2019.csv")
    data = pd.read_csv(data_path)
    data = data.drop('Lecture Name', axis=1)
    data = data.drop('Professor Name', axis=1)

    # nan값 제
    data = data[data['course_id'].notna()]

    rows = ['semester', 'course_id', 'official_lecture_name', 'official_prof_name', 'english', 'assignments', 'team_projects', 'attendance', 'exams', 'total_score', 'etc']

    # english column to numeric values
    data = data.replace('All of the course are delivered in English', 5)
    data = data.replace(['Most of the course are delivered in English, but Korean is seldomly used.English and Korean are used evenly', 'Most of the course are delivered in English, but Korean is seldomly used.'], 4)
    data = data.replace('English and Korean are used evenly', 3)
    data = data.replace('Korean is mostly used', 1)

    # exams column to numeric values

    data['exams'] = data['exams'].replace('None', 0).replace('More than 2', 3).fillna(0)

    # assignment/team_projects column to numeric values

    data = data.replace('Many', 3)
    data = data.replace('Average', 2)
    data = data.replace('None', 1)

    # attendance column to numberic values

    data = data.replace(["checked every time", "Checked every time"], 3)
    data = data.replace(["Checked randomly", "checked randomly"], 2)
    data = data.replace(["Not checked", "not checked"], 1)

    # total score data type to int
    data['total_score'] = data['total_score'].astype(int)

    # print(data.info())

    major_data_dict_list = []

    for i in data.index:
        val = data.loc[i]
        if major in val['course_id']:
            single_dict = {}
            for key in rows:
                single_dict[key] = val[key]

            major_data_dict_list.append(single_dict)

    # print(major_data_dict_list)

    return major_data_dict_list


if __name__ == '__main__':
    data = data_parser('SWE')
    print(data)
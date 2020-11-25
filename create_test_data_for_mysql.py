#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
출처 : https://blog.gyus.me/2020/generate-sample-data-with-python
student_score DDL
create table student_score
(
	uid int auto_increment
		primary key,
	name varchar(30) null comment '이름',
	grade int null,
	class_no int null,
	year int null comment '연도',
	semester int null comment '1 혹은 2',
	subject varchar(30) null comment '과목',
	score int null comment '점수'
)
comment '학생의 성적테이블';
"""

import os
import pathlib
import random

from getpass import getpass

from faker import Faker

fake = Faker('ko_KR')
과목들 = ['국어', '영어', '수학', '과학', '사회', '윤리', '지리', '기술', '체육']

filename = "student_score.sql"


def get_test_data():
    이름 = fake.name()        # 자동으로 이름을 만들어서 가져온다.
    연도 = random.randrange(2010, 2021)  # 2010 ~ 2020
    학년 = random.randrange(1, 4)  # 1~3
    반 = random.randrange(1, 6)  # 1~5
    datas = []
    for y in range(2):
        학기 = y + 1
        for idx, 과목 in enumerate(과목들):  # for 반복문에서 enumerate함수와 함께 index(idx) 사용하기. -> print(idx,data)
            점수 = random.randrange(0, 101)
            data = f"('{이름}',{연도}, {학기}, {학년}, {반}, '{과목}', {점수}),"     # data format(형식)
            datas.append(data)          # data를 datas 리스트에 넣는다.
    return datas
# retunr 결과
"""
('서지후',2017, 2, 2, 1, '기술', 71),
...
('서지후',2017, 2, 2, 1, '체육', 61),
"""

def create_datas():
    f = open(filename, "w")
    f.write("""TRUNCATE TABLE my_db.student_score;
INSERT INTO my_db.student_score (name, year, semester, grade, class_no, subject, score)
VALUES
""")
    datas = []
    for x in range(1000):
        one_person_data = get_test_data()
        datas += one_person_data

    # 마지막에 있는 ,(콤마) 를 ; (세미콜론) 으로 변경하기 위한 코드
    datas[-1] = datas[-1][:-1] + ';'
    for data in datas:
        f.write(data)
    f.close()


if __name__ == '__main__':
    create_datas()
    current_dir = pathlib.Path().absolute()
    dump_file = f"{current_dir}/{filename}"
    print("덤프파일 경로 : ", dump_file)
    mypass = getpass("패스워드를 입력해주세요 : ")
    os.system(f"mysql -u root -p{mypass} < {dump_file}")

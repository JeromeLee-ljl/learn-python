import sqlite3


def test():
    with sqlite3.connect('test.db') as conn:
        try:
            cursor = conn.cursor()
            cursor.execute('create table user (id varchar(20) primary key,name varchar(20),score int)')
            cursor.execute(r'insert into user values ("a-001","adam",95)')
            cursor.execute(r'insert into user values ("a-002","bart",62)')
            cursor.execute(r'insert into user values ("a-003","lisa",78)')
            cursor.execute(r'insert into user values ("a-004","tom",83)')
        finally:
            cursor.close()
        conn.commit()

    def get_score_in(low, high):
        "返回指定分数区间的名字，按分数从低到高排序"
        with sqlite3.connect('test.db') as conn:
            try:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM user WHERE score > ? AND score < ? ORDER BY score', (low, high))
                values = cursor.fetchall()
            finally:
                cursor.close()
        return values

    if __name__ == '__main__':
        r = get_score_in(60, 100)
        print(r)


if __name__ == '__main__':
    test()

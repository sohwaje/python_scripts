class buckets(object):
    def __init__(self, thing):
        self.thing = thing

    # 메소드(함수)    
    def open_the_buckets(self):
        for line in self.thing:
            print(line)

"""
인스턴스
"""
    first_buckets = buckets(["apple","banna"])
    second_buckets = buckets(["bread","meal"])

"""
인스턴스.메소드() 형식으로 호출
"""
first_buckets.open_the_buckets()
second_buckets.open_the_buckets()

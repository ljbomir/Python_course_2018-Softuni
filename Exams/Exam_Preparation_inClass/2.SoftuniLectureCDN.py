import re


class Lecture:

    def __init__(self, lecture, trainer,course,duration,server):
        self.lecture = lecture
        self.trainer = trainer
        self.course = course
        self.server = server
        self.duration = duration

    def to_minutes(self):
        pattern = r"(?P<hours>\d+)h(?P<minutes>\d+)m"
        match = re.finditer(pattern, self.duration)
        return sum(list(int(x.group('minutes')) + int(x.group('hours'))*60 for x in match))

    def geturl(self):
        pattern = "https://streamcdn{}.softuni.bg/course={}&lecture={}&trainer={}"
        result = pattern.format(self.server, self.course, self.lecture, self.trainer)
        return result


def format_time(_min):
    hours = int(_min / 60)
    minutes = _min % 60
    print(f"total duration: {hours:02d}:{minutes:02d}:00")


all_duration = 0
server_duration = 0
server_index = 1
lectures = []
line = input()
while "scrape" not in line:
    tokens = dict(x.split(':') for x in line.split(';'))
    tokens['server'] = server_index
    current_lecture = Lecture(**tokens)
    server_duration += current_lecture.to_minutes()
    if server_duration > 600:
        server_duration = current_lecture.to_minutes()
        server_index += 1
        current_lecture.server = server_index

    lectures.append(current_lecture)

    line = input()

Null, course_trainer, name = line.split(' ')
for lecture in lectures:
    if course_trainer == "course":
        if name == lecture.course:
            print(f"{lecture.geturl()}")
            all_duration += lecture.to_minutes()
    elif course_trainer == "trainer":
        if name == lecture.trainer:
            print(f"{lecture.geturl()}")
            all_duration += lecture.to_minutes()

format_time(all_duration)


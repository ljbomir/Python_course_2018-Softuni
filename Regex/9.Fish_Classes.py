import re
data = input()

pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<status>['\-x])>"
fish_match = re.finditer(pattern, data)

if not re.search(pattern, data):
    print("No fish found.")


class Fish:
    def __init__(self, match, tail, body, status):
        self.match = match
        self.tail = tail
        self.body = body
        self.status = status


count = 1
for fish in fish_match:
    fish_body = fish.groupdict()['body']
    fish_tail = fish.groupdict()['tail']
    fish_status = fish.groupdict()['status']
    fish_obj = Fish(match=fish.group(), tail=fish_tail, body=fish_body, status=fish_status)
    body_sm = len(fish_body)*2
    tail_sm = len(fish_tail)*2

    if len(fish_tail) > 5:
        fish_obj.tail = 'Long'
    elif len(fish_tail) > 1:
        fish_obj.tail = 'Medium'
    elif len(fish_tail) == 1:
        fish_obj.tail = 'Short'
    elif len(fish_tail) == 0:
        fish_obj.tail = None

    if len(fish_body) > 10:
        fish_obj.body = 'Long'
    elif len(fish_body) > 5:
        fish_obj.body = 'Medium'
    else:
        fish_obj.body = 'Short'

    if fish_status == "'":
        fish_obj.status = 'Awake'
    elif fish_status == "-":
        fish_obj.status = 'Asleep'
    elif fish_status == "x":
        fish_obj.status = 'Dead'

    print(f"Fish {str(count)}: {fish_obj.match}")
    if fish_obj.tail is None:
        print(f"  Tail type: {fish_obj.tail}")
    else:
        print(f"  Tail type: {fish_obj.tail} ({tail_sm} cm)")
    print(f"  Body type: {fish_obj.body} ({body_sm} cm)")
    print(f"  Status: {fish_obj.status}")
    count += 1









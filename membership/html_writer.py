import csv
import datetime


class HTMLWriter:
    def __init__(self):
        self.filename = "members.csv"
        with open(self.filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            self.data = {}
            for id, name in reader:
                self.data[name] = id

    def write(self, name):
        today = datetime.datetime.today()

        data = f"""\
<html>

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type">
    <link rel="stylesheet" href="index.css">
</head>

<body class="c4">
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c7"><span class="c5">일련번호 {self.data[name]}</span></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c6"><span class="c8">회 원 증</span></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c1"><span class="c3">이름 {name}</span></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c6"><span class="c3">당 회원은 본 회의 회원임을 인정합니다.</span></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c2"></p>
    <p class="c6"><span class="c3">{today.year}년 {today.month}월 {today.day}일</span></p>
    <p class="c6"><span class="c3">프린터협회장</span></p>
</body>

</html>"""

        with open("index.html", "w", encoding="utf-8-sig") as file:
            file.write(data)


if __name__ == "__main__":
    html_writer = HTMLWriter()
    html_writer.write("홍길동")

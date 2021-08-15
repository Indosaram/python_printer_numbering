import json
import datetime


class HTMLWriter:
    def __init__(self):
        self.filename = "data.json"

    def initialize(self):
        data = {"current_number": 0}
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def write(self):
        with open(self.filename, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        data["current_number"] += 1
        with open(self.filename, "w", encoding="utf-8-sig") as f:
            json.dump({"current_number": data["current_number"]}, f)

        data = f"""\
<html>
<table cellspacing="0" cellpadding="0" border="1" style="width: 159px; height: 163px; font-size: 10pt; border-width: 0px; border-color: rgb(0, 0, 0); border-collapse: collapse; border-style: solid; background-color: rgb(255, 255, 255);" class="">
<tbody>
<tr>
<td style="width: 158px; height: 162px; border-width: 1px; border-color: rgb(0, 0, 0); border-style: solid;">
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;"><br></p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;">발권시간 : {self.current_time}</p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;"><br></p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;"><span style="font-size: 22pt; font-weight: bold;">순 번 표</span></p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;"><br></p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;">대 기 번 호</p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;"><span style="font-size: 22pt;">{data["current_number"]}</span></p>
<p style="font-size: 13.3333px; text-align: center; line-height: 160%;"><br></p>
</td>
</tr>
</tbody>
</table>
<p style="line-height: 160%;"><br></p>
</html>"""

        with open("index.html", "w") as file:
            file.write(data)

    @property
    def current_time(self):
        return datetime.datetime.now().strftime("%H시 %M분")


if __name__ == "__main__":
    html_writer = HTMLWriter()
    html_writer.initialize()
    html_writer.write()

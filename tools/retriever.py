import time
import argparse
import bs4.element as element

from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup


def get_cases(tag: element.Tag):
    title = tag.find("h3").text
    pre = tag.find("pre").text.replace("\r", "")
    try:
        additional = tag.find("p").text
        return title, pre, additional
    except AttributeError:
        return title, pre


class TestCase:
    def __init__(self, i_cases, o_cases, path, q_indicator="a"):
        self.i_cases = i_cases
        self.o_cases = o_cases
        self.path = path / f"{q_indicator}"

        for i in range(3):
            (self.path / f"{i}").mkdir(exist_ok=True, parents=True)

    def dump(self):
        for j, (i, o) in enumerate(zip(self.i_cases, self.o_cases)):
            with open(self.path / f"{j}/input.txt", "w") as f:
                f.write(i)

            with open(self.path / f"{j}/answer.txt", "w") as f:
                f.write(o)


class Question:
    def __init__(self, tag: element.Tag):
        self.tag = tag
        self.task_statement = None
        self.part = None
        self.test_cases = []
        self.answe_cases = []
        self.q_indicator = ""

    def _title(self) -> str:
        return self.tag.find("span").text

    def _source_limit(self) -> str:
        return self.tag.find("p").text

    def _task_statement(self):
        self.task_statement = self.tag.find(
            "div", attrs={"id": "task-statement"})

    def _given_score(self) -> str:
        if self.task_statement is None:
            self._task_statement()

        return self.task_statement.find("p").text

    def _part(self):
        if self.task_statement is None:
            self._task_statement()

        self.part = self.task_statement.find_all(
            "div", attrs={"class": "part"})

    def _question_text(self) -> str:
        if self.part is None:
            self._part()

        q_tag = self.part[0]
        title = q_tag.find("h3").text
        texts = [p.text for p in q_tag.find_all("p")]

        question_text = f"### {title}\n"
        question_text += "\n".join(texts) + "\n\n"
        return question_text

    def _limitation(self) -> str:
        if self.part is None:
            self._part()

        l_tag = self.part[1]
        title = l_tag.find("h3").text
        texts = [li.text for li in l_tag.find_all("li")]

        limitation_text = f"### {title}\n\n* "
        limitation_text += "\n* ".join(texts) + "\n\n"
        return limitation_text

    def _input(self) -> str:
        if self.part is None:
            self._part()

        in_tag = self.part[2]
        title = in_tag.find("h3").text
        text = in_tag.find("p").text
        ex = in_tag.find("pre").text.replace("\r", "")

        input_text = f"### {title}\n"
        input_text += f"{text}\n\n"
        input_text += f"```\n{ex}```\n"
        return input_text

    def _output(self) -> str:
        if self.part is None:
            self._part()

        o_tag = self.part[3]
        title = o_tag.find("h3").text
        text = o_tag.find("p").text

        output_text = f"### {title}\n"
        output_text += text + "\n\n"
        return output_text

    def _cases(self) -> str:
        if self.part is None:
            self._part()

        text = ""
        for i in range(4, 10):
            tag = self.part[i]
            if not ("入力例" in tag.text or "出力例" in tag.text):
                break
            cases = get_cases(tag)
            if "入力例" in cases[0]:
                self.test_cases.append(cases[1])
            elif "出力例" in cases[0]:
                self.answe_cases.append(cases[1])
            text += f"### {cases[0]}\n\n"
            text += f"```\n{cases[1]}```\n"
            if len(cases) == 3:
                text += f"{cases[2]}\n\n"
        return text

    def dump(self, path: Path):
        title = self._title()
        source_limit = self._source_limit()
        question_text = self._question_text()
        limitation = self._limitation()
        input_text = self._input()
        output_text = self._output()
        cases = self._cases()

        self.q_indicator = title[0].lower()

        text = f"## {title}\n"
        text += source_limit + "\n\n"
        text += question_text + limitation + input_text + output_text
        text += cases
        with open(path / "README.md", "a") as f:
            f.write(text)

        cases = TestCase(self.test_cases, self.answe_cases, path / "cases",
                         self.q_indicator)
        cases.dump()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contest")

    args = parser.parse_args()
    contest = args.contest
    url = f"https://atcoder.jp/contests/{contest}/tasks_print"
    try:
        html = urlopen(url)
        time.sleep(1)
    except HTTPError:
        print("contest does not exist")
        exit(0)

    soup = BeautifulSoup(html, "html.parser")
    path = Path(contest.upper())

    q_tags = soup.find_all("div", attrs={"class": "col-sm-12"})
    questions = [Question(q_tag) for q_tag in q_tags if len(q_tag) != 0]

    for q in questions:
        q.dump(path)

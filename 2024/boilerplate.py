from jinja2 import Environment, FileSystemLoader
import requests
import argparse
from pathlib import Path
import re
from bs4 import BeautifulSoup
import sys


parser = argparse.ArgumentParser(
    prog="boilerplate",
    description="""Sets up boilerplate code and an input file for a new day of Advent of Code.
    Requires a .session file containing the session cookie to access online information.
    Online info includes inferring a label and downloading input.""",
)
parser.add_argument('day', type=int)
parser.add_argument('--label', type=str, default=None)
parser.add_argument('--nocode', action='store_true')
parser.add_argument('--notest', action='store_true')
parser.add_argument('--noinput', action='store_true')
parser.add_argument('-f', '--force', action='store_true',
                    help="Force the overwriting of files (DANGEROUS)")


class style():
  RED = '\033[31m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  RESET = '\033[0m'
  CHECK = '\u2714\ufe0e'


template_env = Environment(
    loader=FileSystemLoader("templates"),
    )


def read_session_key() -> str:
    print(f"Reading session key:", end=" ")
    try:
        with open('.session', 'r') as f:
            session_key = f.read().strip()
            key_len = len(session_key)
            if key_len != 128:
                raise ValueError(f"Wrong session key length: {key_len}")
        print(style.GREEN + style.CHECK + style.RESET)
    except ValueError:
        print(style.RED + "X - bad key value" + style.RESET)
    except:
        print(style.RED + "X - error reading session key" + style.RESET)
    return session_key


def sanitize_title(s):
    return s.lower().replace(" ", "_")


if __name__ == '__main__':
    args = parser.parse_args()
    session_key = read_session_key()
    cookies = dict(session=session_key)
    if args.label is None:
        print("Reading label from AoC page title:", end=" ")
        r = requests.get(f"https://adventofcode.com/2024/day/{args.day}", cookies=cookies)
        bs = BeautifulSoup(r.text, 'html.parser')
        title = bs.h2.string.strip(' -')
        day_str, human_title = title.split(": ")
        assert day_str == f"Day {args.day}"
        args.label = sanitize_title(human_title)
        if re.match(r'^[_a-z]+$', args.label):
            print(style.GREEN + style.CHECK + style.RESET + f" using label {args.label}")
        else:
            print(style.RED + f"X label {args.label} may need more sanitizing" + style.RESET)
            sys.exit(-1)

    full_label = f"day{args.day:02d}_{args.label}"
    fn_code = f"{full_label}.py"
    fn_test = f"test_{full_label}.py"
    fn_input = f"../private/2024/{full_label}_input.txt"
    for name, fn in [("code", fn_code), ("test", fn_test), ("input", fn_input)]:
        print(f"Checking {name} path:", end=" ")
        path = Path(fn)
        if path.exists():
            print(style.RED + f"X - {fn} already exists" + style.RESET)
            sys.exit(-1)
        else:
            print(style.GREEN + style.CHECK + style.RESET + f' {fn} doesn\'t exist')

    print("Reading input data:", end=" ")
    r = requests.get(f"https://adventofcode.com/2024/day/{args.day}/input", cookies=cookies)
    if r.status_code == 200:
        print(style.GREEN + style.CHECK + style.RESET)
    else:
        print(style.RED + f"X - status code {r.status_code}" + style.RESET)
    print("Writing input data:", end=" ")
    with open(fn_input, "w", encoding='utf-8') as f:
        f.write(r.text)
    print(style.GREEN + style.CHECK + style.RESET)

    template_params = dict(full_label=full_label, day=args.day)
    
    print("Getting code template:", end=" ")
    code_template = template_env.get_template('code.py')
    print(style.GREEN + style.CHECK + style.RESET)
    print("Writing code file:", end=" ")
    with open(fn_code, "w", encoding='utf-8') as f:
        f.write(code_template.render(template_params))
    print(style.GREEN + style.CHECK + style.RESET)

    print("Getting test template:", end=" ")
    test_template = template_env.get_template('test.py')
    print(style.GREEN + style.CHECK + style.RESET)
    print("Writing test file:", end=" ")
    with open(fn_test, "w", encoding='utf-8') as f:
        f.write(test_template.render(template_params))
    print(style.GREEN + style.CHECK + style.RESET)


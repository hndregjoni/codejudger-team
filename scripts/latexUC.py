#! /usr/bin/env python3

from sys import argv

path = argv[1]

def splt(line):
    return line.split("|")

def no_spaces(line):
    return [*filter(
        lambda i: not (i.isspace() or i == ''),
        line
    )]

def trim(line):
    return [*map(
        lambda s: s.strip(),
        line
    )]

def sanitize(t):
    return t.replace("<br>", "\\newline")\
        .replace("&", "\\&")\
        .replace("%", "\\%")\
        .replace("{", "\\{")\
        .replace("}", "\\}")\
        .replace("–","-")\
        .replace("’", "'")\
        .replace("'", "\\'")\
        .replace("-", "\\-")\
        .replace("_", "\\_")

def read_lines(_lines):
    lines = [*map(
        splt,
        _lines
    )]

    lines = [*map(
        no_spaces,
        lines
    )]

    lines = [*map(
        trim,
        lines
    )]

    return lines


def get_table(data):
    title = sanitize(data[0][1])

    summary = sanitize(data[2][1])
    dependency = sanitize(data[3][1])
    actors = sanitize(data[4][1])
    precond = sanitize(data[5][1])
    desc_m = sanitize(data[6][1])
    desc_alt = sanitize(data[7][1])
    nfreq = sanitize(data[8][1])
    postcond = sanitize(data[9][1])

    return f"""\\begin{{table}}[htbp]
\\centering
\\begin{{tabularx}}{{\\textwidth}}{{|l|X|}}
\\hline
UC Name & {title} \\\\ \hline

Summary &  {summary} \\\\ \hline

Dependency & {dependency} \\\\ \hline

Actors & {actors} \\\\ \hline

Preconditions & {precond} \\\\ \hline

Description of the Main Sequence & {desc_m} \\\\ \hline

Descriptoin of the Alternative Sequence & {desc_alt} \\\\ \hline

Non functional requirements & {nfreq} \\\\ \hline

Postcondition & {postcond} \\\\ \hline

\end{{tabularx}}
\end{{table}}
"""

with open(path) as f:
    all_lines = f.readlines()

    # print([*map(
    #     splt,
    #     lines
    # )])

    # result = []

    # for line in lines:
    #     result.append(line.split("|"))
    #     # print(line.split("|").strip())
    #     # print("AAAA")
    
    # result = no_spaces(result)
    
    print(get_table(read_lines(all_lines)))

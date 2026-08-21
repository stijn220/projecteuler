import html, re

LATEX = {
    r"\times": "×", r"\cdot": "·", r"\div": "÷",
    r"\le": "<=", r"\leq": "<=", r"\ge": ">=", r"\geq": ">=",
    r"\ne": "!=", r"\neq": "!=", r"\approx": "~", r"\equiv": "=",
    r"\ldots": "...", r"\cdots": "...", r"\dots": "...",
    r"\pm": "+/-", r"\infty": "oo", r"\%": "%",
    r"\left": "", r"\right": "", r"\,": " ", r"\;": " ", r"\!": "",
}

def to_text(s):
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p\s*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"\$\$?(.*?)\$\$?", r"\1", s, flags=re.S)

    s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", s)
    for cmd in sorted(LATEX, key=len, reverse=True):
        s = s.replace(cmd, LATEX[cmd])
    s = re.sub(r"\\[a-zA-Z]+", "", s)          # overige commando's weg
    s = re.sub(r"\^\{([^{}]*)\}", r"*\1", s)   # ^{10} -> *10
    s = s.replace("{", "").replace("}", "")

    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()

print("Plak je HTML, sluit af met een lege regel:\n")

regels = []
while True:
    try:
        regel = input()
    except EOFError:
        break
    if regel == "":
        break
    regels.append(regel)

print("\n--- plain text ---\n")
print(to_text("\n".join(regels)))
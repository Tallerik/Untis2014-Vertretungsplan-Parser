


def load(url):
    from urllib.request import urlopen

    import json

    html = urlopen(url)

    text = html.read()

    text = str(text)

    tags =["html", "head", "meta", "script", "link", "style", "body", "title", "a", "input"]

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(text, 'html.parser')



    text = soup.prettify().splitlines()

    l = False

    textneu = []

    data = []

    for t in text:



        if """<tr class="\\'list" odd\\'="">""" in t:

            l = True

        if '</table>' in t:

            l = False

        if l:

            textneu.append(t)



    tr = False

    td = False

    eintrag = []

    for txt in textneu:

        if not "<" in txt:
            if not "\\n" in txt:
                eintrag.append(txt.lstrip())







        if "</tr" in txt:

            data.append(eintrag)

            eintrag = []

    return data



output = {}

output["heute"] = load("http://www.bas-vertretung.de/v-plan/heute/subst_001.htm")
output["morgen"] = load("http://www.bas-vertretung.de/v-plan/morgen/subst_001.htm")
print(output)
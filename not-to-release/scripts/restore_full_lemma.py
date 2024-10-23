#!/usr/bin/env python3

# Copyright 2020 Peter Kolb (https://github.com/pekoli)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import os
import re


def process_file(infile, outfile, logfile):
    with open(infile, "rt") as inf, open(outfile, "wt") as outf:
        for line in inf:
            if line.startswith("#") or line.strip() == "":
                outf.write(line)
            else:
                columns = line.split("\t")
                if columns[3] == "NOUN" and columns[2] != "unknown":
                    old_lemma = columns[2]
                    columns = process_word(columns)
                    outf.write("\t".join(columns))
                    if old_lemma != columns[2]:
                        mark = " *" if (columns[2] != columns[1] and old_lemma[0] in ['Ä','Ö','Ü'] and
                                        not columns[2].endswith(old_lemma) and not columns[1].endswith(columns[2])) else ""
                        logfile.write(old_lemma+" -> "+columns[2]+" ("+columns[1]+" "+columns[3]+mark+")\n")
                else:
                    outf.write(line)


def process_word(columns):
    lemma = find_substring(columns[1], columns[2])  # Arbeitsplatz-Rechnern   Rechner
    if lemma is None:
        lemma = find_substring(columns[1], columns[2].lower())  # Wirtschaftsministerien   Ministerium
    if lemma is None:
        lemma = find_substring(columns[1], umlaut(columns[2]), columns[2])  # Pferde-Äpfeln   Apfel
    if lemma is None:
        lemma = find_substring(columns[1], umlaut(columns[2]).lower(), columns[2].lower())  # Pferdeäpfeln   Apfel
    if lemma is not None:
        columns[2] = lemma
    return columns


def find_substring(wordform, lemma, ohne_umlaut=None):
    max_suffix_length = int(len(lemma) / 2)  # the suffix that is cut off may not be longer than the remaining stem
    for i in range(0, max_suffix_length+1):
        lemma_prefix = lemma[0:len(lemma)-i]
        try:
            idx = wordform.rindex(lemma_prefix)
        except ValueError as err:
            idx = -1
        if idx != -1:
            if ohne_umlaut is None:
                return wordform[0:idx] + lemma
            else:
                return wordform[0:idx] + ohne_umlaut
    return None


def umlaut(lemma):
    # Stammvokal ist letzter Vokal (a,o,u,au,oo), aber -e, -en, -el, -er am Wortende zählt nicht.
    ul_pat = re.compile(r"^(.*?)(a|o|u|au|oo)([bcdfghklmnpqrstvwxzß]+)(e|en|el|er)?$", re.IGNORECASE)
    m = ul_pat.search(lemma)
    if m:
        prefix = m.group(1) if (m.group(1) is not None) else ""
        stammvokal = m.group(2)
        cons = m.group(3) if (m.group(3) is not None) else ""
        ende = m.group(4) if (m.group(4) is not None) else ""
        if stammvokal == "au":
            lemma = prefix+"äu"+cons+ende
        elif stammvokal == "Au":
            lemma = prefix+"Äu"+cons+ende
        elif stammvokal == "oo":
            lemma = prefix+"ö"+cons+ende
        elif stammvokal == "a":
            lemma = prefix+"ä"+cons+ende
        elif stammvokal == "A":
            lemma = prefix+"Ä"+cons+ende
        elif stammvokal == "o":
            lemma = prefix+"ö"+cons+ende
        elif stammvokal == "O":
            lemma = prefix+"Ö"+cons+ende
        elif stammvokal == "u":
            lemma = prefix+"ü"+cons+ende
        elif stammvokal == "U":
            lemma = prefix+"Ü"+cons+ende
    return lemma


if __name__ == "__main__":
    with open("restore-lemmas.log", "wt") as logfile:
        files = os.listdir(sys.argv[1])
        for file in files:
            if file.endswith(".conllu"):
                process_file(file, file+".rl", logfile)

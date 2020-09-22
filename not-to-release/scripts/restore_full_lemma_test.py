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
import unittest
from scripts.restore_full_lemma import process_word


class TestLemma(unittest.TestCase):

    def test_process_word(self):
        columns = ["", "Wirtschaftsministerien", "Ministerium"]
        columns = process_word(columns)
        self.assertEqual("Wirtschaftsministerium", columns[2])

        columns = ["", "Fettdruck-As", "A"]
        columns = process_word(columns)
        self.assertEqual("Fettdruck-A", columns[2])

        columns = ["", "Arbeitsplatz-Rechnern", "Rechner"]
        columns = process_word(columns)
        self.assertEqual("Arbeitsplatz-Rechner", columns[2])

        columns = ["", "Pferde-Äpfeln", "Apfel"]
        columns = process_word(columns)
        self.assertEqual("Pferde-Apfel", columns[2])

        columns = ["", "Pferdeäpfeln", "Apfel"]
        columns = process_word(columns)
        self.assertEqual("Pferdeapfel", columns[2])

        columns = ["", "Fachkräfte", "Fachkraft"]
        columns = process_word(columns)
        self.assertEqual("Fachkraft", columns[2])

        columns = ["", "Multimedia-Fachkräfte", "Fachkraft"]
        columns = process_word(columns)
        self.assertEqual("Multimedia-Fachkraft", columns[2])

        columns = ["", "Systemhäusern", "Haus"]
        columns = process_word(columns)
        self.assertEqual("Systemhaus", columns[2])

        columns = ["", "Börsengänge", "Gang"]
        columns = process_word(columns)
        self.assertEqual("Börsengang", columns[2])

        columns = ["", "US-Bundesstaaten", "Staat"]
        columns = process_word(columns)
        self.assertEqual("US-Bundesstaat", columns[2])


if __name__ == '__main__':
    unittest.main()

# Restore full lemma

## What?
For most compound words the HDT lemma annotation contains only the headword. This mainly concerns nouns
 as in the following examples:
```
# sent_id = hdt-s10009
7       Leitungsinfrastruktur   Infrastruktur   NOUN    NN      Gender=Fem|Number=Sing|Person=3 2       obj     _       _

# sent_id = hdt-s10011
6       Stellenstreichungen     Streichung      NOUN    NN      Gender=Fem|Number=Plur|Person=3 4       conj    _       _

# sent_id = hdt-s10015
17      Vorstandvorsitzender    Vorsitzender    NOUN    NN      Case=Nom|Gender=Masc|Number=Sing|Person=3       16      nsubj   _       
```
but also adjectives:
```
# sent_id = hdt-s10005
2       US-amerikanische        amerikanisch    ADJ     ADJA  Degree=Pos|Gender=Neut|Number=Sing      3       amod 
```
This poses problems for some use cases like neural lemmatisation. We therefore provide a script to
restore the full lemma in the CONLLU files. 

The script `restore_full_lemma.py` uses the word form and lemma columns of the CONLLU files to
rebuild the full lemma. This is achieved by simply adding the missing prefix (if any) from the word form
to the lemma (for nouns only).
Cases with umlaut are also handled. Lines where the lemma is "unknown" are ignored.

In total, 216974 lemmas are changed.

As a by-product, some existing errors in the lemma annotation are corrected. The following table gives
examples.

| word form               | original (incorrect) lemma | restored lemma        |
|-------------------------|----------------------------|-----------------------|
| Computermonitore        | Tor                        | Computermonitor       |
| Administration          | Ration                     | Administration        |
| Massenspeichereinheiten | Reinheit                   | Massenspeichereinheit |
| MBit/s                  | s                          | MBit/s                |
| Strings                 | Ring                       | String                |

## Installation and usage

The script requires Python 3. No additional packages need to be installed.

To process all files ending with `.conllu` in the specified directory:
```
python3 restore_full_lemma.py <DIR>
```
For each CONLLU file `<F>` in `<DIR>` an output file named `<F>.rl` with the restored lemmas is created.
The input files are not touched.

A log file named `restore-lemmas.log` is also created in the working directory. It lists all changes
that were made.

## Unit test

To run the unit test add the `scripts` directory to your Python path:
```bash
export PYTHONPATH=$PYTHONPATH:/path/to/UD_German-HDT/scripts
```
Then run the tests:
```bash
python3 scripts/restore_full_lemma_test.py
```

## Relevant issues

- [lemma of compound words contains only the headword #3](https://github.com/UniversalDependencies/UD_German-HDT/issues/3)
- [Investigate making use of HDT for German default models for improved robustness #294](https://github.com/stanfordnlp/stanza/issues/294)

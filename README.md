# Summary

UD German-HDT is a conversion of the Hamburg Dependency Treebank, created at the University of Hamburg through manual annotation in conjunction with a standard for morphologically and syntactically annotating sentences as well as a constraint-based parser.


# Introduction

The Hamburg Dependency Treebank consists of 261,821 sentences (4.8M tokens). The sentences were all sourced from the German news site heise.de, from articles published between 1996 and 2001. The content of the articles ranges from formulaic periodic updates on new BIOS revisions and processor models or quarterly earnings of tech companies over features about general trends in the hardware and software market to general coverage of social, legal and political issues in cyberspace, sometimes in the form of extensive weekly editorial comments. The creation of the treebank through manual annotation was largely interleaved with the creation of a standard for morphologically and syntactically annotating sentences as well as a constraint-based parser.

For UD_German-HDT, 206,794 sentences (3.8M tokens) from the original HDT were converted with [TrUDucer](https://gitlab.com/nats/TrUDucer), a treebank conversion tool created by Felix Hennig and extended by Maximilian Wendt and Emanuel Borges Völker. The conversion has a very high
accuracy of 97% (checked on a manually converted subset of the treebank). Annotation information not captured in the original annotation was resolved by using external data sources (Wiktionary) and manual input from annotators.

# Data quality

While the conversion is automatic, the rules are quite extensive and have been developed over the course of more than a year.  We manually confirmed the correctness on relevant sub-sets and monitored the conversion.  We used external knowledge in the form of the German Wiktionary to identify inherently reflexive verbs.

The main focus of the original HDT annotation were the dependency relations.  Some morphological features are under-specified (such as “not-fem” to denote that a word is either neuter or masculine) and during the conversion process we noted that sometimes the normal noun (NN) and proper noun (NE) are mixed up in the source annotation. This translates to the conversion and we aim to fix it in the future.

# Acknowledgments

The following people worked on the conversion:
 - Emanuel Borges Völker (conversion: grammar development, annotation refinements, …)
 - Maximilian Wendt (conversion: grammar development, annotation refinements, …)
 - Felix Hennig (initial grammar development, main TrUDucer development)
 - Arne Köhn (supervision)

The following people are working on error correction:
 - Verena Blaschke 
 - Nina Böbel
 - Leonie Weissweiler


## References

If you use this treebank, please cite the following paper, describing the conversion of the HDT to UD:

```
@inproceedings{borges-volker-etal-2019-hdt,
    title = "{HDT}-{UD}: A very large {U}niversal {D}ependencies Treebank for {G}erman",
    author = {Borges V{\"o}lker, Emanuel  and Wendt, Maximilian  and Hennig, Felix  and K{\"o}hn, Arne},
    editor = "Rademaker, Alexandre  and Tyers, Francis",
    booktitle = "Proceedings of the Third Workshop on Universal Dependencies (UDW, SyntaxFest 2019)",
    month = aug,
    year = "2019",
    address = "Paris, France",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W19-8006",
    doi = "10.18653/v1/W19-8006",
    pages = "46--57",
}
```


The TrUDucer paper describing the formalism behind the conversion:

```
@inproceedings{hennig-kohn-2017-dependency,
    title = "Dependency Tree Transformation with Tree Transducers",
    author = {Hennig, Felix  and K{\"o}hn, Arne},
    editor = "de Marneffe, Marie-Catherine  and Nivre, Joakim  and Schuster, Sebastian",
    booktitle = "Proceedings of the {N}o{D}a{L}i{D}a 2017 Workshop on Universal Dependencies ({UDW} 2017)",
    month = may,
    year = "2017",
    address = "Gothenburg, Sweden",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-0407",
    pages = "58--66",
}
```

The paper describing the HDT:

```
@inproceedings{hennig-kohn-2017-dependency,
    title = "Dependency Tree Transformation with Tree Transducers",
    author = {Hennig, Felix  and K{\"o}hn, Arne},
 editor = "de Marneffe, Marie-Catherine  and Nivre, Joakim  and Schuster, Sebastian",
    booktitle = "Proceedings of the {N}o{D}a{L}i{D}a 2017 Workshop on Universal Dependencies ({UDW} 2017)",
    month = may,
    year = "2017",
    address = "Gothenburg, Sweden",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-0407",
    pages = "58--66",
}

```

The annotation guidelines of the original HDT:

```
@article{foth2006umfassende,
  title={Eine umfassende Constraint-Dependenz-Grammatik des Deutschen},
  author={Foth, Kilian A},
  year={2006},
  publisher={Fachbereich Informatik}
}
```

## Software

[TrUDucer](https://gitlab.com/nats/truducer) the software used to convert the HDT.  Comes with a pipeline to replicate the conversion of the HDT.

[jwcdg](https://gitlab.com/nats/jwcdg), the successor of the parser used for initial automatic annotation of the HDT.  It contains the lexicon with the relevant morpho-syntactic features annotated.


# Data Split

The HDT consists of three parts:
- part A (101,999 sentences) - manually annotated and checked for consistency with DECCA
- part B (104,795 sentences) - manually annotated but not checked with DECCA
- part C (55,027 sentences) - automatically parsed with WCDG and not included in the UD release

Sentences which where not accepted by the UD validation script do not appear in the current version and may be added in future releases. Of the 206,794 converted sentences, 173,247 sentences are currently included.
Due to their size, they are arranged in as follows:
- de_hdt-ud-dev.conllu (17,293 sentences) - sentences 1 to 10000 from part A, sentences 102001 to 112000 from part B
- de_hdt-ud-test.conllu (17,028 sentences) - sentences 10001 to 20000 from part A, sentences 112001 to 122000 from part B
- de_hdt-ud-train-a.conllu (68,801 sentences) - sentences 20001 to 102000 from part A
- de_hdt-ud-train-b.conllu (70,125 sentences) - sentences 122001 to 206794 from part B

de_hdt-ud-train-a.conllu and de_hdt-ud-train-b.conllu have been further split into two files each for size reasons.

# License

Heise gave permission to distribute the text for academic use; the annotations are licensed under a Creative Commons share-alike license.


# Changelog

2024-11-15 v2.15
* Fixed ADP-DET phrases that had been erroneously treated as *det* rather than *obl/nmod* (like *unter anderem, vor allem, für alle, ...*)
* Fixed multiple-subject and multiple-object errors
* Fixed error of determiners with degree (e.g., *mehr*) -- now tagged as ADV (like similar constructions in English treebanks)
* "ein" when unambiguously used as a numeral is now NUM
* Other small fixes
* Construction annotations in the [UCxn](https://github.com/LeonieWeissweiler/UCxn) framework added to MISC
    * This release adds rule-based annotations of Interrogatives, Conditionals, Existentials, and NPN (noun-preposition-noun) constructions on the head of the respective phrase, plus construction elements.
    * The UCxn v1 notation and categories are documented [here](https://github.com/LeonieWeissweiler/UCxn/blob/main/docs/UCxn-v1.pdf).

2023-05-15 v2.12
* Dative arguments are oblique, hence they are obl:arg and not iobj.
* PRON vs. DET annotation made consistent across German UD treebanks.

2021-09-08
* Fixed segmentation of contracted preposition + article.

UD 2.4: initial release

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.4
License: CC BY-SA 4.0
Includes text: yes
Genre: news nonfiction web
Lemmas: converted from manual
UPOS: converted from manual
XPOS: automatic with corrections
Features: converted from manual
Relations: converted with corrections
Contributors: Borges Völker, Emanuel; Hennig, Felix; Köhn, Arne; Wendt, Maximilan; Blaschke, Verena; Böbel, Nina; Weissweiler, Leonie
Contributing: here
Contact: nina.boebel@hhu.de
===============================================================================
</pre>

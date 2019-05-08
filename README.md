# Summary

UD German-HDT is a conversion of the Hamburg Dependency Treebank,
created at the University of Hamburg through manual annotation in
conjunction with a standard for morphologically and syntactically
annotating sentences as well as a constraint-based parser.


# Introduction

The [Hamburg Dependency Treebank](http://hdl.handle.net/11022/0000-0000-7FC7-2)
consists of 261,821 sentences (4.8M tokens). The sentences were all
sourced from the German news site heise.de, from articles published
between 1996 and 2001. The content of the articles ranges from
formulaic periodic updates on new BIOS revisions and processor models
or quarterly earnings of tech companies over features about general
trends in the hardware and software market to general coverage of
social, legal and political issues in cyberspace, sometimes in the
form of extensive weekly editorial comments. The creation of the
treebank through manual annotation was largely interleaved with the
creation of a standard for morphologically and syntactically
annotating sentences as well as a constraint-based parser.

For [UD_German-HDT](https://github.com/UniversalDependencies/UD_German-HDT),
206,794 sentences (3.8M tokens) from the original HDT were converted
with [TrUDucer](https://gitlab.com/nats/TrUDucer), a treebank
conversion tool created by Felix Hennig and extended by Maximilian
Wendt and Emanuel Borges Völker. The conversion has a very high
accuracy of 97% (checked on a manually converted subset of the
treebank). Annotation information not captured in the original annotation
was resolved by using external data sources (Wiktionary) and manual input
from annotators.

# Data quality

While the conversion is automatic, the rules are quite extensive and
have been developed over the course of more than half a year.  We
manually confirmed the correctness on relevant sub-sets and monitored
the conversion.  We used external knowledge in the form of the German
Wiktionary to identify inherently reflexive verbs.

The main focus of the original HDT annotation were the dependency
relations.  Some morphological features are under-specified (such as
“not-fem” to denote that a word is either neuter or masculine) and
during the conversion process we noted that sometimes the normal noun
(NN) and proper noun (NE) are mixed up in the source annotation. This
translates to the conversion and we aim to fix it in the future.

# Acknowledgments

The following people worked on the conversion:
 - Emanuel Borges Völker (conversion: grammar development, annotation refinements, …)
 - Maximilian Wendt (conversion: grammar development, annotation refinements, …)
 - Felix Hennig (initial grammar development, main TrUDucer development)
 - Arne Köhn (supervision)


## References

If you use this treebank, please cite the upcoming paper describing
the conversion of the HDT to UD.

The TrUDucer paper describing the formalism behind the conversion:

Hennig, Felix, & Köhn, Arne (2017). Dependency tree transformation
with tree transducers. In Proceedings of the NoDaLiDa 2017 Workshop on
Universal Dependencies (UDW 2017) (pp. 58–66). Gothenburg, Sweden:
Association for Computational Linguistics.  url:
http://www.aclweb.org/anthology/W17-0407


The paper describing the HDT:

Foth, K. A., Köhn, A., Beuck, N., & Menzel, W. (2014). Because Size
Does Matter: The Hamburg Dependency Treebank.  In Proceedings of the
Language Resources and Evaluation Conference 2014
(pp. 2326–2333). Reykjavik, Iceland: European Language Resources
Association (ELRA).  url:
http://nbn-resolving.de/urn:nbn:de:gbv:18-228-7-2013


The annotation guidelines of the original HDT:

Foth, K. A. (2006). Eine umfassende Constraint-Dependenz-Grammatik des
Deutschen. url: http://nbn-resolving.de/urn:nbn:de:gbv:18-228-7-2048


## Software

[TrUDucer](https://gitlab.com/nats/truducer) the software used to
convert the HDT.  Comes with a pipeline to replicate the conversion of
the HDT.

[jwcdg](https://gitlab.com/nats/jwcdg), the successor of the parser
used for initial automatic annotation of the HDT.  It contains the
lexicon with the relevant morpho-syntactic features annotated.

[DECCA](http://sifnos.sfs.uni-tuebingen.de/decca/), a tool to detect
and correct errors in annotated corpora


# Data Split

The HDT consists of three parts:
- part A (101,999 sentences) - manually annotated and checked for consistency with DECCA 
- part B (104,795 sentences) - manually annotated but not checked with DECCA 
- part C (55,027 sentences) - automatically parsed with WCDG and not included in the UD release

Sentences which where not accepted by the UD validation script do not appear in the current version and may be added in future releases. Of the 206,794 converted sentences, 173,247 sentences are currently included.
Due to their size, they are arranged in [Github](https://github.com/UniversalDependencies/UD_German-HDT) as follows:
- de_hdt-ud-dev.conllu (17,293 sentences) - sentences 1 to 10000 from part A, sentences 102001 to 112000 from part B
- de_hdt-ud-test.conllu (17,028 sentences) - sentences 10001 to 20000 from part A, sentences 112001 to 122000 from part B
- de_hdt-ud-train-a.conllu (68,801 sentences) - sentences 20001 to 102000 from part A
- de_hdt-ud-train-b.conllu (70,125 sentences) - sentences 122001 to 206794 from part B

# License

Heise gave permission to distribute the text for academic use; the
annotations are licensed under a Creative Commons share-alike license.


# Changelog

UD 2.4: initial release

<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.4
License: HZSK-ACA (Text) / CC BY-SA-4.0 (Annotation)
Includes text: yes
Genre: news nonfiction web
Lemmas: converted from manual
UPOS: converted from manual
XPOS: automatic with corrections
Features: converted from manual
Relations: converted with corrections
Contributors: Borges Völker, Emanuel; Hennig, Felix; Köhn, Arne; Wendt, Maximilan
Contributing: elsewhere
Contact: Arne Köhn <arne@chark.eu>
===============================================================================
</pre>

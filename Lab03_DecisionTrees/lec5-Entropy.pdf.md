Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.6
====== lec5-Entropy.pdf ======
Text date: [[Zettelkasten:2024:04:26|2024-04-26]] Modi date: [[Zettelkasten:2024:04:26|2024-04-26]]
@ARTIKEL  
[*] **[[../lec5-Entropy.pdf]] **



{{../lec5-Entropy.pdf.avif?width=500}}

Pages:           6


10-704: Information Processing and Learning

Spring 2015

Lecture 5: January 27
Lecturer: Aarti Singh

Scribes: Kyle Soska

Note: LaTeX template courtesy of UC Berkeley EECS dept.
Disclaimer: These notes have not been subjected to the usual scrutiny reserved for formal publications.
They may be distributed outside this class only with the permission of the Instructor.

5.1

Summary of Entropy Estimators

5.1.1

Discrete variables

We have a distribution P supported on a finite alphabet {1, ..., d} with P (X = j) = pj where

d
P

pj = 1. We

j=1

observe independent samples {Xi }ni=1 ∼ P and would like to estimate some functional of P , say the entropy:

H(P ) = −

d
X

pj log2 (pj )

j=1

For this problem, we discussed two estimators:
• Plugin Estimator
The plugin estimator uses empirical estimates of the frequencies pˆj = n1
estimate of the entropy as follows:
Hˆn = −

d
X

Pn

i=1 1[Xi = j] to obtain an

pˆj log2 (pˆj )

j=1

• LP Estimator
The LP Estimator works by transforming the samples {Xi }ni=1 into a fingerprint, which is the
vector f = (f1 , f2 , ...) for which fi is the number of elements in the domain that occurred i times in
the sample, i.e. with empirical frequency i/n. The fingerprint is also known as the “type” of a sample.
The fingerprint serves as an estimate of the histogram of the distribution which is defined as the
mapping hp : (0, 1] → N ∪ {0} for which hp (x) is the number of domain elements that occur with
probability exactly x. More formally, hp (x) = |{α : pα = x}|. The entropy can be computed from the
histogram as follows:
H(x) = −

X

hp (x)x log2 (x)

x:hp (x)6=0

We can then quantize (0, 1] to a grid Q = {q1 , ..., qk } and let hj be the variable associated with hp (qj )
to obtain the approximation:
5-1


Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.6
====== Stochastik_CheatSheet.pdf ======
Text date: [[Zettelkasten:2024:04:23|2024-04-23]] Modi date: [[Zettelkasten:2024:04:23|2024-04-23]]
@ARTIKEL  
[*] **[[../Stochastik_CheatSheet.pdf]] **



{{../Stochastik_CheatSheet.pdf.avif?width=500}}

Pages:           7


Intelligent Data Analysis and Machine Learning
Probability theory: Cheat sheet
University of Potsdam, Department of Computer Science, 2019
Lena Jäger

Let X,Y,Z be random variables with range RX , RY , RZ , respectively.

1

Distributions

1.1

Discrete random variables

A discrete random variable is a random variable whose range is either finite or countably infinite (e.g., N, Q, {1, 0}
or {1, 2, 3, 4, 5, 6}).
1. The probability distribution is defined by a probability mass function P that assigns a probability P (X =
x) ∈ [0, 1] to each x ∈ RX . Instead of P (X = x), one can also write PX (x).
P
i) The sum of all probabilities must be 1:
P (X = x) = 1
x∈RX

ii) The probability that one out of a union of n elementary events x1 , x2 , . . . xn occurs equals the sum of
n
n
S
P
their individual probabilities: P ( xi ) =
P (xi ).
i=1

i=1

iii) The probability that one out of a union of disjoints events A1 , A2 , . . . An occurs equals the sum of the
n
n
S
P
individual probabilities of each event: P ( · Ai ) =
P (Ai ).
i=1

i=1

iv) It is not possible that nothing happens: P (X = ∅) = 0
2. The cumulative probability massPfunction gives the probability of X being less or equal than a certain
number: cmf (x) = P (X ≤ x) =
P (X = y).1
y≤x

1.2

Continuous random variables

A continuous random variable is a random variable whose range is uncountably infinite (e.g., the real numbers or
an interval on the real numbers).
1. The probability distribution is defined by a densitiy function p : RX → R+
0 where RX is R or a closed
interval [a, b] on R.
i) The probability of X taking a value within an interval [a, b] is the definite integral of the density function
Rb
over this interval (the area under the graph of the density function): P (X ∈ [a, b]) = p(x)dx
a

ii) The probability of X taking a specific value a is zero: P (X = a) =

Ra

p(x)dx = 0

a

iii) The integral over all possible values of X is 1: P (X ∈ R) =

R∞

p(x)dx = 1 if RX = R and

−∞

P (X ∈ [a, b]) =

Rb

p(x)dx = 1 if RX = [a, b].

a
1 Usually, statistics textbooks use F (x) rather thatn cmf (x). In this summary, I am using cmf to refer to the cumulative probability

mass function in order to clearly distinguish it from the cumulative density function used for continuous random variables which is
usually also referred to by F (x) (see below).


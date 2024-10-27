# General notes:

1) Am pastrat fisierele skyscrapers_lines.tms, skyscrapers_columns.tms si skyscrapers_lines_visibility.tms pentru a va explica pe baza lor
cum am ajuns la varianta finala, skyscrapers_column_visibility.tms nu ar fi avut sens sa fie facut separat dupa ideea mea, voi explica mai tarziu de ce.

2) Evident ca nu sunt psihopat sa scriu 11.6k linii "de mana", am folosit meta-programare asa cum ati indicat, un exemplu il regasiti in fisierul
meta-programare.py, unde aveti un exemplu de generare de stari de tranzitie la stanga, stari folosite pentru a transpune matricea. S-a dat si mult
copy paste dar cred ca e de la sine inteles.

3) Fiecare stare face ceva destul de specific, am incercat sa le dau nume cat mai intuitive dar si specifice in acelasi timp, la vizibilitati am mai
folosit acronime precum: RTL = RightToLeft sau BTFC = BottomTopFirstColumn, diferenta intre First si Fourth o fac inlocuind F cu Fo, de exemplu BTFoC = BottomTopFourthColumn. Am folosit acronime si la transpunerea matricei, adica la verificarea simpla pe coloane: SDFS = SecondDigitFirstSet, 

## Skyscrapers_lines

Voi prezenta pe scurt etapele pe care le am gandit ca sa ajung la masina turing pe care ati vazut o:
1) *skipFirstVisibilityFigures* => starea initiala, eu vreau sa trec peste primele 4 cifre si ultimele 4,
                                 deoarece nu sunt relevante verificarii pe linii
2) Dupa ce trece de aceasta stare, la un moment dat dam de caracterul #, de unde mergem intr o stare intermediara,
*goRightAfterDiez*

3) Analizand formatul inputului, observam ca daca dupa diez sunt 2 cifre consecutive, practic ne aflam la ultima secventa
de cifre, care si aceasta trebuie ignorata, pentru ca e irelevanta verificarii pe linii, aici intervine starea *goRightAfterDiezSecondNr*

4) Din aceasta stare, daca gasim pe banda 1,2,3,4 inseamna ca atunci clar suntem la ultima secventa de cifre deci trebuie ignorate,
daca in schimb dam de caracterul ":", mergem in alta stare intermediara, *transitionBack*, pentru a ne intoarce la inceputul
secventei de 4 cifre care trebuie verificate

5) Din aceasta stare ne ducem din nou intr-o stare intermediara, *goRight*, care are un nume foarte sugestiv, ne deplaseaza in dreapta
pe banda, si dupa va incepe procesul de verificare propriu zis

6) *lookFor* * unde steluta e regex, reprezinta toate starile de verificare a cifrelor dintr o secventa de 4, spre exemplu:
 * daca din starea *goRight* gasesc 1 pe banda, inseamna ca am nevoie de o stare *lookForTwoThreeFour* care face exact ce zice numele;
 * dupa din aceasta stare am iar 4 cazuri, daca gasesc 1 din nou, putem intra deja in starea N, daca gasesc 2, 3 sau 4 vom avea inca
 3 stari *lookForThreeFour*, *lookForTwoFour*, respectiv *lookForTwoThree*, si tot asa
 * in total avem 15 astfel de stari (nr de submultimi al unei multimi cu 4 elemente, in cazul nostru {1, 2, 3, 4} mai putin multimea vida)

## Skyscrapers_columns

Aici se afla "the bulk of the code", adica aproximativ 8500 de linii. Inainte sa ma apuc de implementarea verificarii pe coloane m am gandit
cum reduc problema la verificarea pe linii. Concluzia ? Transpun matricea, si dupa pot aplica exact acelasi algoritm la vizibilitatea pe
coloane dupa ce o implementez pe cea de la linii, pentru ca prin transpunerea matricei practic transform coloanele in linii.

Deci, in fisierul skyscrapers_columns.tms problema se reduce de fapt la transpunerea matricei, pe care am facut o astfel:

1) Este important sa intelegeti cum am vrut eu sa arate banda dupa aceasta transpunere, ca sa nu modific inputul initial,
am ales sa copiez totul la dreapta dupa un caracter arbitrar, "s", iar mai apoi sa delimitez coloanele transpuse cu alte 
4 caractere alese arbitrar, respectiv "a", "b", "c", "d", deci dupa transpunere pe banda va fi de exemplu:
*3321#3:2134:1#2:3241:2#2:1423:2#1:4312:3#1233 s2314a1243b3421c4132d*

2) Pentru a face transpunerea avem nevoie de cate un set de destul de multe stari pentru toate cele 16 cifre pe care vrem
sa le copiem, deoarece acestea se afla pe 16 pozitii diferite, deci noi trebuie sa tinem minte pe ce pozitie se gaseste
cifra pe care vrem sa o copiem, valoarea ei in sine, si unde o scriem.

3) Ca sa explic "algoritmul" de transpunere a matricei vom lua drept exemplu copierea a celei de a 2 a cifre din primul set,
adica de fapt prima cifra din a 2 a linie din inputul initial. Avem urmatoarele stari:

* *skipFirstVisibilityFiguresCVBackSDFS* o stare care trece peste cifrele de vizibilitate de la finalul inputului pana la ":"
* *findSecondDigitFirstSet*, avem nevoie de aceasta stare pentru a semnala inceputul "numaratorii" de pozitii pe care trebuie 
sa le parcurgem pana la cifra de interes
* *goLeftSecondDigit1, goLeftSecondDigit2, ... goLeftSecondDigit21* acestea sunt stari intermediare pentru a contoriza 
pozitia pe care ne aflam
* dupa ce am ajuns pe pozitia dorita, avem 4 stari pentru a tine minte cifra pe care vrem sa o copiem undeva in dreapta,
*copySecondDigitOne, copySecondDigitTwo, copySecondDigitThree, copySecondDigitFour*
* din aceste stari ma deplasez in dreapta de tot pana la s, si dupa intru in alta stare dupa caz: 
*moveTwoWriteOne, moveTwoWriteTwo, moveTwoWriteThree, moveTwoWriteFour*, Two reprezinta contorul cifrei pe care o copiez,
am nevoie de aceste stari pentru ca intre input si s am lasat un spatiu, deci am nevoie de stari intermediare ca sa nu
scriu in spatiul dintre s si input
* folosind aceste stari, gasesc primul spatiu liber dupa s si scriu in functie de stare 1, 2, 3 sau 4
* dupa scriere se trece intr o stare in care se cauta urmatoarea cifra de copiat, in cazul nostru *findThirdDigitFirstSet*

4) Dupa fiecare set copiat, adica dupa fiecare coloana scrisa, adaug pe rand cate un caracter, asa cum am zis,
a, b, c sau d, pentru a delimita coloanele, spre ex in starea *findFirstDigitSecondSet*, inainte sa ma duc in starea,
*skipFirstVisibilityFiguresCVBackFDSS*, scriu pe banda caracterul a in urmatorul spatiu liber

5) Avand in vedere ce am zis la nr.4, ulterior toate starile de tipul skipFirstVisibility*, *moveFiveWriteOne* sau
*findSecondDigitSecondSet* vor avea mai multe linii scrise deoarece trebuie ignorat caracterul a, apoi b, c, sau d
unde e cazul

Dupa transpunere rationamentul de verificare ramane acelasi ca la cel pe linii cum am mai zis, doar ca
aici nu vom mai avea ":", "#" plus alte cifre care despart coloanele, ci doar a,b,c,d. Starile de verificare
sunt aceleasi ca la verificarea pe linii la care am mai adaugat acronimul CV = Column Verification, de exemplu:
*lookForTwoThreeFourCV, lookForTwoFourCV* etc.

## Skyscrapers_lines_visibility

Vizibilitatea pe linii am implementat o dupa ce am scris fisierul skyscrapers_final.tms pentru a mi simplifica treaba.
Dupa ce am "linkat" verificarea simpla pe linii de cea pe coloane, adaugand cateva stari de tranzitie in care doar ma
pozitionez la inceputul inputului, am realizat ca dupa aceste 2 verificari am garantia ca atat pe linii cat si pe coloane
am cifre diferite de la 1 la 4, deci am inceput sa scriu la fisierul skyscrapers_lines_visibility.tms avand asta in calcul.
Am ajuns la concluzia ca am urmatoarele situatii posibile:

```
2    24** 
2    34**
2    14**
2    3*4*
2    3**4
```
```
3    2134
3    2314
3    2341
3    1324
3    1342
3    1243
```
```
**43	2
**42	2
**41	2
*4*3	2
4**3	2
```
```
3421	3
4312	3
4132	3
1432	3
4231	3
2431	3
```

Inca un lucru pe care l am facut a fost mai intai sa verific toate vizibilitatile de la stanga la dreapta si apoi, 
"la intoarcere", sa le verific pe toate de la dreapta la stanga, de aici vin tipurile de stari LeftToRight si RightToLeft 
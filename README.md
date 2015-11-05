### __AICodeFactory
I'm trying to make a program that can program a program by itself.

	* API seems to be necessary and THEY ARE NEEDED!
	* Give Limited choices for Program, use generated API for output. Pair control. Evaluation Method
	
	* Generate a python file that create "Hello World"
	* Verify the output
####Quest 1
```
	Pool:	A(All Possible Letters)
	Quest1:	>> Hello World!
	LineLimit:	1
	Renforce:	cmpr(compare), sqn(sequence), %(persentage)
	Feedback:	W-PoL(weight of possition of letters)
```
####Quest 2
```
	P:	A
	Q2:	<< 1, >> Hello World!
		<< ?, >> Exit
	LL:	10
	R:	cmpr, sqn, %
	F:	W-PoL
```
####Quest 3
```
	P:	A
	Q3:	<< 1, >> 2
		<< 2, >> 3
		<< 100, >> 101
	LL:	5
	R:	cmpr, offset, Accuracy
	F:	W-Acc(weight according to accuracy)
```
####Quest 4
```
	P:	A
	Q4:	<< 1, >> 5
		<< 2, >> 25
		<< 3, >> 125
	LL:	10
	R:	cmpr, offset, Accuracy
	F:	W-Acc
```
####Quest 5
```
	P:	A
	Q5:	<< 1, >> xoxoxoxoxo
		<< 2, >> xxooxxooxxoo
		<< 3, >> xxxoooxxxoooxxxooo
	LL:	10
	R:	cmpr, sqn, %
	F:	W-PoL

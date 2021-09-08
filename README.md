# Gödelfish

Gödelfish is a Gödel numbering for the (joke) esoteric programming language [Deadfish](https://esolangs.org/wiki/Deadfish).

It has a [page on the esolangs wiki](https://esolangs.org/wiki/G%C3%B6delfish).

This repo contains the [specification](docs/Gödelfish-article.pdf) and some simple scripts to work with (generate, convert, and evaluate) code and Gödel numbers.

There are two kinds of Gödelfish numbers (𝜑̈):

* Natural Gödelfish: Non-negative integers (ℕ), representing all possible Deadfish programs.
* Unnatural Gödelfish: Real numbers from (ℝ − ℕ), representing all possible Brainf\*\*\* programs.

Both kinds are converted numerically into [Brainfoctal](https://esolangs.org/wiki/Brainfoctal) (a Gödel numbering of Brainf\*\*\*), and then can be executed as bf to produce the expected output.

## Why?

* Experiment converting between two programming languages directly from Gödel numberings using equations / mathematical functions.
* Experiment mapping a Gödel numbering of a program to its output solely by means of equations / mathematical functions. (Natural Gödelfish does this to evalute the admittedly simple Deadfish language).

## Scripts

* **/scripts**
  * [dfᗒgf.py](scripts/dfᗒgf.py): Converts Deadfish code into Gödelfish integer
  * [gfᗒbf8.py](scripts/gfᗒbf8.py): Converts a Gödelfish integer into [Brainfoctal](https://esolangs.org/wiki/Brainfoctal)
  * [gfᗒO.py](scripts/gfᗒO.py): Converts a Natural Gödelfish value into its resulting output encoding (i.e. evaluates a program directly from its Gödel number)
* [gf.py](gf.py): Wraps all of the above into one 'helpful' utility.

## Usage and examples

Clone this repo from Github and use the scripts directly.


### Hello World! (Unnatural conversion)
    $ ./gf.py -b -0.02267050412500270959407579713247251696870738403389181782725188269749688319088642196836222187626319203264982082686924411902690
    ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

Assuming you have a bf interprerter `bff4` on your `$PATH` you can pipe the output to see it evaluate:

    $ ./gf.py -b -0.02267050412500270959407579713247251696870738403389181782725188269749688319088642196836222187626319203264982082686924411902690 | bff4
    Hello World!

### Deadfish overflow test (Natural conversion)
The `0d` prefix for the number is a custom base-4 notation:

    $ ./gf.py -b 0d011221203
    ++-[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<++-[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>>>+<+<<-]>>[>[<<<+>+>>-]<<[>>+<<-]>-]>[-]<<<[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>>>+<+<<-]>>[>[<<<+>+>>-]<<[>>+<<-]>-]>[-]<<<[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<++-[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>>>+<+<<-]>>[>[<<<+>+>>-]<<[>>+<<-]>-]>[-]<<<[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<-[>+>+<<-]>>[<<+>>-]>-<<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>+>+<<-]>>[<<+>>-]>+>++>+[->+++[-<++++>]<<]<[->>-<<]+>>[<<->>[-]]<<[[-]<[-]>]<[>>+>+<<<-]>>>[<<<+>>>-]<<+>[<->[>++++++++++<[->-[>+>>]>[+[-<+>]>+>>]<<<<<]>[-]++++++++[<++++++>-]>[<<+>>-]>[<<+>>-]<<]>]<[->>++++++++[<++++++>-]]<[.[-]<]<>++++++++++.++++++++++++[-]<

The input number `0d011221203` is equivalent to decimal 23139, or hex `0x5a63`, and all of these formats are recognised as input by the interpreter. Conceptually it is important that the program input is a single numeric value, *not* a string of symbols from one specific alphabet or in one specific base.

Assuming you have a bf interprerter `bff4` on your `$PATH` you can pipe the output to see it evaluate the correct Deadfish accumulator output value:

    $ ./gf.py -b 0d011221203 | bff4
    288

### Output encoding evalutation

	$ ./scripts/gfᗒO.py -h
	usage: gfᗒO.py [-h] value [radix] [digits]

	Convert a Natural Gödelfish value into its resulting output encoding.

	positional arguments:
	  value       Gödelfish value, 𝜑̈ ∈ ℕ
	  radix       radix of output values
	  digits      number of digits per output value in base radix

### Deadfish overflow test (Natural evaluation)

Base-10 output encoding:

    $ ./scripts/gfᗒO.py 0d011221203 10
    288

Hexadecimal ouput:

    $ ./scripts/gfᗒO.py 0d011221203 16
    0x120

### Multi-value output (Natural evaluation):

Base-10, 3 digits per output value:

    $ ./scripts/gfᗒO.py 0x59565555d55555555555555d555f570000000000000000000000000000000000000003000000000020c000357000c0003 10 3
    72101108108111032119111114108100


Base-10, 5 digits per output value:

    $ ./scripts/gfᗒO.py 0x59565555d55555555555555d555f570000000000000000000000000000000000000003000000000020c000357000c0003 10 5
    7200101001080010800111000320011900111001140010800100

Base-16, 16 digits per output value:

    $ ./scripts/gfᗒO.py 0x59565555d55555555555555d555f570000000000000000000000000000000000000003000000000020c000357000c0003 16 16
    0x480000000000000065000000000000006c000000000000006c000000000000006f00000000000000200000000000000077000000000000006f0000000000000072000000000000006c0000000000000064


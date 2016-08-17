# JI-GPACal

This is the gpa calculator for um-sjtu ji. I use it to calculate my own GPA.

## Usage

Firstly, you need to type your grade one by one. I do not read the grade from SJTU or JI database because this way is more flexible.

````bash
cp grade-sample.xlsx grade.xlsx
open grade.xlsx # just in Mac OS X, you can direcly open it with Microsoft Office
````

Since `grade.xlsx` is in `.gitignore`, it won't be pushed or pulled. After typing the grade, you can get your GPA directly by

````bash
python3 gpacal.py # python2 may be OK, but I use python3 
````

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

## Dependencies

The only package is `xlrd`. You can install it by `pip3`.

````bash
pip3 install xlrd
````

## Improvements and Contribution

There are several points open to pull request. Other improvements are also welcomed.

- [X] Neglect the line if letter grade is empty (it is useful because I can type the course just after taking it). Completed by [@CZY](https://github.com/IFICL).
- [ ] Support `csv` file.
- [ ] Can be used without python environment (actually only use `py2exe` is okay).



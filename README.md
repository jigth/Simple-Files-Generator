# Simple-Files-Generator

Generate arbirary amount of files within arbitrary directories using a simple Python Script.

I made this repo to save the code used to generate multiple files using a Python3 script and make it available to readers of a post of mine named "Rsync, a faster backup option", available at [my personal website's blog](https://jigth-v2.netlify.app/blog/backup-copy-files-rsync)

**NOTE:** The python script was generated using ChatGPT V4 (paid), adjusted using some Prompt Engineering techniques and validated by myself in a Linux environment created using AWS EC2 service.

## Usage

First create a virtualenv (make sure you have the necessary dependencies to do so, more info available [here](https://docs.python.org/3/library/venv.html))
```bash
python -m venv env
```

Then activate the environment
```bash
source env/bin/activate # Linux and MacOS
.\venv\Scripts\activate.bat # Windows CMD
.\venv\Scripts\Activate.ps1 # Windows PowerShell
```

And finally run the program using a syntax like the following: 

```
python3 <scriptName> <totalNumberOfFiles> <directory1> [...<more directories>]
```

**Example:**

```bash
python3 simple-files-generator.py 20 dir1 dir2
```

20 files (in total) should be generated at dir1 and dir2 directories with random contents and paragraphs.

If you have any issue please raise an issue.

**Author:** Daniel Ochoa Montes.

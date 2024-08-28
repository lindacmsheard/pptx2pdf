# Convert a folder of pptx files to pdf
source: https://pypi.org/project/pptxtopdf/

> :warning: Windows only - this is because of the comclient driver. 

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
To use as-is, place pptx files into the following directory
```
.\data\input\pptx
```

or adapt main.py
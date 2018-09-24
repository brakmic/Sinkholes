## Contributing
To add more sinkholes, there is a fairly easy-to-use python script called `add_rows.py`, with a complimentary python file called `addition.py`. Place any additional rows into `addition.py` and then run `add_rows.py` and it should take care of adding it to all of the various files!

Feel free to add more sinkholes via PR :)

#### Getting Started
To get setup to add rows to everything all at once, we'll need a few python packages that allow us to write various formats. Here is how we go about installing those packages in a virtual environment.
```
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
...
```

#### Adding Rows
Fork this repo, clone it down, add your new rows, push back to your fork, and then issue a PR.
```
(venv) $ # Make any necessary additions to addition.py using your preferred text editor
(venv) $ ./add_rows.py
[+] Successfully wrote out to Sinkholes_List.json
[+] Successfully wrote out to Sinkholes_List.csv
[+] Successfully wrote out to Sinkholes_List.xls
[+] Successfully wrote out to Sinkholes_List.xlsx
[+] Successfully wrote out to Sinkholes_List.ods
(venv) $ deactivate
$ git add .
$ git commit -m "Adding in X's Sinkholes"
$ git push
```

#### `add_rows.py` usage
```
usage: add_rows.py [-h] [--debug] [--sync]

optional arguments:
  -h, --help  show this help message and exit
  --debug     A debug flag; will not write out to file will only print to
              stdout using pretty print
  --sync      Sync will simply *not* perform any adding of rows to files.
              Instead, it will perform all of the same actions to sync the
              files so each file format reflects the same data.
```

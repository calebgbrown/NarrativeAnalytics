+Narrative Analytics
+=================
+
+Quick introduction to narrative analytics:
+
+1) Install Python 2.7 along with it's nltk and matplotlib packages:
+* [nltk installation instructions](http://nltk.org/install.html)
+* [matplotlib installation instructions](http://matplotlib.org/users/installing.html)
+
+2) Install a git client.
+
+3) Create an account for yourself on github, and set up SSH keys to the account.
+
+4) Run: ```git clone git@github.com:calebgbrown/NarrativeAnalytics.git```
+
+5) Add the parent directory of the tsl directory to your PYTHONPATH environment variable, on *NIX this can be done with:
+
+```source setup-env.sh```
+
+On the setup-env.sh file in the tsl directory.
+
+6) Look at the example film scripts in [example-scripts](example-scripts)
+
+7) Process the scripts into a parsed format by running:
+
+```
+cd utils
+./parse_scripts.py
+```
+
+8) Look at the parsed output under example-scripts/parsed
+
+9) Look at the [generate_reports.py](utils/generate_reports.py) and [partition.py](utils/partition.py) utility scripts for examples with what can be done with the parsed data
\ No newline at end of file

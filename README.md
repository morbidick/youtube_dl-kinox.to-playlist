# download series on kinox.to with youtubedl

## Usage

* for now edit the vars in main.py

```bash
# generate new environment
$ virtualenv -p python3 venvvirtualenv -p python3 venv
# initiate environment
$ source venv/bin/activate

# install dependencies
$ pip install -r requirements.txt
# start
$ ./main.py
# save added dependencies
$ pip freeze > requirements.txt
```

## TODO

* get new mirror if file is not available
* set output folder
* simultaneous download
* command line args
* youtube-dl plugin

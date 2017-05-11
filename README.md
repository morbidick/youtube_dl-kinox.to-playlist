# download series on kinox.to with youtubedl

## Usage

for now edit the vars in main.py

```bash
# generate new virtual environment
$ virtualenv -p python3 venv
# initiate environment
$ source venv/bin/activate

# install dependencies
$ pip install -r requirements.txt
# start
$ ./main.py

# add dependency
$ pip install my-dependency
# save added dependencies
$ pip freeze > requirements.txt
```

## TODO

* get new mirror if file is not available
* check if file exists
* set output folder
* simultaneous download
* command line args
* youtube-dl plugin

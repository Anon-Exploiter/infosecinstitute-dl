# infosecinstitute-dl

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub](https://img.shields.io/github/license/Anon-Exploiter/infosecinstitute-dl)
[![Contributors][contributors-shield]][contributors-url]
![GitHub closed issues](https://img.shields.io/github/issues-closed/Anon-Exploiter/infosecinstitute-dl)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=%40syed_umar)](https://twitter.com/syed__umar)

[contributors-shield]: https://img.shields.io/github/contributors/Anon-Exploiter/infosecinstitute-dl.svg?style=flat-square
[contributors-url]: https://github.com/Anon-Exploiter/infosecinstitute-dl/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/Anon-Exploiter/infosecinstitute-dl.svg?style=flat-square
[issues-url]: https://github.com/Anon-Exploiter/infosecinstitute-dl/issues

A small and dirty python based script to download courses from InfosecInstitute.

[![asciicast](https://asciinema.org/a/350800.svg)](https://asciinema.org/a/350800)

### Description

InfosecInstitute courses downloader. Requires **Python3** and **aria2** (for downloading).

Infosec.py automates everything, it'll return the list of all [paths](https://flex.infosecinstitute.com/portal/skills/asset/path), user will enter the path ID, it'll create a new folder and will start downloading all the path files in there. 

You also need to add your credentials in the script's main() function [L264](https://github.com/Anon-Exploiter/infosecinstitute-dl/blob/master/infosec.py#L264). The course link format is also given in the script.

```python
def main():
  ddlURLs 	= []
  host 		= "..."
  loginURL 	= "..."

  username 	= ""
  password 	= ""
```

### Requirements
- aria2
- python3
- python3-requests

### Tested On
- Ubuntu 18.04 LTS
- Pop! OS 18.04 LTS
- ~Windows~
- ~Mac OS~ (it doesn't work on Mac OS atm)

### Execution
If you want, you can edit the file `infosec.py` and hard-code the credentials in the variables or you use can environmental variables in two ways, directly through exporting in CLI or by adding credentials in `creds.sh` and source it. 

On **linux** (with `env variables`):
```bash
export IUSERNAME=test@gmail.com
export IPASSWORD=password

python3 infosec.py
```

On **linux** (with `creds.sh`): 
```bash
source creds.sh
python3 infosec.py
```

The script doesn't work well on **Mac OS** and on **Windows**. **Mac** has some weird issues in execution while Windows doesn't have `aria2` (it now does have it, but ah well) - So the solution to all this is to use a Docker container built from a `Dockerfile`. 

```bash
docker build -t infosec-institute .
docker run -it --rm -v `pwd`:/root/ -e 'IUSERNAME=test@test.com' -e 'IPASSWORD=pswd' infosec-institute
```

### Features
- Lists all courses
- Fetches course based on user's inputted Course ID
- Creates directory from the parsed ID
- Downloads and places all the courses inside the folder

### Features (not-supported)
PDF files aren't being downloaded now since they're using a external host for rendering the PDFs and that's llviewersg3a.com. Can't find a workaround for this, make sure to submit an issue or PR if you find one. 

### Filing Bugs/Contribution
Feel free to file a issue or create a PR if you come across any. Also, before creating a issue, make sure to execute the updated script with `-d` argument and share the whole output for better understanding of the issue (don't share your cookies from the first line). 
```bash
python3 infosec.py -d 
```

### Changelog
| Changes                                                                                                   | Release                                             |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Fixed login issue; changed email to username														        | 0.3 - 25-10-2020                                    |
| Lists all the courses, user will pass userID, will create folder name and will store all vids there       | 0.2 - 27-07-2020                                    |
| Initial release containing infosec.py & downloader.py -> Requires manual intervention                     | 0.1 - 26-07-2020                                    |


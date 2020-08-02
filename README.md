# infosecinstitute-dl

A small and dirty python3 based script to download courses from InfosecInstitute.

[![asciicast](https://asciinema.org/a/350800.svg)](https://asciinema.org/a/350800)

### Description

InfosecInstitute courses downloader. Requires **Python3** and **aria2** (for downloading).

Infosec.py automates everything, it'll return the list of all paths, user will enter the path ID, it'll create a new folder and will start downloading all the path files in there. 

You also need to add your credentials in the script's main() function. The course link format is also given in the script. 

### Requirements
- aria2
- python3
- python3-bs4
- python3-requests

### Tested On
- Ubuntu 18.04 LTS
- Pop! OS 18.04 LTS
- ~Windows~

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
| Lists all the courses, user will pass userID, will create folder name and will store all vids there       | 0.2 - 27-07-2020                                    |
| Initial release containing infosec.py & downloader.py -> Requires manual intervention                     | 0.1 - 26-07-2020                                    |

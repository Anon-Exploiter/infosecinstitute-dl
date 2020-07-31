# infosecinstitute-dl

A small and dirty python3 based script to download courses from InfosecInstitute.

[![asciicast](https://asciinema.org/a/350800.svg)](https://asciinema.org/a/350800)

### Description

InfosecInstitute courses downloader. Requires **Python3** and **aria2** (for downloading).

Infosec.py automates everything, just change the Course's URL in main() function and it'll automatically generate all the links for the course and will write those links in **downloads.json**. By default, it'll start downloading too, let's say you don't want to download right now and don't want to fetch all the DDL links later too (so you need downloader.py only afterwards).

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
Made the script really quickly today, did resolve some issues, there might be other issues too, feel free to file a issue or create a PR if you come across any. 

### Changelog
| Changes                                                                                                   | Release                                             |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Lists all the courses, user will pass userID, will create folder name and will store all vids there       | 0.2 - 27-07-2020                                    |
| Initial release containing infosec.py & downloader.py -> Requires manual intervention                     | 0.1 - 26-07-2020                                    |

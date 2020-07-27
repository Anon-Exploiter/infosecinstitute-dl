# infosecinstitute-dl
A small and dirty python3 based script to download courses from InfosecInstitute.

### Description

InfosecInstitute courses downloader. Requires **Python3** and **aria2** (for downloading).

Infosec.py automates everything, just change the Course's URL in main() function and it'll automatically generate all the links for the course and will write those links in **downloads.json**. By default, it'll start downloading too, let's say you don't want to download right now and don't want to fetch all the DDL links later too (so you need downloader.py only afterwards).

**Downloader.py** will automatically read **downloads.json** file and will start downloading (if S3 URLs are still alive/valid).

You also need to add your credentials in the script's main() function. The course link format is also given in the script. 

### Requirements
- aria2
- python3
- python3-bs4
- python3-requests

### Features
- Lists all courses
- Fetches course based on user's inputted Course ID
- Creates directory from the parsed ID
- Downloads and places all the courses inside the folder

### Features (not-supported)
PDF files aren't being downloaded now since they're using a external host for rendering the PDFs. Will look at it in free time. Feel free to submit a PR. 

### Filing Bugs/Contribution
Made the script really quickly today, did resolve some issues, there might be other issues too, feel free to file a issue or create a PR if you come across any. 

### Changelog
| Changes                                                      | Release                                             |
| ------------------------------------------------------------ | --------------------------------------------------- |
| Lists all the courses, user will pass userID, will create folder name and will store all vids there     | 0.2 - 27-07-2020                                    |
| Initial release containing infosec.py & downloader.py -> Requires manual intervention  | 0.1 - 26-07-2020                                    |

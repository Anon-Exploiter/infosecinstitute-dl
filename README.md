# infosecinstitute-dl
A small and dirty python3 based script to download courses from Infosec Institute. 

### Description

A simple downloader for InfoSec's courses. Requires **Python3** and **aria2** (for downloading).

Infosec.py automates everything, just change the Course's URL in main() function and it'll automatically generate all the links for the course and will write those links in **downloads.json**. By default, it'll start downloading too, let's say you don't want to download right now and don't want to fetch all the DDL links later too (so you need downloader.py only afterwards).

**Downloader.py** will automatically read **downloads.json** file and will start downloading (if S3 URLs are still alive/valid).

You also need to add your credentials in the script's main() function. The course link format is also given in the script. 

### Filing Bugs/Contribution
Made the script really quickly today, did resolve some issues, there might be other issues too, feel free to file a issue or create a PR if you come across any. 

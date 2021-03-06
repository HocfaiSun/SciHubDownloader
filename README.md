# Sci-Hub Downloader Ver.2.1

![downloader_logo](/scidownloader_new.png)

## Client update 2022/06/02
`BULK DOWNLOAD` function has been added to the new client version 2.1, please download `Scihubdownloader_for_Win_ver.2.1.zip` for new function.

Now, you can click `BULK DOWNLOAD` to select txt file to download all articles at once and don't need to input all information with `;` for separation.

The format of txt file as below:

![txt_file](/txtfile.png)

If you want to save the articles to assigned folder, please click `SAVE PATH` button and select the folder, then click `BULK DOWNLOAD` button and select txt file, the downloaded articles will be saved to the folder you selected. If you don't assign the folder, the articles will be saved to the folder where `main.exe` exists.

## About this downloader

This downloader is based on the work that finished by zaytoun (Sci-Hub API) and Israel Dryer (ttkbootstrap).

## Features

*   Download SCI articles by article's title, URL and DOI

*   Downlaod multiple articles use different combination

*   Show information when finish or unfinish downloading

*   Save the articles to the selected folder

*   Download articles everywhere with internet connection

*   SCI-HUB source can change automatically

## How to run this downloader

### Run this downloader by the source code

If you are good at coding, you can run and customize the source code, but first you need go to [zaytoun's project page](https://github.com/zaytoun/scihub.py) to download the source code which is a part of this projects, then move the file `scihub.py` in `scihub` folder to  `SciHubDownloader` folder of this project, now you can run  `main.py`  in  `SciHubDownloader` and change the code as you want. If you can't run the souce code, please don't forget to install the required modules in terminal.

### Run this downloader by clients

If you are not good at coding, you can download all of the files in this project, then extract the zip file `SciHubDownloader_for_Win.zip`. Now you can double click  `main.exe` to run this downloader directly.

## How to use this downloader

### Download articles

You can input article's title, URL or DOI, then click `DOWNLOAD` button to dowload the articles. You can also input the combination of title,URL and DOI to download multiple articles, but don't forget to add English style ';' to seperate each term.

### Save articles

If you click `DOWNLOAD` button directly, the articles will be saved in the folder where the downloader located. If you want to specify the folder you want, you can click `SAVE PATH` button to specify the save path.

### Clear input

If you want to clear your input information, you can click `CLEAR INPUT` button to clear it quickly.

## Other things

*   Please don't move `scihublogo.png` file in the folder, the downloader will not work without this file.
*   Due to the large size and bad performance of Mac version, here I will not upload Mac version.


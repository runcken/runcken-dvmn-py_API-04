# Download images from SpaceX and NASA

Script for downloading images from SpaceX launches, and also for downloading APOD and EPIC NASA images

## How to install

Clone repository to your local device. To avoid problems with installing required additinal packages, use a virtual environment, for example:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

Python3.12 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

The script doesnt uses additinal packages:

_environs==14.3.0_


After that you can run script using this command for download image from SpaceX:


```bash
python fetch_spacex_images.py
```
or for download images from NASA:


```bash
python fetch_apod_nasa_images.py
```


```bash
python fetch_epic_nasa_images.py
```

It will save images to 'images' folder.
Its possible to run script with SpaceX launch you need adding argument in console like:

```bash
python fetch_spacex_images.py --id_launch 'id launch you need'
```

Also its possible to change time period for downloading from NASA adding argument like:


```bash
python fetch_epic_nasa_images.py --days 'quantity days'
```


You will not run script without API KEY NASA, you can get it on https://api.nasa.gov

The file with the API KEY NASA isnt included in the repository. To use the script with your credentials, 
you need to create a .env file in the folder with the script, and add into it lines like API_KEY_NASA=your_key.

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.

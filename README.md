# wu — wallpaper updater
This script update wallpaper for desktop and loock screen at the same time it moves the wallpaper to a special folder for all wallpapers.
## Installation 
### Requirements
* make
* python
```bash
git clone https://github.com/kostya1F634/wu.git
cd wu
make
# you get binary "wu" in this directory
```
Or just download binary from releases and move it for example to /usr/local/bin
```bash
chmod +x wu
mv wu /usr/local/bin
```
## Usage
Idea of usage
* First create alias in shell config smh like this
```bash
alias wu="wu -d ~/path/to/wallpaper/dir -i"
# or with default directory ~/Pictures/wallpapers
alias wu="wu -i"
```
Then when you use the browser, you like the image, you download it, use the script, it is automatically update wallpapers and moved to the folder with other wallpapers like this
```bash
cd ~/Dowloads
wu example_of_image.jpg
# or
wu "example image with spae.jpg"
```

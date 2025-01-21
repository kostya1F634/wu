# wu — wallpaper updater
This script update KDE plasma's desktop and loock screen wallpaper simultaneously and at the same time it moves the wallpaper to a special folder for all wallpapers.
## Idea of Usage
* First create alias in shell config smh like this
```bash
alias wu="wu -d ~/path/to/wallpaper/dir -i"
# or with default directory ~/Pictures/wallpapers
alias wu="wu -i"
```
When you are browsing, and you see an image that you liked, you download it, use the script `wu image.jpg`, it automatically updates wallpapers and moves to the folder with other wallpapers
```bash
# Browsing -> See image -> Download image
cd ~/Dowloads
wu image.jpg
# or
wu "example image with spaces.jpg"
```
As a result, you get all the images in one place automatically
## Installation 
### Requirements
* make
* python
If you want to get only binary to /usr/local/bin
```bash
cd /tmp
git clone https://github.com/kostya1F634/wu.git
cd wu
make
make copy
# or if you want custom directory
sudo mv -м wu /path/to/your/dir
```
Or you can create link to /usr/local/bin
```bash
cd ~/
git clone https://github.com/kostya1F634/wu.git
cd wu
make
make link
# or if you want custom directory
sudo ln -sм "$(pwd)/wu" /path/to/your/dir
```
Or download binary from releases and move it for example to /usr/local/bin or create link like above
```bash
chmod +x wu
mv wu /usr/local/bin
```

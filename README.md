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
If you want get only binary for binary
```bash
cd /tmp
git clone https://github.com/kostya1F634/wu.git
cd wu
make
mv wu  /usr/local/bin/wu
```bash
cd ~/
git clone https://github.com/kostya1F634/wu.git
cd wu
make
ln -s ~/wu/wu /usr/local/bin/wu
```
Or download binary from releases and move it for example to /usr/local/bin or create link like above
```bash
chmod +x wu
mv wu /usr/local/bin
```

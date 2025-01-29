# 🏞️ wu — Wallpaper Updater script for inspiration
## ✨ Features
* 🔄 easy way to update desktop and lock screen wallpaper simultaneously
* ⚙️ automatically moves updated wallpaper to directory with all wallpapers
* 🚀 update wallpapers blazingly fast from terminal
## 💡 Idea of Usage
You can quickly change the wallpaper to the ones you like.
* First, create alias in shell config like this
```bash
alias wu="wu -d ~/path/to/wallpaper/dir -i"
# with default directory ~/Pictures/wallpapers
alias wu="wu -i"
```
* Second, when you are browsing, and you see an image that you liked, you download it, use the script `wu image.ext`, it automatically updates wallpapers and moves to the directory with other wallpapers
```bash
# Browsing -> See Image -> Download Image -> Open Terminal
cd ~/Dowloads
wu image.ext
```
* As a result, you update wallpapers and get all wallpapers in one place automatically
## 📥 Installation 
Download binary from latest release and move it for example to /usr/local/bin
```bash
chmod +x wu
sudo mv -v wu /usr/local/bin
```
## 🔧 Installation from source
### 📋 Requirements
* 🛠️ make
* 🐍 python

🔢 If you want to get only binary to /usr/local/bin
```bash
cd /tmp
git clone https://github.com/kostya1F634/wu.git
cd wu
make
make copy
# or if you want custom directory
sudo mv -v wu /path/to/your/dir
```
🔗 Or you can create link to /usr/local/bin (not delete cloned repository)
```bash
cd ~/
git clone https://github.com/kostya1F634/wu.git
cd wu
make
make link
# or if you want custom directory
sudo ln -sv "$(pwd)/wu" /path/to/your/dir
```

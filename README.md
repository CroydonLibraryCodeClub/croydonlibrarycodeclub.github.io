# Croydon library code club website

## Repository for the web site

Add HTML and other files to show up on the https://croydonlibrarycodeclub.github.io website.

## Library laptop notes

Laptop info:
```
Lenovo ideapad 310-15ABR
Carrizo [1002:9874] (rev ca)
```

Create a USB key with an MX linux ISO on it, I used [MX-21_x64](https://mxlinux.org/download-links/) and [Rufus](https://rufus.ie/) on Windows or the built in USB creator on Linux.

Reboot the laptop and mash the F2 key with the Fn button held down to get into the BIOS.

Change the boot order to boot from USB.

Now run the installer. If it fails with `failed to create partition` then run GParted and create a new partition table of type `gpt` and reboot. The admin password for the Live USB is `demo`

Choose 105 Intl keyboard + English UK keyboard with no variant.

For partitioning choose entire hard drive and default options for partitions and ESP.

For computer name I used `cc01` to `cc10`.

For domain leave the default `example.dom`

Untick SAMBA.

Locale: `en_GB.UTF-8`

Tick System clock uses LOCAL

Timezone: `Europe/London`

Default user login: `codeclubadmin`
Deafult user password and admin password (check email)

Reboot and remove USB.

MX welcome: tick don't show at start up.

Connect to network.

Click package icon to do full upgrade.

Install [Scratch3](https://github.com/redshaderobotics/scratch3.0-linux/releases) via GDebi.

Note: sonic-pi through synaptic doesn't work

## Create a user account

Use `MX Tools` user manager to create a codeclub account with the password of `codeclub`. Make sure it doesn't have the sudo group. And tick the autologin box.

## Scanner setup

Download the driver [here](https://www.canon.co.uk/support/consumer_products/products/scanners/lide_series/canoscan-lide-300.html) and install.

# Setting up git

Generate a key for the machine:
```
ssh-keygen -t rsa -b 4096 -C "cc01@powered-up-games.com"
```

Setting up port forwarding for git over public WIFI:
```
nano ~/.ssh/config

Host github.com
  Hostname ssh.github.com
  Port 443
```

Cloning StudentFiles in the home directory, enter:
```
git clone git://github.com/CroydonLibraryCodeClub/StudentFiles.git
git clone git://github.com/CroydonLibraryCodeClub/croydonlibrarycodeclub.github.io.git
```

Reconfigure the remote to use ssh with the following commands (you must be in each directory):
```
git remote set-url origin git@github.com:CroydonLibraryCodeClub/StudentFiles.git
git remote set-url origin git@github.com:CroydonLibraryCodeClub/croydonlibrarycodeclub.github.io.git
```


Adding your SSH key to the ssh-agent:
```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```
Copy the public key `~/.ssh/id_rsa.pub` to GitHub.

Setting the git user name and email:
```
git config --global user.email "cc01@powered-up-games.com"
git config --global user.name "cc01"
```

# Fix annoying keyring popup

This menu usually pops up multiple times when trying to use Google Chrome.

Open the `Passwords and Keys` program, right click to open the context menu for the `Login` entry, and set the password to blank.


# Installing Visual Studio Code

Install from [this](https://go.microsoft.com/fwlink/?LinkID=760868) link.

# Installing Unity

Use [this](https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage?_ga=2.111589954.731056823.1573857184-1379241474.1573857184) link to install the hub and then install 2018.4 LTS

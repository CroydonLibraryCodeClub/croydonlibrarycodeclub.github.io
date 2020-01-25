# Croydon library code club website

## Repository for the web site

Add HTML and other files to show up on the https://croydonlibrarycodeclub.github.io website.

## Library laptop notes

Laptop info:
```
Lenovo ideapad 310-15ABR
Carrizo [1002:9874] (rev ca)
```

Create a USB key with an MX linux ISO on it, I used [MX-18.2_x64](https://mxlinux.org/download-links/) and [Rufus](https://rufus.ie/).

Reboot the laptop and mash the F2 key with the Fn button held down to get into the BIOS.

Change the boot order to boot from USB.

When the launcher comes up, select the default option, but press the `e` key to edit the boot options. Add `nomodeset` onto the end of the linux boot line. This prevents a problem with the windows not repainting correctly on the desktop during installation.

Now run the installer. If it fails with `failed to create partition` then run the command:
```
sudo apt update && sudo apt install mx-installer
```

Choose 105 Intl keyboard + English UK keyboard with no variant.

For partitioning choose entire hard drive and default options for partitions and GRUB.

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

Login to wifi.

Click package icon to do full upgrade.

Install sonic-pi through synaptic.

Install qjackctl.

## Downgrade kernel

The latest kernel (4.19) doesn't appear to work well with the wifi driver. To downgrade, open the `MX Package Installer` and install kernel `4.14` then open the `MX Tools` and set the machine to boot to 4.14.

## Create a user account

Use `MX Tools` user manager to create a codeclub account with the password of `codeclub`. Make sure it doesn't have to sudo group.

Edit the file `/etc/lightdm/lightdm.conf` and set the autologin to `codeclub`

## Remove annoying beep

In a terminal open `alsamixer` and mute beep channel.

## Possibly not needed with Kernel 4.14... test with next upgrade

Uncomment stretch backports in `/etc/apt/sources.list.d/debian.list`

Force package for Gnome network manager to the latest.

Apply

Re-comment the stretch line.

## Scanner setup

Download the driver [here](https://www.canon.co.uk/support/consumer_products/products/scanners/lide_series/canoscan-lide-300.html) and install.

# Setting up git

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

Reconfigure the remote to use ssh with the command:
```
git remote set-url origin git@github.com:CroydonLibraryCodeClub/StudentFiles.git
git remote set-url origin git@github.com:CroydonLibraryCodeClub/croydonlibrarycodeclub.github.io.git
```

Generate a key for the machine:
```
ssh-keygen -t rsa -b 4096 -C "croydoncodeclub@powered-up-games.com"
```

Adding your SSH key to the ssh-agent:
```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```
Copy the public key `~/.ssh/id_rsa.pub` to GitHub.

Setting the git user name and email:
```
git config --global user.email "croydoncodeclub@powered-up-games.com"
git config --global user.name "cc01"
```
# Fixing sonic-pi
Sonic Pi should now work with the stock installs, but you need to run qjackctl first.

# Fix annoying keyring popup

This menu usually pops up multiple times when trying to use Google Chrome.

Open the `Passwords and Keys` program, right click to open the context menu for the `Login` entry, and set the password to blank.


# Installing Visual Studio Code

Install from [this](https://go.microsoft.com/fwlink/?LinkID=760868) link.

# Installing Unity

Use [this](https://public-cdn.cloud.unity3d.com/hub/prod/UnityHub.AppImage?_ga=2.111589954.731056823.1573857184-1379241474.1573857184) link to install the hub and then install 2018.4 LTS

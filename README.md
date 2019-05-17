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

Now run the installer.

Choose English UK keyboard with extended Windows keys.

For partitioning choose entire hard drive and default options for partitions and GRUB.

For computer name I used `cc01` to `cc10`.

For domain: `codeclub`

Untick SAMBA.

Locale: `en_GB.UTF-8`

Tick System clock uses LOCAL

Timezone: `Europe/London`

Default user login: `codeclub`
Deafult user password: `codeclub`

Admin password (check email)

Tick autologin

Reboot and remove USB.

MX welcome: tick don't show at start up.

Login to wifi.

Click package icon to do full upgrade.

Install sonic-pi through synaptic.






After a default Manjaro installation, the laptop will beep on boot, to prevent this, add a file `/etc/modprobe.d/nobeep.conf`:
```
blacklist pcspkr
```

Hibernate does not currently work, so to force a shutdown when the lid is closed, in file `/etc/systemd/logind.conf` add the line:
```
HandleLidSwitch=poweroff
```

# Setting up git

Cloning StudentFiles in the home directory, enter:
```
git clone git://github.com/CroydonLibraryCodeClub/StudentFiles.git
```

Reconfigure the remote to use ssh with the command:
```
git remote set-url origin git@github.com:CroydonLibraryCodeClub/StudentFiles.git
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
Sonic Pi should now work with the stock installs, but with the ideapad laptops you need to add a file to stop jack defaulting to realtime and loading the HDMI device. Copy the file `.jackdrc` in this repo to the `codeclub` home directory.

```
/usr/bin/jackd -r -d alsa -d hw:Generic,0
```
The `-r` option prevents jack from needing realtime permissions. `-d alsa` tells jack to select the alsa driver. The remaining options are sent to the alsa driver itself. `-d hw:Generic,0` selects the onboard audio rather than the HDMI output on the ideapad laptops.
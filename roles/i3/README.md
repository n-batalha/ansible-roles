# i3 role (alpha)

Currently a very opinionated Ansible role for i3 with many assumptions (see below).

## Features

* HiDPI setup
* Gnome Keychain integration

## TODO

### Split core setup and extras

To comply with roles design:

* not all screens are 220dpi.
* not all use the Gnome Keyring.

### `status_command process exited unexpectedly (exit 1)`

To be investigated.

### Suspend

Is it configured by the lock command?

https://faq.i3wm.org/question/239/how-do-i-suspendlockscreen-and-logout.1.html

## Issues

### Google Chrome and Gnome Keyring

Some users claim Gnome's Keyring works out of the box, but some applications need to be told to still use Gnome's Keyring (when not running gnome). E.g. `--password-store=<basic|gnome|kwallet>`.

## References

* https://www.reddit.com/r/i3wm/comments/863l1j/gnomekeyring_in_i3/
* https://wiki.archlinux.org/index.php/GNOME/Keyring#PAM_method
* https://wiki.archlinux.org/index.php/GNOME/Keyring#Using_the_keyring_outside_GNOME
* https://www.reddit.com/r/i3wm/comments/863l1j/gnomekeyring_in_i3/
* https://wiki.gnome.org/Projects/GnomeKeyring/Pam
* https://wiki.archlinux.org/index.php/GNOME/Keyring#With_a_display_manager
* https://ubuntuforums.org/showthread.php?t=2377036

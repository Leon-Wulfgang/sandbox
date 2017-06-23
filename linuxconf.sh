#!/usr/bin/env bash

#VAGRANT#
vagrant version
vagrant init ubuntu/trusty64 # create Vagrantfile for some box
vagrant up # download and setup box according to Vagrantfile
vagrant status # running/stopped/suspended(saved)
vagrant suspend
vagrant up # start/restart box
vagrant ssh # connect and login to box
vagrant halt # save and shut down - vs vagrant up
vagrant destroy # format and forget box, used up will restore to baseline


#LINUX#
# d=dir | -=file
# trusty = code name for ubuntu version
# root user dir = /root/
# user home dir = /home/<user>
# /etc= conf files
# /var= variable files, that grow in time, eg. system,log,app
#   /bin= executable binary, by all users, eg. ls
#   /sbin= only for root user, sys admin
#   /lib= support binary
#   /usr= user programs, not required at boot up
echo $PATH # separated by :
# no remote root
sudo # run as root
# no su = least privilege
# https://packages.ubuntu.com/ = package search for apt-get
# /etc/apt/sources.list = package list
sudo apt-get update # update packages source list
sudo apt-get upgrade # upgrade software
sudo apt-get autoremove # auto remove no use apps
sudo apt-get install finger # install app
finger [<user>] # info about logged in user
cat /etc/passwd # username:encryptedPasswordX:userId:GroupId:description:homeDir:defaultShell = vagrant:x:1000:1000::/home/vagrant:bin/bash
sudo adduser student # add user <username>
sudo cat /etc/sudoers # see sudo user conf
sudo ls /etc/sudoers.d # list addtional sudoers for ubuntu
sudo cp /etc/sudoers.d/vagrant /etc/sudoers.d/student # copy vagrant sudo conf as student's
sudo nano /etc/sudoers.d/student # linux editor, easy, edit student sudo conf
# control + o # nano cmd overwrite
man passwd # manual passwd app
sudo passwd -e student # force expire student's password
ssh student@127.0.0.1 -p 2222 # ssh into localhost forwarded port 2222 to vmbox 22
ssh-keygen # key filename, phrase, generates 2 files, default dir /home/user/.ssh/ , pub-key(put in server) and pri-key(client)
# /home/<user>/.ssh # dir for public key
touch .ssh/authorized_keys # create a file in .ssh hidden folder
chmod 700 .ssh #
chmod 644 .ssh/authorized_keys #
ssh student@127.0.0.1 -p 2222 -i ~/.ssh/linuxconf # login using ssh key
sudo nano /etc/ssh/sshd_config # edit ssh conf, eg. disable passwd login : PasswordAuthentication no
sudo service ssh restart # restart ssh service for new conf
ls -al # d|rwx|rw-|r-- = dir|(owner)read,write,exec|(group)read,write,-|(all)read,-,-
       # permissions ? owner group ? month day time path
       # r=4 w=2 x=1
sudo chgrp root .bash_history # change file group to root
sudo chown root .bash_history # change file owner to root
# default port http=80, https=443, ssh=22, ftp=21, pop3=110, smtp=25
sudo ufw status # status of ubuntu firewall app
sudo ufw default deny incoming # set default rule of ufw to deny all incoming request
sudo ufw default allow outgoing # set default rule of ufw to allow outgoing request
sudo ufw allow ssh # set ssh to allow for remote admin
sudo ufw allow 2222/tcp # set 2222 (forwarded for 22 ssh) and tcp, for vm
sudo ufw allow www # allow http
sudo ufw enable # enable firewall, if ssh not allowed, remote access will be dead


# some tutorial
# https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04
# https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04
# https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-and-file-storage-with-peps-on-ubuntu-14-04
# https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-with-mail-in-a-box-on-ubuntu-14-04
# https://www.digitalocean.com/community/tutorials/how-to-install-the-lita-chat-bot-for-irc-on-ubuntu-14-04
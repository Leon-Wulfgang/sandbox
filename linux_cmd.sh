#!/usr/bin/env bash
psql forum

#HEROKU#
heroku config:set MYKEY=myvalue # set env vars for container
heroku pg:psql # start a pg console
heroku restart # manually restart container
heroku run bash # start a bash, new container instance each time ran
"source" # application
"dyno" # machine
heroku logs --dyno api # logs for 'api' dyno
heroku logs --source app # logs for 'app' source
heroku logs --tail --source app --dyno api # tail log, for set source 'app', set dyno 'api'
heroku log -n 10 # print 10 lines of log
heroku log # output logs of the application
heroku addons:create heroku-postgresql # add heroku pg addon to application, enables pg db
heroku run # run a command in the application
git push heroku HEAD:master # push changes to heroku remote, master head
heroku open # open application in default browser
heroku create # new application, after creation, git remote -v lists both git and heroku
heroku login # user/pass


#GIT#
git remote -v # add/set remote
git branche -all # show all branch
git pull  # pull commits from remote
git push  # push commits to remote
git commit # commit staging to repo, creates a commit
git add # add file to be commmited to staging
git init # initialize a new repo
git status # current changes made, branch status
git diff --staged # diff staged with head
git diff id0 id1 # diff commit id 0 and 1
git log # print commits
git checkout -b pg origin/pg  # checkout branch pg from remote:origin/pg
git checkout master # checkout master branch
git clone https://github.com/haowu0802/sandbox.git # clone repository to local


#SHELL#
ls -al # list all files including hidden ones - long version
pwd # current dir
cd ~ # cd to home
export AWS_KEY="MYKEY" # set env var
printevn # print environment variables
glob # file grabber
mkdir # make directory
# rm -r # remove dir and files recursively
cp /from /to # copy from arg1 to arg2
mv /from /to # move from arg1 to arg2
cd .. # one level up
# rm -rf /  # remove all files and folders recursively with force flag
date #print date and time
expr 2 + 2  # calculate 2+2 print 4
echo You Rock # print You Rock
uname # print OS name
hostname  # print host machine's name
host google.com # googles ip address
bash --version  # bash version and copyright
histroy # list of cmd history

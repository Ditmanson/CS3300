# A repository must exist on github
- go to your git hub
- create a repository
- Do not add a readme file if you are initializing from a local directory
> the reason you don't do that is because it might cause merge conflicts you have to deal with
- Once the repository is created github will provide you directions to initilize it.
# From your local directory
- git init
> -b will allow you to initalize with a different branch name other than Main
- git commit -m "first commit"
- git branch -M main
> The -M or -m branch is just so you can rename it
- git remote add origin https://github.com/Ditmanson/test.git
> git remote other options include rename, remove, set-head, set-branches, set-url, get-url, prune
- git push -u origin main
> -u is shorthand for --set-ustream you can also add a -f or --force if github gives you a warning

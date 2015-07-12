# setup &c

this script depends on having a tree structure like so

    reponame
    ../trees/reponame

that is, it requires a `trees` directory that contains initialized git repos

in future it will probably just create these repos itself,

and maybe use a hidden .trees folder for them... hm.

Also, this script must be run from within your repo.

It is intended to be used immediately before committing to check your changes

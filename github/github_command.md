#  GitHub command



![Git flow](https://github.com/harrynguyen1993/note/blob/main/github/GitFlow.PNG) 
   

## Creat file ignore
    ```
    >>> git init
    >>> touch .gitignore 
    >>> git add add origin  "Remote_repo path  https://github.com/harrynguyen1993/note.git"  
    >>> ..........
    ```
## Git tag
    ```
    >>> git tag -a [tag_name[] -m ["First tag"
    >>> git tap   < Show list tag >
    >>> git show [tag_name]  < Show a tag >
    >>> git tag -l ["partal_tag name *"]  < Search a tag >
    >>> git log --pretty=oneline   < show log all push head>
    >>> git tag -a [tag_name] [id_head]  < create new tag from an id of head >

    ### Push tag to remote repo

    >>> git push origin [tag_name]  < push tag to remote repo>
    >>> git push origin --tags  < push all tag to remote repo>
    

    ### Checkout from a tag to remote repo

    >>> git checkout -b [develop_branch] [tap_name]


    ### Delete a tag to remote repo
    >>> git tag -d [tap_name]
    >>> git push origin --delete [tag_name]
    ```
  

  ## Git alias --> faster command

    '''
    >>> git config --global alias.co checkout
    >>> git config --global alias.cm commit
    >>> git config --global alias.br branch
    >>> git config --global alias.st status
    >>> git config --global alias.rb rebase
    >>> git config --global alias.a add
    >>> git congif --global alias.resets 'reset HEAD--'
    >>> git congif --global alias.last 'log -1 HEAD'
    '''


## Git branch 

    '''
    >>> git log --oneline --decorate  <Show log >
    >>> git config --global merge.tool [diffmerge]  <Tool to merge>
    >>> git merge [branch need to merge ]
    >>> https://sourcegear.com/diffmerge/  [Tool check conflict]
    >>> git mergetool  <Show tool to merge>
    >>> git branch
    >>> git branch -v
    >>> git branch -merged  [check lists branch is merged to current branch]
    >>>
    '''
## Git rebase 
    '''
    >>> git rebase --onto master server client

    '''


## git server local :   https://bonobogitserver.com/

## git stash 
    ```
    >>> git stash 
    >>> git stash apply -index
    >>> git stash save 
    >>> git stash list
    >>> git stash appy   [stash]
    >>>>> -  Remove
    >>> git stash  drop [stash]
    >>> git stash pop
    >>> git stash -all
    >>> git clean -f -d
 

    ```


# reverse merge or rebase
    ```

    >>> git merge --abort
    >>> git rebase --abort
    >>> git diff ... ....
    >>> git revert HEAD
    >>> git reset --hard Head
    ```


# Collect to one line
    - git rebase -i HEAD~~
    - Change pick to squash
    - Update title  
    - git rebase -i HEAD~3
    - git push -f origin feature_top_page
    - change to r update message

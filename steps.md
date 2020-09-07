## Installing asdf


## Commitizen
Dependencies -
* NodeJS

### Installing NodeJS
GitHub Project - https://github.com/asdf-vm/asdf-nodejs

* Install requirements
```bash
brew install coreutils gpg
```
* Import the Node.js release team's OpenPGP keys to main keyring
```bash
zsh -c '${ASDF_DATA_DIR:=$HOME/.asdf}/plugins/nodejs/bin/import-release-team-keyring'
```
* Install NodeJS
```bash
asdf install nodejs latest
```
* Set current version
```bash
asdf list nodejs    # check nodejs version; 14.9.0 here
asdf local nodejs 14.9.0    # set current version to use
asdf current nodejs     # sanity check
```

### Installing Commitizen
```bash
npm install -g commitizen
npm install -g cz-conventional-changelog
echo '{ "path": "cz-conventional-changelog" }' > ~/.czrc
```
To use, run `git-cz` instead of `git commit`-
```bash
git-cz
cz
git cz
```
Either of the 3 works

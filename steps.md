## Installing asdf


## Commitizen
Dependencies -
* NodeJS
* Yarn

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

### Installing Yarn
* Install Yarn
```bash
asdf plugin add yarn
asdf install yarn latest
```
* Set current version
```bash
asdf list yarn    # check yarn version; 1.22.5 here
asdf local yarn 1.22.5    # set current version to use
asdf current yarn     # sanity check
```

### Installing Commitizen
```bash
yarn global add commitizen
yarn install
```
To use, run the following -
```bash
git-cz
```
In case, the binary `git-cz` is not found, then find the yarn binary path
```
yarn global bin
```
Try again by prefixing the output of previous step -
```bash
/Users/adimyth/.asdf/installs/nodejs/14.9.0/.npm/bin/git-cz
```

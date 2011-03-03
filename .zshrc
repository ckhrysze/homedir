# Path to your oh-my-zsh configuration.
export ZSH=$HOME/.oh-my-zsh

# Set to the name theme to load.
# Look in ~/.oh-my-zsh/themes/
export ZSH_THEME="ckhrysze"

# Set to this to use case-sensitive completion
# export CASE_SENSITIVE="true"

# Comment this out to disable weekly auto-update checks
# export DISABLE_AUTO_UPDATE="true"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Example format: plugins=(rails git textmate ruby lighthouse)
plugins=(git)

source $ZSH/oh-my-zsh.sh

# give me back ctrl arrow key navigation
bindkey ";5C" forward-word
bindkey ";5D" backward-word
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

# unset to have rvm prompt info working correctly
# http://rvm.beginrescueend.com/integration/zsh/
# Also, this needs to be after oh my zsh and before rvm
unsetopt auto_name_dirs

if [[ -s /home/hildebrandc/.rvm/scripts/rvm ]] ; then source /home/hildebrandc/.rvm/scripts/rvm ; fi

# Customize to your needs...
export PATH=/home/hildebrandc/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/var/lib/gems/1.8/gems/heroku-1.6.5/bin:/home/hildebrandc/mp/bin

source .private

# Q, the fast loading option
export EDITOR="emacs -Q"

# uses package source-highlight
# taken from http://linux-tips.org/article/78/syntax-highlighting-in-less
export LESSOPEN="| /usr/share/source-highlight/src-hilite-lesspipe.sh %s"
export LESS=' -R '


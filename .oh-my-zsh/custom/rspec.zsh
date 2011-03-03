# completion
autoload -U compinit
compinit

# autocompletion for ruby_spec
# works with spm/spv/spc aliases
# see also ~/bin/ruby_spec.rb
_ruby_specs() {
  if [[ -n $words[2] ]]; then
    compadd `ruby_spec -l ${words[2]}`
  fi
}
compdef _ruby_specs ruby_spec
alias spm="ruby_spec models"
alias spv="ruby_spec views"
alias spc="ruby_spec controllers"
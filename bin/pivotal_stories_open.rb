#!/usr/bin/env ruby
require 'rubygems'
require 'activeresource'

PROJECT_ID = 57095
TOKEN = "9f28c2c4b0d4738acaec0146e752ce9f"
USER = "CIH"

def promptForStory(stories)
  stories.each_with_index do |s, i|
    puts "#{i}. #{s.name}"
  end
  print "# ?>"
  input = $stdin.gets.chomp.strip
  stories[input.to_i]
end

class Story < ActiveResource::Base
  self.site = "https://www.pivotaltracker.com/services/v3/projects/#{PROJECT_ID}/"
  headers['X-TrackerToken'] = TOKEN
end

# Find stories
stories = Story.find(:all, :params => {:filter => "state:started owner:#{USER}", :project_id => PROJECT_ID})

if stories.size == 0
  puts "Found no open stories"
  exit()
end


story = stories.first
if stories.size > 1
  story = promptForStory(stories)
  puts "Using story, '#{story.name}'"
else
  puts "Only found one story, so using '#{story.name}'"
end

commit_message_file = File.join(ENV["HOME"], '.git-commit-template')
File.open(commit_message_file, 'w') do |file|
  file.puts("#{story.name}\n[##{story.id}]")
end
system("git config --global commit.template '#{commit_message_file}'")

#!/usr/bin/env ruby

time=Time.now

def L(b,i)
  l=0
  return l if (l=Math.sqrt(i-2*b))==l.floor
  return l if (l=Math.sqrt(i+2*b))==l.floor
  return -1
end

t,b,i,d,l=[],0,1,-5,0
t << l unless (l=L(b+=2,i+=(d+=10)))==-1 until t.length==6

puts "#{Time.now-time} sec."
puts t.inspect

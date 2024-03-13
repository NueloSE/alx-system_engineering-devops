#!/usr/bin/env ruby
sender = ARGV[0][/from:(\w+|[+]?\d+)/,1]
reciever = ARGV[0][/to:(\w+|[+]?\d+)/,1]
flags = ARGV[0][/[-+]\d:\d:-\d:[+-]?\d:-\d/]
puts "#{sender},#{reciever},#{flags}"

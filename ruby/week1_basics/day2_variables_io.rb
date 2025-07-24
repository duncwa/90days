print "Enter your name: "
name = gets().chomp.to_s
print "What is your favorite number: "
number = gets().chomp.to_i
print "What is your favorite programming language: "
language = gets().chomp.to_s
puts "Hello #{name}, your favorite number is #{number} and your favorite language is #{language}."
puts "Did you know that #{number} * 2 = #{number * 2}?"
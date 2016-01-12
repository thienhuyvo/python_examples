filename = "test.txt"

file_handle = open(filename, 'r+')
print "Do you want to truncate your %r file?" % filename
response = raw_input("> ")

if response == 'Y' :
	print "First we will show your current body in your file:"
	print file_handle.read()
	print "Truncating your file..."
	file_handle.truncate()

print "Now we're going to ask you for 3 lines:"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "We're going to write these to the file"
file_handle.write("\n")
file_handle.write(line1)
file_handle.write("\n")
file_handle.write(line2)
file_handle.write("\n")
file_handle.write(line3)
file_handle.write("\n")

print "This is your new file:"
print file_handle.read()
file_handle.close()

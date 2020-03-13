# The purpose of INIT will update and define our config files.
# You will need to pass in the API key, which will update conf.json, and all other files.

# After all you will want to do is to ensure elasticsearch is running, then turn on logstash with the correct conf files.
import sys

def main():
	args = sys.argv[1:]
	if len(args) == 0:
		print("Need to pass in an API key as an Argument")
		exit(1)
	print("API:", args[0])

if __name__ == "__main__":
	main()

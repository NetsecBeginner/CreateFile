#!/usr/bin/env python
#NetsecBeginner - 8/01/17
#Create Files of Arbitrary Sizes

#Imports
import argparse

#Get File Size, Write File
def main():
	#Parse Arguments
        p = argparse.ArgumentParser()
        p.add_argument("file", type=str, help="Name of File")
	p.add_argument("size", type=int, help="Size of File")
        p.add_argument("-b", "--bytes", action="store_true", help='measure input in bytes')
        p.add_argument("-k", "--kilobytes", action="store_true", help="measure input in kilobytes")
        p.add_argument("-m", "--megabytes", action="store_true", help="measure input in megabytes")
        p.add_argument("-g", "--gigabytes", action="store_true", help="measure input in gigabytes")
	args = p.parse_args()

	#Interpret Input
	multiplier = 1

	if args.bytes:
		multiplier = args.size * 1
	elif args.kilobytes:
		multiplier = args.size * 1000
	elif args.megabytes:
		multiplier = args.size * 1000000
	elif args.gigabytes:
		multiplier = args.size * 1000000000

	#Write File
	f = open(args.file, "a")
	f.write("x" * multiplier)

#Call Main
main()

#!/usr/bin/env python
import pickle
boolean = raw_input("change any settings? Y/n: ")
if boolean != "n":
	act = raw_input("enter an action: ")
	if act == "challenge":
		ip = raw_input("enter computer ip adress: ")
		user = raw_input("enter a user on this computer: ")
		password = raw_input("enter this user's password: ")
		diff = raw_input("enter a challenge difficulty level: ")
		variables = [act, ip, user, password, diff]
		outfile = open("memory","w")
		pickle.dump(variables,outfile)
else:
	act = "challenge"
	ip = raw_input("enter computer ip adress: ")
	user = raw_input("enter a user on this computer: ")
	password = raw_input("enter this user's password: ")
	diff = raw_input("enter a challenge difficulty level: ")
	variables = [act, ip, user, password, diff]
	outfile = open("memory","w")
	pickle.dump(variables,outfile)

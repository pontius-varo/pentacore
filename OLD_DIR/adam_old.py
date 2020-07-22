import pentmas
import modules
import ac1

version = "0.02"

def start():
    pentmas.slow_txt("Welcome to Pentacore, ver.%s! The premier text-adventure game since 2020." % version)
    pentmas.slow_txt("Developed by Pontius Varo. ©Eltersoft. All rights reserved. ")
    pentmas.slow_txt("Loading.......")
    pentmas.slow_txt("[-----------------------------------------]")
    ac1.room1()

start()

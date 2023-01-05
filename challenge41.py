#!/usr/bin/env python3

def main():
    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
    cn = input("what is the name? ")
    cs = input("what are the  stats? ")

    print(marvelchars.get(cn).get(cs))

    print(cn, cs, "is:", marvelchars.get(cn).get(cs))


main()

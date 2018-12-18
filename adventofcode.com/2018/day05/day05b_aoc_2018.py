answers = []

original = raw_input()

for _ in "abcdefghijklmnopqrstuvwxyz" :
  previous = ""
  current = original.replace(_,"").replace(_.capitalize(),"")
  while previous != current :
    previous = current
    for reaction in [ "aA", "bB", "cC", "dD", "eE", "fF", "gG", "hH", "iI", "jJ", "kK", "lL", "mM", "nN", "oO", "pP", "qQ", "rR", "sS", "tT", "uU", "vV", "wW", "xX", "yY", "zZ",
                      "Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "Gg", "Hh", "Ii", "Jj", "Kk", "Ll", "Mm", "Nn", "Oo", "Pp", "Qq", "Rr", "Ss", "Tt", "Uu", "Vv", "Ww", "Xx", "Yy", "Zz"  ] : 
      current = current.replace( reaction , "" )
  answers.append( len(previous) )

print min(answers)
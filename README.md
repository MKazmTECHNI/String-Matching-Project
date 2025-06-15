# Resolving the name 

"Its just a Project", well, not for me. i tryhard in those (only 7 hours before the assigment date (or often after)).
So within these few hours thats what i managed. for from best, but I've seen worse

## Simple String Comparing

I use Levenshtein's Algorythm, to calculate distance between string and big list, and return the string from list thats closest to the original string. 

## To use it:

Just put the names you need into names.csv. The number next to names was required for a project, and isn't important, you can cut it out yourself pretty quickly and easily.

### IMPORTANT - `names.py` and `surnames.py` DO NOT have all names in the world. 

There might be some names that have been inserted correctly, but came out as completly diffrent ones. I tried my best to add as many names and surnames and insert it into files, but I've already found some examples that should've been there and wasn't. **If you find bigger/better list or bunch of names that aren't in, send them up or smth, and I'll update it**, pwetty please

### "why is it so... unfinished? (ugly)"

Cuz i wrote most of it on power of a hunch, depression, faith its gonna work, and cafeine. And after finishing the project on the name from input, i've found out that I was supposed to do it only for file it does it's function now. if you needed faster version, look for implementation in C or sum, I've tried my best alr?


## May be added

- In when comparing, if levenshtein distance is greated than `'min_dist'`, stop comparing with this name. Should make it slightly faster.

- If you insert "Anna Kowalski" it'll go through even tho its masculine surname. if you're that sensitive about that, be my guest, go over 6000 names and surnames, and add 1 if its a dude and 0 if its a girl, then modify code slightly to change the end, but I'm aint doing allat (it shouldn't really have an impact later either way)
 
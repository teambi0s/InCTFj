### May the force be with you

**Challenge File**: [force](Handout/force)  

To get the flag, you must pass the correct input to this binary.
You might have to use the force for this one.

#### Hint 1

Look carefully, maybe only a part of the input matters, and you don't need to worry about what all of it really does.

#### Hint 2

After taking the input, the program only loads the first character later on, never really doing anything with the other characters. Why not brute force it?

#### Hint 3

Need a easy way to brute-force? check out:
<https://wiki.bi0s.in/reversing/miscellaneous/brute_force_cracking/>

#### Difficulty : 4

#### Flag : inctfj{i_have_the_high_ground}

### Solution

The binary was made using slightly obfuscated code so as to force the player to use brute-force, although the program can take long inputs, only the first character is used and can be easily bruteforced.

```sh

for i in {a..z}; do echo $i | ./bin; done | grep -a "inctf"

```

The player can use brute-force, or solve the encryption within.


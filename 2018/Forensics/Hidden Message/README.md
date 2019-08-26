# Challenge Name - Hidden Message

## Challenge Description -
Detective John finds a image and also a suspicious python script in a victims system. He suspects that there is something hidden in it. Help detective john find the secret message.

## Difficulty - Medium

## How to solve

They will be provided with a python code which inputs a string and encodes it to base_64 and then encodes into hex.The encoded string will be given.
To get to the flag they need to decode it in the reverse process by first decoding it to hex and then to base_64. then you get the passphrase.
The message is hidden by steghide .To extract it the command is
``` $steghide extract -sf <file-name>```
Then it asks for a passphrase the pass which we got when we decoded the python code will be given. Then the files hidden are extracted.

## Flag

inctfj{50m3t1m35_53cr3t_m3ssag35_ar3_3mb3dd3d}

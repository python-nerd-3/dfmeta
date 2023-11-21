# DF Template Manipulation
### /join 44046
This is a repository for various different tools to read and write DF templates. 
## How does this work?
DiamondFire templates contain a tag that contains data about the template. This tag is called `codetemplatedata` and can be viewed simply with /i tag list. 

This data tag contains information like the creator of the template, the name of it, its "version" (probably an unused statistic), and most importantly its code.

The code is compressed using gzip (to compact it) and base64 (to make the bytes into plain text). You can simply decrypt the code with these 2 cyphers and you get
code data containing everything about the code.

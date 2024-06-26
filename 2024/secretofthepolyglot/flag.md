1. If you run `file` command against the .pdf file. you may notice that that file should be a png file so convert .pdf to .png using `mv` command in Linux.

2. inspecting that image you will get a piece of flag. Then use `binwalk` command to see if the image contain any compress files. so it does.

3. To get the other part of the flag,  run `binwalk -e <image.png>` to extract compressed data. And `cat` the ASCII file.

**picoCTF{f1u3n7_1n_pn9_&_pdf_7f9bccd1}**  

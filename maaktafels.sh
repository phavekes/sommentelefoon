#!/bin/bash
for ((x=1;x<=10;x++)); 
do 
   # your-unix-command-here
   for ((y=1;y<=10;y++));
   do
   	echo "$x keer $y"
   	gtts-cli -l nl "Hoeveel is $x keer $y?" -o "sound/som $x keer $y.mp3"
   	antwoord=`echo "$x * $y" | bc`
   	gtts-cli -l nl "$x keer $y is $antwoord" -o "sound/antwoord $x keer $y.mp3"
   done
done
gtts-cli -l nl "Welkom bij de sommentelefoon!" -o "sound/welkom.mp3"
gtts-cli -l nl "Geef het antwoord op de sommen door aan de draaischijf te draaien." -o "sound/uitlegdraaischijf.mp3"
gtts-cli -l nl "Dat is goed!" -o "sound/goed1.mp3"
gtts-cli -l nl "Goedzo!" -o "sound/goed2.mp3"
gtts-cli -l nl "Dat klopt!" -o "sound/goed3.mp3"
gtts-cli -l nl "Inderdaad!" -o "sound/goed4.mp3"
gtts-cli -l nl "Helaas, fout." -o "sound/fout1.mp3"
gtts-cli -l nl "Jammer, dat is niet goed." -o "sound/fout2.mp3"
gtts-cli -l nl "Nee, dat klopt niet." -o "sound/fout3.mp3"
gtts-cli -l nl "Dat is niet goed." -o "sound/fout4.mp3"

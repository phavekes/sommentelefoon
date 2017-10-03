#!/bin/bash
if ! which pip > /dev/null; then
   echo -e "pip not found! Install? (y/n) \c"
   read
   if "$REPLY" = "y"; then
      sudo apt-get install python-pip
   fi
fi
if ! which gtts-cli > /dev/null; then
   echo -e "gtts-cli not found! Install? (y/n) \c"
   read
   if "$REPLY" = "y"; then
      sudo pip install gTTS
   fi
fi


for ((x=1;x<=10;x++)); 
do 
   gtts-cli -l nl "$x" -o "sound/$x.mp3" 2>&1 >> /dev/null
   for ((y=1;y<=10;y++));
   do
   	echo "$x keer $y"
   	gtts-cli -l nl "Hoeveel is $x keer $y?" -o "sound/som $x keer $y.mp3" 2>&1 >> /dev/null
   	antwoord=`echo "$x * $y" | bc`
   	gtts-cli -l nl "$x keer $y is $antwoord" -o "sound/antwoord $x keer $y.mp3" 2>&1 >> /dev/null
   done
done
gtts-cli -l nl "Welkom bij de sommentelefoon!" -o "sound/welkom.mp3"
gtts-cli -l nl "Geef het antwoord op de sommen door aan de draaischijf te draaien." -o "sound/uitlegdraaischijf.mp3"
gtts-cli -l nl "Welke tafel wil je oefenen?." -o "sound/welketafel.mp3"
gtts-cli -l nl "Dat is goed!" -o "sound/goed1.mp3"
gtts-cli -l nl "Goedzo!" -o "sound/goed2.mp3"
gtts-cli -l nl "Dat klopt!" -o "sound/goed3.mp3"
gtts-cli -l nl "Inderdaad!" -o "sound/goed4.mp3"
gtts-cli -l nl "Helaas, fout." -o "sound/fout1.mp3"
gtts-cli -l nl "Jammer, dat is niet goed." -o "sound/fout2.mp3"
gtts-cli -l nl "Nee, dat klopt niet." -o "sound/fout3.mp3"
gtts-cli -l nl "Dat is niet goed." -o "sound/fout4.mp3"
gtts-cli -l nl "Dit is het einde van de opdracht, je kunt nu ophangen." -o "sound/einde.mp3"
gtts-cli -l nl "Oke, we gaan oefenen met de tafel van " -o "sound/gekozentafel.mp3"

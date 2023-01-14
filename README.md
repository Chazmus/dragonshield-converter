# Summary

Convert an exported CSV from Dragonshield card manager into a CSV that can be imported into an alternative card manager (Deckbox for now 
but potentially others in the future). 

Personally just using this until Dragonshield implement advanced card searching capabilities in your
inventory which is not currently possible.

# Instructions

Requires python to be installed.

Run 'python main.py' in this directory in your favourite terminal. Should pop up with a handy dandy GUI.

Select your 'all-folders.csv' which you export from Dragonshield card manager as the input csv.
Specify an output csv filename and hit "Convert". The resulting csv can be imported into Deckbox.

## Issues

I've found cards with 'transform' when exported from Dragonshield do not export the full name of the card as compared with how 
Deckbox defines them. 

For example: Dragonshield exports the card "Henrika Domnathi", however, in Deckbox this card is defined as "Henrika Domnathi // Henrika, Infernal Seer"
as such, it fails to import. Not much I can do about this without some more advanced online card lookup to append the missing transformed side text.
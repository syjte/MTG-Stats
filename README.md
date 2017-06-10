# MTG-Stats
A collection of codes for analysing MTG deck statistics

There are two chunks of code: The first chunk uses existing cEDH decks, and can be used to tweak those decks to check the effect on Ad Nauseams.

The commented out chunk is used for manual input of deck statistics. However, the input only takes in CMC up to 6, so you will need to add more input lines to cater for larger CMCs.

To use the ANsim2, the TappedOut list needs a specially configured custom categories:
  1) #X for cards that net X mana.
  2) #6 for ramp cards that don't net mana the turn you play them. (For future AI purposes)
  3) #Tutor for tutors to hand
  4) #Ttutors for tutors to top of library
  5) #Draw for anything that draws a card
  6) #Counter for anything that counters
  7) #Combo for combo pieces.
  7) #0 for anything else. Ad Nauseam falls in this category - this card needs to be in the deck for the simulation to work.
  
Copy the base tappedout url without any of the category filters and paste it in the code, then run everything and you can start the simulations.

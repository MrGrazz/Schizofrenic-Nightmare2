
define my = Character("My", color="#a4a4a4")

define thatguy = Character("thatoneguy", color="#640000")

define chainsmoke = Character("Chainsmoker", color="#1d5706")

define billy = Character("Billy", color="#006eff")

define spoon = Character("Spooner", color="#fffb00")

define yowaimo = Character("Go/jo", color="#6200ff")

define Elon = Character("Elon", color="#353535")

define He = Character("He", color="#1eff00")

define Breaking = Character("Breaking New", color="#ff0000")

define  Grazz= Character("Mr. Grazz",  color="#1eff00")


image my = "my.png"
image thatguy = "nosequiensea.png"
image chainsmoke = "Chainsmoker(pressure).png"
image billy = "Billy.jpeg"
image yowaimo = "yowaimo.png"
image Elon = "Elon.png"
image Spooner = "spoon.jpeg"
image He = "he.png"
image Breaking = "breaking.jpg"

#Use "at Transform(lo que sea) with moveinright" para mover a la derecha y "moveinleft", "moveintop", o "moveinbottom"
#Use "alpha=0.0" y "with vpunch" para voler transparente y "alpha=1.0" y "with dissolve" para reaparecer
#Use ""

label start:

    scene gaymer at Transform(size=(1920,1080))

    my"Well that was sure a fantasy... I am quite paranoid this time of the day"
    show my at Transform(zoom=10, yoffset=400, xalign=0.2)
    my"Time to raise an shine"
    my"I wonder what is on the new right now"
    show breaking at Transform(zoom=0.7 ,yoffset=50, xalign=0.8)
    Breaking"Now on the news we had caught something on live"
    Breaking"Leonardo Adria Lopez de la Puente has been caugh on camara failing the jump for the beef"
    Breaking"We will keep you updated in the situation so stay tune"
    my"Dang... he should had gone for the chicken"
    show thatguy at Transform(zoom=1.5, yoffset=200, xalign=0.8)with moveinright
    thatguy"{bt=1000}{sc=1000}{rotat}####{/rotat}{/sc}{/bt} what are you doing watching Tv we have things to do"




    return

import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "YES"]
no = ["N", "n", "no", "NO"]


#waarom werkt de terminal niet
required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#het verhaal en zet intro aan het eind van de code holy shit dat 
def intro():
  print ("Dit is het verhaal over Rayan en zijn toch naar Nederland "
  "in dit verthaal krijg jij als de speler de optie om Rayan zijn opties te kiezen "
  "Rayan komt uit Syrie en probeert nu zijn vaderland te vertrekken "
  "zodat hij een visum kan halen voor zijn familie "
  "dit is het verhaal van Rayan"
  "welke optie kies je: ")
  time.sleep(1)

  print("")

  print ("""  A. Neem jou familie mee
  B. Laat jou familie achter en ga met je vrienden op pad
  C. Ga alleen op pad""")
  
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_familie()
  elif choice in answer_B:
    print("\nJe bent net als Vin Diesel van Fast & Furious je zal eerder niet gaan dan jouw familie achterlaten "
    "\n\nYou failed try again ")
  elif choice in answer_C:
    print("\nJe ging alleen op pad alleen kwam je er snel achter dat je geen idee heb waar je naartoe moet, "
    "uiteindelijk ging je liften en werd je opgepakt, door een seriemoordenaar bad luck i guess"
    "\n\nYou died")
  else:
    print (required)
    

#als je voor familie koos bij de intro ook de enige optie 
def option_familie(): 
  print ("\nJe koos ervoor om jou familie mee te nemen nu moet je alleen nog het vervoer uitkiezen  "
  "welke optie kies je:")
  time.sleep(1)
  print ("""  A. ga met de boot
  B. ga met de auto 
  C. ga lopen en hoop dat je word opgepikt""")
  choice = input(">>> ")
  if choice in answer_A:
    option_boot()
  elif choice in answer_B:
    option_auto()
    
  elif choice in answer_C:
    print("\nJe hebt besloten om te lopen maar niemand wilt je oppikken met jou familie,"
    "je besluit om toch door te gaan maar uitendelijk begeef jij en je famile het,"
    "jullie vallen dood op de grond neer van water tekort."
    "\n\nYou Died!")
  else:
    print (required)
    option_familie()

#als je voor optie boot koos bij optie familie
def option_boot(): 
   print ("\nJullie besloten om met de boot te gaan maar nu moeten jullie nog beslissen met welke boot jullie gaan "
  "welke optie kies je: ")
   time.sleep(1)
   print ("""  A. Met de veerpond
  B. Het bootje van jouw vader
  C. Een roeiboot """)
   choice = input(">>> ")
   if choice in answer_A:
    option_veerpond()
   elif choice in answer_B:
    option_bootje()
    
   elif choice in answer_C:
    print("Jullie gaan met de roeiboot op pad, je komt er al snel achter dat Nederland iets verder ligt dan je had verwacht"
    "Jullie varen voor dagen maar uiteindelijk komen jullie om van de dorst"
    "\n\nYou died!")
   else:
    print (required)
    option_boot()

#als je voor optie bootje koos bij optie boot erg orgineel ik weet het
def option_bootje(): 
   print ("\nJullie besloten om met de boot van jouw vader te gaan en jullie beginnen de reis "
   "jullie komen onderweg een veerpond tegen waar veel mensen uit gevallen zijn, ga je ze helpen of niet? "
   "welke optie kies je: ")
   time.sleep(1)
   print ("""  A. help een paar mensen op je bootje
   B. negeer ze 
   C. probeer ze op de veerpond te krijgen """)
   choice = input(">>> ")
   if choice in answer_A:
    option_help()
   elif choice in answer_B:
    option_negeer()
    
   elif choice in answer_C:
    print("Je probeert zoveel mogelijk mensen op de veerpond te krijgen maar zodra je dicht bij de boot komt "
    "valt er een groep mensen op je bootje, ze proberen allemaal te profiteren van jouw bootje "
    "jij en je familie worden van jullie bootje afgeduwed en worden bedolven door nog een groep mensen "
    "jullie verdronken door al de mensen die op jullie vallen "
    "\n\nYou died")
   else:
    print (required)
    option_bootje()


#als je voor optie help koos bij bootje
def option_help(): 
   print ("\nJullie hebben en paar mensen op de boot geholpen al had je niet iedereen niet kunnen helpen "
   "je hebt teminste een jong koppel met een kind geholpen. "
   "jullie komen aan in Nederland en het koppel vraagt of ze naar Overijsel kunnen gaan omdat daar hun familie is "
   "welke optie kies je: ")
   time.sleep(1)
   print ("""  A. ja maar natuurlijk
   B. nee eerst moeten wij ons visum krijgen
   C. gooi ze overboord """)
   choice = input(">>> ")
   if choice in answer_A:
    option_JaNatuurlijk()
   elif choice in answer_B:
    option_NeeVisum()
    
   elif choice in answer_C:
    print("Je gooide het koppel overboord met het kind en je familie ziet je als een monster en besluiten "
    "om jou overboord te gooien alleen stoot je je hoofd tegen een rots en ben je in een klap dood "
    "\n\nYou did ask for it")
   else:
    print (required)
    option_help()

#als je voor optie JaNatruurlijk had gekozen bij help
def option_NeeVisum(): 
   print ("\nJe zegt dat we eerst ons visum moeten halen en dat we daarna pas gaan kijken wat we gaan doen "
   "jullie komen aan in Noord Holland en gaan meteen naar het asiel zodat jullie ergens kunnen wonen "
   "het koppel bedankt jullie voor jullie hulp en gaat zelf op pad, "
   "onderweg zie je een advertentie over dit opkomend bedrijf en je ze vragen aan mensen om in het bedrijf te inversteren "
   "welke optie kies je: ")
   time.sleep(1)
   print ("""  A. ga naar het asiel 
   B. inversteer je laaste beetje geld in het bedrijf  """)
   choice = input(">>> ")
   if choice in answer_A:
    option_NaarAsiel()
   elif choice in answer_B:
    option_inversteer()
    
   else:
    print (required)
    option_NeeVisum()

#als je voor optie zelf NaarAsiel had gekozen bij NeeVisum
def option_NaarAsiel(): 
   print ("\nJe kreeg een visum en mocht in Nederland wonen, je woont nu al 2 jaar in Nederland en je hebt ondertussen  "
   "een goeie baan gekregen en je woont nu in de zelfde buurt als de rest van jouw familie "
   "je stuurt elke maand wat geld naar de rest van jouw familie zodat zij ook kunnen overkomen "
   "hoe het er nu voor staat ben je erg gelukkig ")
   time.sleep(1)
   print ("""  A. kies optie A om te kijken welk einde je hebt gekregen  """)
   choice = input(">>> ")
   if choice in answer_A:
    option_Good()
    
   else:
    print (required)
    option_NaarAsiel()


#als je voor optie zelf NaarAsiel had gekozen bij NeeVisum
def option_inversteer(): 
   print ("\nJe vrouw was niet blij met jouw keuze en noemde je dommer dan de achterkant van een ezel "
   "maar aangezien je nu praktisch gratis onderdak heb vond je het niet zon heel slecht idee "
   "3 maanden later kreeg je weer wat te horen van dat bedrijf waar je in had geversteerd "
   "nu maar hopen dat het inversteren het waard was ")
   time.sleep(1)
   print ("""  A. kies optie A om te kijken welk einde je hebt gekregen  """)
   choice = input(">>> ")
   if choice in answer_A:
    option_Secret()
    
   else:
    print (required)
    option_inversteer()



#als je voor optie JaNatruurlijk had gekozen bij help
def option_JaNatuurlijk(): 
   print ("\nJe koos ervoor om naar Overijsel te gaan met jouw familie en het jonge koppel "
   "ze bedanken jullie voor voor de hulp en vragen of jullie bij hun willen komen wonen bij de rest van de familie "
   "welke optie kies je ")
   time.sleep(1)
   print ("""  A. ga bij hun komen wonen
   B. ga zelf een huis regelen  """)
   choice = input(">>> ")
   if choice in answer_A:
    option_KoppelWonen()
   elif choice in answer_B:
    option_ZelfRegelen()
    
   else:
    print (required)
    option_JaNatuurlijk()

#als je voor optie koppelwonen had gekozen bij JaNatuurlijk
def option_KoppelWonen():
  print("\nje besloot om bij het koppel in te trekken met jouw familie al was er niet al teveel ruimte in het huis "
  "het was wel gezellig en de familie vond het geen probleem omdat je ze had gered ")
  time.sleep(1)
  print(""" A. kies optie A om te kijken welk einde je hebt gehaald """)
  choice = input(">>> ")
  if choice in answer_A:
    option_Good()

  else:
    print (required)
    option_KoppelWonen


#als je voor optie zelf regelen had gekozen bij JaNatuurlijk
def option_ZelfRegelen(): 
   print ("\nJe koos ervoor om niet naar het koppel te luisteren en om naar Zuid holland te gaan, daar scheidde jullie van elkaar "
   "en ging het koppel zelf op pad naar Overijsel "
   "jij en jouw familie kregen een visum en mochten en Alkmaar wonen ")
   time.sleep(1)
   print ("""  A. kies optie A om te kijken welk einde je hebt gekregen  """)
   choice = input(">>> ")
   if choice in answer_A:
    option_Neutral()
    
   else:
    print (required)
    option_ZelfRegelen()



#als je voor optie negeer koos bij optie bootje
def option_negeer():
  print("\nJe koos ervoor om niemand te helpen en op dat moment dat je langs de boot vaarde "
  "begon iedereen met spullen te gooien waar jij en jouw familie onder bedolven werden "
  "kies optie om te kijken wat er gebeurt: ")
  time.sleep(1)
  print("""  A. vervolg op verhaal  """)
  choice = input(">>>")
  if choice in answer_A:
    print("\nJe overleefde het helaas niet en nu ben je dood "
    "\n\nMisschien moet je wat aardiger zijn voor de volgende keer ")

  else:
    print(required)
    option_negeer()

#als je voor optie niks koos bij optie veerpond
def option_veerpond():
  print("\nJullie kozen voor de veerpond en dce reis verliep goed totdat de boot begint met omkiepen "
  "er breekt paniek uit en jij moet nu de optie maken die jou het beste lijkt "
  "welke optie kies je")
  time.sleep(1)
  print("""  A. pak een van de reddings boten
  B. doe niks """)
  choice = input(">>>")
  if choice in answer_A:
    option_reddingsboten()
   
  elif choice in answer_B:
    option_niks()
    
  else:
    print(required)
    option_veerpond()


#als je voor optie niks koos bij optie veerpond
def option_niks():
  print("\nBijna ieredeen in de boot begint uit de boot te springen, "
  "er landen steeds meer mensen in het water met nog meer mensen er bovenop"
  "in alle chaos zijn meerdere mensen verdronken waardoor er meer ruimte is vrij gekomen op de boot"
  "jullie komen in Nederland aan maar nu moeten jullie nog een asiel zoeken maar naar welke provincie gaan jullie"
  "welke optie kies je: ")
  time.sleep(1)
  print("""  A. ga naar Noord Brabant
  B. ga naar Groningen
  C. ga naar Flevoland  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Brabant()
   
  elif choice in answer_B:
    print("Jullie komen aan in Groningen en jullie gaan even zitten bij een cafe "
    "terwijl jullie aan het uitrusten zijn komt er een aardbeving en een sterke ook "
    "jullie proberen het cafe te verlaten maar tevergeefs worden jullie bedolven door het puin "
    "\n\nYou died!")

  elif choice in answer_C:
    option_Flevoland()

  else:
    print(required)
    option_niks()


#als je voor optie reddingsboten koos bij optie veerpond
def option_reddingsboten():
  print("\nEr was complete chaos op de boot en jij koos ervoor om een van de reddingsboten te pakken "
  "je krijgt het voor elkaar om er een te pakken, je gaat onderweg naar Nederland je en uiteindelijk komen jullie aan in Nederland "
  "nu moeten jullie nog kijken naar welke provincie jullie gaan "
  "welke optie kies je: ")
  time.sleep(1)
  print("""  A. ga naar Noord Brabant
  B. ga naar Groningen
  C. ga naar Flevoland  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Brabant()
   
  elif choice in answer_B:
    print("Jullie komen aan in Groningen na de lange tocht met de boot maar de tocht was te lang en jullie komen om van de dorst "
    "\n\nYou died")

  elif choice in answer_C:
    option_Flevoland()

  else:
    print(required)
    option_reddingsboten()


#als je voor optie Brabant koos bij optie niks
def option_Brabant():
  print("\nJullie besloten om naar Brabant te gaan en komen aan in Breda en "
  " nu staan jullie voor een paar keuzes om wat jullie verder gaan doen "
  " welke optie kies je: ")
  time.sleep(1)
  print("""  A. ga naar het asiel van Breda
  B. ga bij een van jouw vrienden wonen 
  C. ga een huis huren  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Breda()
   
  elif choice in answer_B:
    option_BijVriendenWonen()

  elif choice in answer_C:
    print("Jullie besloten om een huis te huren maar jullie hadden geen rekening gehouden "
    "dat jullie een visum nodig hadden om in Nederland te wonen "
    "dus besloten jullie om bij een shady woonverhuurder te gaan wonen"
    "al hadden jullie het wel een paar weken uitgehouden uiteindelijk werden jullie veraden door de huisverhuurder "
    "omdat jullie geen geld meer hadden, zitten julie in de gevangenis "
    "\n\nYou Failed")

  else:
    print(required)
    option_Brabant()
  

#als je voor optie Breda heb gekozen bij optie Brabant
def option_Breda():
  print("jullie kozen ervoor om naar het asiel te gaan in Breda "
  "al moesten jullie wel een paar weken wachten jullie wonen nu eindelijk in Nederland "
  "Je hebt een baan gekregen en je verdient genoeg om voor je gezin te zorgen "
  "al is het niet veel jullie zijn teminste gelukkig" )
  time.sleep(1)
  print(""" A. kies voor optie A om te kijken welk einde je hebt gehaald  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Neutral()

  else:
    print(required)
    option_Breda()


#als je voor optie auto koos bij optie familie
def option_auto(): 
   print ("\nJullie besloten om met de auto te gaan en jullie komen in Nederland aan met niet veel gedoe "
   "maar naar welke provincie gaan jullie naar toe "
   "welke optie kies je: ")
   time.sleep(1)
   print("""  A. ga naar Noord Brabant
  B. ga naar Groningen
  C. ga naar Flevoland  """)
   choice = input(">>>")
   if choice in answer_A:
    option_Brabant()
   elif choice in answer_B:
    print("toen jullie in Groningen aankwamen en aan het tanken waren kwam er een vrachtwagen met volle snelheid op het tankstation af "
    "de remmen wilde niet werken van de chauffeur en botst volledige op het tankstation "
    "er was een gigantische explosie en helaas was jouw familie in de explosie en hadden jullie het helaas niet overleefd "
    "\n\nYou died!")

   elif choice in answer_C:
    option_Flevoland()

   else:
    print(required)
    option_auto()


#als je voor Flevoland koos bij auto of niks
def option_Flevoland():
  print("\nJullie besloten om naar Flevoland te gaan en komen aan in Lelystad en "
  " nu staan jullie voor een paar keuzes om wat jullie verder gaan doen "
  " welke optie kies je: ")
  time.sleep(1)
  print("""  A. ga in Almere wonen
  B. ga naar een  andere povincie
  C. ga bij de rest van jouw familie wonen  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Almere()
   
  elif choice in answer_B:
    print("Jullie gingen kijken voor een andere provincie om in te wonen "
    "jullie proberen naar Den Helder te gaan maar onderweg daar naar toe komen jullie in een groot ongeluk "
    "\n\nYou died")
    
  elif choice in answer_C:
    option_BijFamilieWonen()
    
    
  else:
    print(required)
    option_Flevoland()


#als je voor optie Almere heb gekozen bij Flevoland
def option_Almere():
  print("jullie kozen ervoor om naar Almere te gaan "
  "jullie kregen een visum en sindsdien wonen jullie in Almere "
  "al heb je niet de beste baan, je krijgt wel een uitkering van de overheid "
  "jullie komen prima rond en zijn blij dat jullie niet meer in angst leven ")
  time.sleep(1)
  print(""" A. kies voor optie A om te kijken welk einde je hebt gehaald  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Neutral()

  else:
    print(required)
    option_Almere()

#als je voor optie BijVriendenWonen heb gekozen bij Brabant
def option_BijVriendenWonen():
  print("jullie kozen ervoor om bij wat vrienden te wonen nadat jullie je visum kregen "
  "jullie woonden daar voor een paar weken, maar op een dag stond er politie voor de deur "
  "jullie werden allemaal gearesteerd voor illegaal wonen, blijkbaar waren je vrienden  illegaal het land binnengekomen "
  "jullie worden terug gestured naar Syrie en zijn weer bij het begin ")
  time.sleep(1)
  print(""" A. kies voor optie A om te kijken welk einde je hebt gehaald  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Bad()

  else:
    print(required)
    option_BijVriendenWonen()
    

#als je voor optie BijFamilieWonen heb gekozen bij Flevoland
def option_BijFamilieWonen():
  print("jullie kozen ervoor om bij jullie familie te wonen "
  "al zijn jullie in een nieuw land met een andere omgeving je thuis zal atlijd bij jouw familie zijn "
  "je kreeg zelfs een goed betaalde baan door je neef "
  "de toekomst ziet er goed uit voor jouw familie ")
  time.sleep(1)
  print(""" A. kies voor optie A om te kijken welk einde je hebt gehaald  """)
  choice = input(">>>")
  if choice in answer_A:
    option_Good()

  else:
    print(required)
    option_BijFamilieWonen()


#als je voor optie BijVriendenWonen had gekozen krijg je dit einde 
def option_Bad():
  print("Erg jammer maar je hebt de Bad ending gehaald "
  "iedereen werd terugestuurd naar Syrie en je zou het hier kunnen opgeven of je kan het weer proberen "
  "ook al word je neergeslagen sta altijd weer op "
  "\n\nYou reached the Bad ending")

 
#als je voor optie BijFamilieWonen had gekozen krijg je dit einde 
def option_Good():
  print("Gefeliciteerd je heb de Good Ending gehaald de hele familie is weer bij elkaar "
  "en je hebt een leuke baan met een goed inkomen dit is een van de goeie eindes"
  "maar er is nog een einde die the Good ending overteft "
  "kijk maar of je hem kan krijgen "
  "\n\nYou reached the Good ending")


#als je voor optie Breda had gekozen krijg je dit einde 
def option_Neutral():
  print("Gefeliciteerd je hebt de Neutral ending gehaald "
  "al is het niet het beste eind dat je kan krijgen is het nog steeds wel beter dan de andere endings "
  "\n\nYou reached the Neutral ending ")


#als je voor optie inversteer had gekozen krijg je dit einde 
def option_Secret():
  print("Gefeliciteerd je hebt de Secret ending gehaald "
  "je hebt echt veel geluk, het bedrijf waar je inversteerde werd erg succesvol en heeft"
  "nu een marketwaarde van maar liefst 500 miljoen! jouw aandelen gingen natuurlijk ook omhoog zoveel dat je genoeg geld "
  "nu heb dat je je hele familie naar Nederland kan brengen en je houdt zelfs nog wat extra over "
  "je hebt alles wat je wilde je hele familie is overgekomen en je hebt genoeg geld om een villa te bouwen voor je hele familie "
  "\n\nYou reached the Secret ending")


intro()




  


  
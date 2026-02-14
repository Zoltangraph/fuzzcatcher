from processing import*
from random import*

def setup():
 size(500,500)
 
 global appleY
 appleY = 0
 
 global appleX
 appleX = 190
 
 global playerX, score
 playerX = 190
 score = 0
 
 
 
 global cippertsprite
 cippertsprite = loadImage("cippertsprite.png")
 
 global applesprite
 applesprite = loadImage("fuzzsprite.png")

def draw ():
  background (0,0,225)
  
  
  global appleY, appleX, playerX
  
  global cippertsprite
  image(cippertsprite,playerX,400,50,50)
  
  global applesprite
  image(applesprite,appleX,appleY,50,50)
  print(appleY)
  appleY = appleY + 5
  #appleY = 5
  
  if appleY > 500:
    appleY = 0
    appleX = randint (0,300)
    
  display()
  collision()
    
    
  if keyPressed:
    if key =="a":
     playerX -= 8
    if key == "d":
     playerX += 8
    
def display():
  global score
  

  
  
  fill(255,255,255)
  textSize(20)
  displayText = "Score: " + str(score)
  text(displayText,12,20)
  
def collision():
 global playerX, appleX, appleY, score
 playerY = 400
 
 if playerX -10 <= appleX <= playerX + 60 and playerY <= appleY <= playerY + 50: 
   print("chaught")
   score += 1
   appleY = 0
   appleX = randint (0,300)

  
  
run()
function rollDice(){
var dice = ["Roll1.jpg","Roll2.jpg","Roll3.jpg","Roll4.jpg","Roll5.jpg","Roll6.jpg"];
var roll = Math.ceil(Math.random() * dice.length);
roll--; // Javascript indexes start at 0 - the count is 6 items, so subtract 1 to get item in range 0-5
document.getElementById("diceImage").innerHTML="<img src='"+dice[roll]+"'>";
}
rollDice();


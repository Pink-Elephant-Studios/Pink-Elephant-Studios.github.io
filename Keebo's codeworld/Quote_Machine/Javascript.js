/*var randomNumber = Math.floor(Math.random()* 20);
quotes[5] */
var quotes = [
	"I was told to put a quote here, but I don't know any good quotes",
	"MY EYESSSSSSS",
	"CLATU! VERATA! NMPHMHHIAHGHU",
	"This here is my BOOMSTICK",
	"POKEMON! Gotta eat em' all!",
	"Contemplate this on the tree of WOE",
	"Conan! What is best in life?!?",
	"Fireball",
	"It's not just a boulder! It's a rock!!!",
	"Teacher!!! You forgot the homework!!!",
	"Teacher!!! Leave us kids alone!!!",
	"Pizza rat",
	"Find the cookie!"
]
function newQuote() {
	var randomNumber = Math.floor(Math.random() * (quotes.length));
	document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber]
}
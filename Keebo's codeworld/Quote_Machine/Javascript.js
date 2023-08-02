/*var randomNumber = Math.floor(Math.random()* 20);
quotes[5] */
var quotes = [
	"I was told to put a quote here, but I don't know any good quotes",
	"MY EYESSSSSSS",
	"CLATU! VERATA! NMPHMHHIAHGHU",
	"This here is my BOOMSTICK",
	"POKEMON! Gotta eat em' all!"
]
function newQuote() {
	var randomNumber = Math.floor(Math.random() * (quotes.length));
	document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber]
}
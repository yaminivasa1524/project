var pcart = document.querySelector('#pcart');
var ptotal =document.querySelector('#ptotal');

function addPizza(pid){
	pizzaId = '#piz' +pid ; 
	var name= document.querySelector(pizzaId).innerHTML;
	var radio ='pizza'+pid;
	var price = document.getElementsByName(radio).values;
	pcart.innerHTML += '<li>' +name + '</li>';

}
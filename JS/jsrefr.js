// var person1 = {

// 	favfood: "pancakes",
// 	favMovie: "Ironman"
// }

// var person2 = person1;  //person2 is reference to person 1
// //any changes in person2 will change data of person1.

// person2.favfood = "wafles";
// console.log(person1.favfood);

//--------------------------------------



//           THIS 

// var timon = {

// 	printdata: function(){
// 		console.log("Hello I am apple.");
// 		console.log(this === timon);    //this is called by timon object.
// 	}
// }

// timon.printdata();

// var einstein = function(){
// 		console.log(this === global);   //this is global function so nothing calls it
// }

// einstein()

// -------------
 //                    PROTOTYPE

// function User(){
// 	this.name = "";
// 	this.life = 100;
// 	this.giveLife = function giveLife(targetPlayer){
// 		targetPlayer.life += 1;
// 		console.log(this.name + "gave 1 life to " + targetPlayer.name);
// 	}
// }

// var Bucky = new User();
// var Wendy = new User();

// Bucky.name = "Bucky";
// Wendy.name = "Wendy";

// Bucky.giveLife(Wendy);
// console.log("Bucky" + Bucky.life);
// console.log("Wendy" + Wendy.life);

//-------------------------------------------------




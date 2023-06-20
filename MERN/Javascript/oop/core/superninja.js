class Ninja{
    constructor(name,health,speed=3,strength=3){
    this.name=name;
    this.heath=speed;
    this.strength= strength;
    }
sayName(){
    console.log (`My name is ${this.name}`);
}
showStats(){
    console.log(`My name is ${this.name} my strength is ${this.strength} my speed is ${this.speed} and my health ${this.health}`)
}
drinkSake(){
    this.health +=10;
    console.log(`${this.health} gained 10 this.heath`);
}
}
class Sensei extends Ninja{
    constructor (name, health=200,speed=10,strength=10,wisdom=10){
        super (name,health,speed,strength);
        this.wisdom=wisdom;
    }
    speakWisdom(){
        super.drinkSake()
        console.log (`bring the method drinksake`)
    }
}
// example output
const superSensei = new Sensei("Master Splinter");
superSensei.speakWisdom();
// -> "What one programmer can do in one month, two programmers can do in two months."
superSensei.showStats();
// -> "Name: Master Splinter, Health: 210, Speed: 10, Strength: 10"


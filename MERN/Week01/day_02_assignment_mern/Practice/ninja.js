class Ninja{
    constructor(name, health){

        this.name = name
        this.health = 100
        this.speed = 3;
        this.strenght = 3;
    }


    sayName(){

        console.log(`My ninja name is ${this.name}!`);
    }

    showStats(){
        console.log(`My ninja name is ${this.name} and ninja strenght is ${this.strenght} and ninja speed is ${this.speed} and ninja health is ${this.health}`);
    }

    drinkSake(){
        this.health = this.health + 10;
        console.log(`Drank sake and gained 10 health points! Health is now ${this.health}`);
    }

}
const ninja1 = new Ninja("Hyabusa");
const ninja2 = new Ninja("Raed");
const ninja3 = new Ninja("Yaya");

ninja1.sayName();
ninja1.showStats()
ninja1.drinkSake()
console.log(`-------------------------------------------------------------------------------`);
ninja2.sayName();
ninja2.showStats()
ninja2.drinkSake()
console.log(`-------------------------------------------------------------------------------`);
ninja3.sayName();
ninja3.showStats()
ninja3.drinkSake()
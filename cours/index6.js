





const newInv1= [
    {name: "Grain of Rice", quantity: 9000},
    {name: "Peanut Butter", quantity: 50},
    {name: "Royal Jelly", quantity: 20}
];

const currInv1= [
    {name: "Peanut Butter", quantity: 9000},
    {name: "Grain of Rice", quantity: 1}    
];
const expected1= [
    {name: "Peanut Butter", quantity: 70},
    {name: "Grain of Rice", quantity: 9001},
    {name: "Royal Jelly", quantity: 20}
];

 const newInv2 = [
     const currInv2=[{ name:"Peanut Butter", quantity:20}];
     const expected2=[{name:"Peanut Butter", quantity: 20}];

     const newInv3 = [{name:"Peanut Butter", quantity:20}];
     const currInv3 = [];
     const expected3 = [{name:"Peanut Butter", quantity:20}];   
 ];
function updateInventory(newInv, currInv){
    for (var i=0; i< newInv.length; i++){
        var ItemFound = false
        var newItem = newInv[i]


    
    for (var i=0; i< newInv.length; i++){
        var currItem = currInv[j];


        if (newItem.name === currItem.name){
            ItemFound = true
            currItem += newItem.quantity
            // no need to keep lopping
            break; 
        }    
    }
    if (ItemFound === falsse){
        currInv.push(newItem)
    }
}
return currInv
}
result = updateInventory(newInv1, currInv1);

for(var i=0; i< XPathResult.length; i++ ){
    var newItem = result[i]
    var expectedItem = expected1[i]
    console.log(newItem);
    console.log("-------------------------------------------------");
    console.log(expectedItem);
}  




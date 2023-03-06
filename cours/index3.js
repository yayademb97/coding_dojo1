/*
Acronyms
Create a function that, given a string, returns the string's acronym
(first letter of each word capitalized).

Do it with .split first if you need to, then try to do it without 
*/
const str1 = "object oriented programming";
const expected1 = ""
str1[0].toUpperCase() + str1.substring(1) + str1[8].toUpperCase() + str1.substring(1) + str1[17].toUpperCase() + str1.substring(1);
console.log()

    // The 4 pillars of OOP
    const str2 = "abstraction polymorphism inheritance encapsulation";
    const expected2 = "";

    const str3 = "software development life cycle";
    const expected3 = "";

    // // Bonus ignore extra spaces
    const str4 = "global information tracker";
    const expected4 = "";

    function acronym(str){
        var acronym = "";
        var wordsArr = str.split("");
        console.log("wordsArr");
    }
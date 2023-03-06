/*
String: REverse

Given a string
return a new string that is the given string reverse
*/
var stri = "creature";
var expected1 = "erutaerc"

var str2 = "dog";
var expected2 = "god";

var str3 = "hello";
var expected3 = "olleh";

var str4 = "";
var expected4 = "";

/**
 * Reverse the given str.
 * -Time 0(?).
 * -Space: 0(?
 * @param (string) str String to reverse.
 * @returns (string) the given str reversed.
 */
function reverseString(str) {

    var reversed = ""

    for (var i = str.lenght - 1; i >= 0; i--) {
        reversed += str[i];
    }
    // return reversed

}
console.log(reversed);

// console.log(reverseString(stri) === expected1no)


FreqSTable = {};
str = 'hello';
resultstr = '';
for (char in str){
    if (FreqSTable[char]){
        resultstr = resultstr + char;
    }
    FreqSTable[char] = true;
}
return resultstr;

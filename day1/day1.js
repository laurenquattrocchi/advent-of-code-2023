// part 1
const fs = require("fs");
const text = fs.readFileSync("./test.txt", "utf-8");
const splitText = text.split("\n")



var sum = 0
for (let i = 0; i < splitText.length; i++){
	var counter = ''
	for (let j = 0; j < splitText[i]; i++){ 
		if (!isNaN(parseInt(splitText[i][j]))){
		   // console.log(parseInt(lst[start]))
		   counter = counter + splitText[i][j]
		   break
		}
	}
	for (let k = splitText.length-1; k > -1; k--){ 
		if (!isNaN(parseInt(splitText[i][k]))){
		   // console.log(parseInt(lst[start]))
		   counter = counter + splitText[i][k]
		   break
		}
	}
	sum = sum + parseInt(counter)
	console.log(counter)
}

console.log(sum)


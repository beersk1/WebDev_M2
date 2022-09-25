// Setup
let stringCont = document.getElementById("str-var");
let intCont = document.getElementById("int-var");
let sumFuncAns = document.getElementById("sum-func-answer");
let if_elseAns = document.getElementById("if-else-header-answer");

// Variables
let stringVar = "Kabeer";
stringCont.innerHTML = stringVar;
let integerVar = 13;
intCont.innerHTML = integerVar;

// Sum function
let sumFunc = (num1, num2) => {
  return num1 + num2;
};

// Setting the output of the function to html content
sumFuncAns.innerHTML = sumFunc(6, 9);

// Decision making
let age = 50;
if (age >= 50) {
  if_elseAns.innerHTML = "Yes!";
} else {
  if_elseAns.innerHTML = "No!";
}

// Loop to print multiples of 3
for (let k = 1; k < 20; k++) {
  document.write(k * 11 + "<br>");
}

/*
Block Binding - let const var
  use const by default
  use let for variables going to change
  use var for global
*/

/* hoisting */
function getValue(condition) {
  if (condition) {
    var value = "blue";
    // other code
    return value;
  } else {
    // value exists here with a value of undefined
    return null;
  }
  // value exists here with a value of undefined
}// becomes
function getValue(condition) {
  var value;// hoisted
  if (condition) {
    value = "blue";
    // other code
    return value;
  } else {
    return null;// value==undefined
  }
}

/* block-level declarations */
/*let*/
function getValue(condition) {
  if (condition) {
    let value = "blue";
    // other code
    return value;
  } else {
    // value doesn't exist here
    return null;
  }
// value doesn't exist here
}

/*re-declare*/
var count = 30;
// throws an error
//let count = 40;
var count = 30;
if (1) {
// doesn't throw an error
//console.log(count)// count not declared here
let count = 40;
console.log(count)
// more code
}

/*const*/
// valid constant
const maxItems = 30;
// syntax error: missing initialization
//const name;
if (1) {
  const maxItems = 5;
  // more code
}
// maxItems isn't accessible here
var message = "Hello!";
let age = 25;
// each of these throws an error
//const message = "Goodbye!";
//const age = 30;
const maxItems0 = 5;
// throws an error
//maxItems = 6;

/*obj const*/
const person = {
  name: "Nicholas"
};
// works
person.name = "Greg";
// throws an error
//person = {name: "Greg"};
console.log(person.name)

/*temporal dead zone*/
if (1) {
  //console.log(typeof value); // throws an error
  let value = "blue";
}
console.log(typeof value); // "undefined"
if (1) {
  let value = "blue";
}

/*block binding in loops*/
for (var i = 0; i < 10; i++) {
  process(items[i]);
}
// i is still accessible here
console.log(i); // 10
for (let i = 0; i < 10; i++) {
  process(items[i]);
}
// i is not accessible here - throws an error
console.log(i);

/*functions in loops*/
var funcs = [];
for (var i = 0; i < 10; i++) {
  funcs.push(function() {
    console.log(i);
  });
}// i == 10
funcs.forEach(function(func) {
  func(); // outputs the number "10" ten times
});
//IIFEs
var funcs = [];
for (var i = 0; i < 10; i++) {
  funcs.push((function(value) {
    return function() {
      console.log(value);
    }
  }(i)));// immediately invoked function expressions (IIFEs)
}
funcs.forEach(function(func) {
  func(); // outputs 0, then 1, then 2, up to 9
});

/* let Declarations in Loops */
// for es6
var funcs = [];
for (let i = 0; i < 10; i++) {
  funcs.push(function() {
    console.log(i);
  });
}
funcs.forEach(function(func) {
  func(); // outputs 0, then 1, then 2, up to 9
})
// for in es6
var funcs = [],
    object = {
      a: true,
      b: true,
      c: true
    };
for (let key in object) {
  funcs.push(function() {
    console.log(key);
  });
}
funcs.forEach(function(func) {
  func(); // outputs "a", then "b", then "c"
});

/*
const Declarations in Loops
*/
/* const in loop init */
var funcs = [];
// throws an error after one iteration
for (const i = 0; i < 10; i++) {
  funcs.push(function() {
    console.log(i);
  });
}
/* const in for in */
var funcs = [],
    object = {
      a: true,
      b: true,
      c: true
    };
// doesn't cause an error
for (const key in object) {
  funcs.push(function() {
    console.log(key);
  });
}
funcs.forEach(function(func) {
  func(); // outputs "a", then "b", then "c"
});

/*
Global Block Bindings
*/
/* in a browser before es6 */
var RegExp = "Hello!";
console.log(window.RegExp); // "Hello!"
var ncz = "Hi!";
console.log(window.ncz); // "Hi!
/* es6 */
// in a browser
let RegExp = "Hello!";
console.log(RegExp); // "Hello!"
console.log(window.RegExp === RegExp); // false
const ncz = "Hi!";
console.log(ncz); // "Hi!"
console.log("ncz" in window); // false


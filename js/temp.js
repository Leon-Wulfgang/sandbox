
/*

var a = function(){}; // a.b=2
Object.prototype.a = 1;
Function.prototype.b = 2;
var c = new a(); // c.b=2
console.log(c.a); // undefined
console.log(a.b, c.b); // 2



function func(){
  console.log(a);
  function a() {};
  var a = 1;
}
func();



var num;
var obj;

x = function func() {
  console.log(this.num);
}
y = function(x){
  x();
  arguments[0]();
}

num = 10;
obj = {
  num: 5,
  run: y,
}

obj.run(x);


x = func()
function a(){};
function func(){
  console.log(a);
  function a() {};
  var a = 1;
}
func();

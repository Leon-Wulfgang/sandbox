/* exec must be in main package */
package main

/* imports must be used, unused won't compile */
import (
	"fmt"
	"os"
)

/* entry point must be main() */
func main(){
	var power int
	power = 100 // not allow unused var
	// power := 100 // shorthand
	name, power := "Go", getPower() // one var is new, can use :=
	if len(os.Args) != 2{
		os.Exit(1)
	}
	/* Args[0] is always the filename */
	fmt.Println(os.Args[0], "Go Args-2:", os.Args[1])
	fmt.Printf("%s Printf %d \n", name, power)

	/* multi return */
	value, exist := pow("goku")
	if exist == false {
		println(value)
	}
	/* _ is blank identifier, no type, can use again */
	_, exist = pow("goku")
	if exist {
		println(exist)
	}

	/* new instance */
	goku := Saiyan{
		Name: "Goku",
		Power: 150,
	}
	goku.Power = 151
	/* no need to assign */
	kugo := Saiyan{}
	kugo.Name = ""
	/* partial property */
	guko := Saiyan{Name:"guko"}
	guko.Power = 1
	/* as order */
	kogu := Saiyan{"kogu", 2}
	kogu.Power = 2

	/* do copy vs do ref */
	notSuper(goku) // copy
	println(goku.Power)
	super(&goku) // ref, "address of" operator
	println(goku.Power)

	/* struct func */
	goku.add90000()
	println(goku.Power)

	/* new */
	gogo := new(Saiyan)
	// same as
	ogog := &Saiyan{}
	gogo.Power, ogog.Power = 0, 0
	goku1 := new(Saiyan)
	goku1.Name = "goku"
	goku1.Power = 9001
	//vs
	goku2 := &Saiyan {
		Name: "goku",
		Power: 9000,
	}
	goku2.Power = 9000

	/* obj in obj */
	gohan := &Saiyan{
		Name: "Gohan",
		Power: 1000,
		Father: &Saiyan { // address of a new Saiyan or existing one
			Name: "Goku",
			Power: 9001,
			Father: nil, // nil is null
		},
	}
	gohan.Father.Name = "goku"
}

func getPower() int{
	return 200
}

/* string in, no return */
func log(message string){

}

/* 2 int in, int out */
// func add(a int, b int) int {
func add(a, b int) int { //shorthand
	return a + b
}

/* string in, int and bool out */
func pow(name string)(int, bool){
	return 1, true
}

/* no obj in go, use struct and composite */
type Saiyan struct {
	Name string
	Power int
	Father *Saiyan // pointer to another obj, any type can be field
}
/* Saiyan is the receiver of this func */
func (s *Saiyan) add90000(){
	s.Power += 90000
}

/* factory, return copy or ref */
func newSaiyanPointer(name string, power int) *Saiyan{
	return &Saiyan{
		Name: name,
		Power:power,
	}
}
func newSaiyanCopy(name string, power int) Saiyan{
	return Saiyan{
		Name: name,
		Power:power,
	}
}


/* do the copy */
func notSuper(s Saiyan){
	s.Power += 10000
}

/* do the reference */
func super(s *Saiyan){ // takes pointer
	s.Power += 10000
}

/* redirected the copy of the in pointer, doesn't change the previously pointed var */
func bad(s *Saiyan){
	s = &Saiyan{}
}

/* godoc when no internet
	godoc -http=:6060
	localhost:6060
*/

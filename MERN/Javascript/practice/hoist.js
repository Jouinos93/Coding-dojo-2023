console.log(hello);                                   
var hello = 'world';                                 
// world
// outut = undefined

var needle = 'haystack';
test();
function test(){
    var needle = 'magnet';
    console.log(needle);
}
// magnet
// output= magnet

var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);

// only okay
// super cool
// output= super cool

var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}

// undefined
// half-chicken

// output= chiken , half-chicken

// console.log(genre);
// var genre = "disco";
// rewind();
// function rewind() {
//     genre = "rock";
//     console.log(genre);
//     var genre = "r&b";
//     console.log(genre);
// }
// console.log(genre);

// // disco , rock, r&b , disco 
// output= disco is not defined

dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);

// san jose,seattle,burbank ,san jose
// output san jose
// seattle
// burbank
// san jose


// console.log(makeDojo("Chicago", 65));
// console.log(makeDojo("Berkeley", 0));
// function makeDojo(name, students){
//     const dojo = {};
//     dojo.name = name;
//     dojo.students = students;
//     if(dojo.students > 50){
//         dojo.hiring = true;
//     }
//     else if(dojo.students <= 0){
//         dojo = "closed for now";

//     return dojo;
// }


function makeDojo(name, students) {
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    
    if (dojo.students > 50) {
        dojo.hiring = true;
    } else if (dojo.students <= 0) {
        return "closed for now";
    }
    
    return dojo;
}

console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));








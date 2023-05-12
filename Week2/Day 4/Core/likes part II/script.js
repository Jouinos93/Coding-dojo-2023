var plus1=9;
var plus2=12;
var plus3=9;
var likes=document.querySelector("#title>h4")
console.log(likes)
var likes1=document.querySelector("#likes1")
var likes2=document.querySelector("#likes2")


function changelikes(){
    plus1++;
    likes.innerText=plus+" like(s)";
}

function changelikes1(){
    plus2++;
    likes1.innerText=plus1+" like(s)";
}

function changelikes2(){
    plus3++;
    likes2.innerText=plus2+" like(s)";
}
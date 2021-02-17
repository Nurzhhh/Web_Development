const input = document.querySelector("#inputField");
const  btn = document.querySelector("#addToDo");
const list = document.querySelector("#toDoContainer");
var el = document.getElementsByTagName('li');

btn.onclick = function(){
    var txt = input.value;
    if(txt ==''){
        alert('You must write something');
    }
    else{
        li = document.createElement('li');
        li.innerHTML = txt;
        list.insertBefore(li,list.childNodes[0]);
        input.value = '';
    }
};
    
list.onclick = function(ev){
    if(ev.target.tagName == 'LI'){
        ev.target.classList.toggle('checked');
    }
};
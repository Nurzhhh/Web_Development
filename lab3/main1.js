let addToDoButton = document.getElementById('addToDo');
let toDoContainer = document.getElementById('toDoContainer');
let inputField = document.getElementById('inputField');

addToDoButton.addEventListener('click', function(){
    var paragraph = document.createElement('p');
    paragraph.classList.add('paragraph-styling');
    if(inputField.value ==''){
        alert('You must write something');
    }
    else{
        toDoContainer.appendChild(paragraph);
        paragraph.innerText = inputField.value;
        inputField.value = "";
        paragraph.addEventListener('click', function(){
            paragraph.style.textDecoration = "line-through";
        })
        paragraph.addEventListener('dblclick', function(){
            toDoContainer.removeChild(paragraph);
        })
    }
})

toDoContainer.onclick = function(ev){
    if(ev.target.tagName == 'UL'){
        ev.target.classList.toggle('checked');
    }
};

window.onload = function(){
    
    let selector = document.querySelector("#category");
    selector?.addEventListener('change',function(){
        let category_id = selector.value;
        console.log(category_id)
        if(category_id == "no_category"){
            removeChilds(document.getElementById('sub_category'));
        }
        else{
            ajax_request(category_id);
        }
        
    });


function ajax_request(id){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
    var res = JSON.parse(this.responseText)
         subdata = res.subdata;
     removeChilds(document.getElementById('sub_category'));
     for(const prop in subdata){
        add_option(prop,subdata[prop]);
     }
    }
  };
  xhttp.open("GET", `/ajax_handler/${id}`, true);
  xhttp.send();
}


function add_option(val,text){
    var sel = document.getElementById('sub_category');
    
// create new option element
var opt = document.createElement('option');

// create text node to add to option element (opt)
opt.appendChild( document.createTextNode(text) );

// set value property of opt
opt.value = val; 

// add opt to end of select box (sel)
sel.appendChild(opt); 
}

}

var removeChilds = function (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};
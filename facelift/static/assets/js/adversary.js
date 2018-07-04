function previewBaseFile(){
   var preview = document.querySelector('#baseImage'); //selects the query named img
   var file    = document.querySelector('#baseInput').files[0]; //sames as here
   var reader  = new FileReader();

   reader.onloadend = function () {
       preview.src = reader.result;
   }

   if (file) {
       reader.readAsDataURL(file); //reads the data as a URL
   } else {
       preview.src = "";
   }
}

function previewAttackFile(){
   var preview = document.querySelector('#attackImage'); //selects the query named img
   var file    = document.querySelector('#attackInput').files[0]; //sames as here
   var reader  = new FileReader();

   reader.onloadend = function () {
       preview.src = reader.result;
   }

   if (file) {
       reader.readAsDataURL(file); //reads the data as a URL
   } else {
       preview.src = "";
   }
}

function start() {
    var base = document.querySelector('#attackCont');
    base.classList.add("moveToCenterFromLeft");
}
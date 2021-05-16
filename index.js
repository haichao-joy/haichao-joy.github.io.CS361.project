function showsummary(){
    var s = document.getElementById('summary-text');
    s.innerHTML="Summary of your text";
}

var sbtn = document.querySelector('.summary-btn');
sbtn.addEventListener('click', showsummary);
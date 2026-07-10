function submit(){
  var name = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var colour = document.getElementById("favcolour").value;
  alert("Hello " + name + " your password is " + password + " and your favourite colour is " + colour);
  document.getElementById("messageOut").innerHTML="Hello"+name+"Youlike ht ecolour"+colour;6
}

function login(){
  var name = document.getElementById("username").value;
  var passw = document.getElementById("password").value;
  if (name == "Bob" && passw == "cake"){
    alert("Welcome to the site");
  }else{
    alert("Incorrect details");
    password.style.backgroundColor = "red";
  }

}
function myFunction() {
  alert("Hello! I am an alert box!");
}
function myFunction1() {
  if (window.top != window.self)  {
    document.getElementById("demo").innerHTML = "This window is not the topmost window! Am I in a frame?";
  } else {
    document.getElementById("demo").innerHTML = "This window is the topmost window!";
  }
}
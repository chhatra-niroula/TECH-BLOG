/**
 * The function toggles the display of an HTML element with the id "menu" between "block" and "none".
 */
// function myFunction() {
//     var x = document.getElementById("menu");
//     if (x.style.display === "none") {
//       x.style.display = "block";
//     } else {
//       x.style.display = "none";
//     }
//   } 

function myFunction() {
  var element = document.querySelector("#menu");
  // console.log(element.className)
  // console.log("hello1")
  if (element.classList.contains("hidden")) {
        element.classList.add("flex");
        element.classList.remove("hidden");
        // console.log(element.className)
        // console.log("i am inside if")
        } else {
          element.classList.replace("flex", "hidden");
        }
  
}
const menu1 = document.getElementById('menu');
const menuButton = document.getElementById('menu-btn');
// hide the menu when a click event occurs outside the menu
document.addEventListener('click', (event) => {
  console.log("i am inside if chhatra")
  if (!menu1.contains(event.target) && !menuButton.contains(event.target)) {
    menu1.classList.add('hidden');
    // console.log("i am insideasfasdf if chhatra")
  }
});




  const btn = document.getElementById('menu-btn')
  const nav = document.getElementById('menu')

  btn.addEventListener('click', () => {
    btn.classList.toggle('open')
 
  })

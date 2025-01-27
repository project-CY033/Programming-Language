document.getElementById("home").addEventListener("click", function() {
    const sportSection = document.getElementById("sport");
    sportSection.scrollIntoView({ behavior: "smooth" });
  });
  
  document.getElementById("game").addEventListener("click", function() {
    const gameSection = document.getElementById("game");
    gameSection.scrollIntoView({ behavior: "smooth" });
  });
  
  document.getElementById("time").addEventListener("click", function() {
    const timeSection = document.getElementById("time");
    timeSection.scrollIntoView({ behavior: "smooth" });
  });
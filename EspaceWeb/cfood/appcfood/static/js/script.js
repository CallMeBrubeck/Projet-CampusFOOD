/* let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menu.addEventListener("click", function () {
    navbar.classList.toggle("active");
});

window.onscroll = () => {
    navbar.classList.remove("active");
}; */
document.addEventListener("DOMContentLoaded", function() {
    let menu = document.querySelector("#menu-icon");
    let navbar = document.querySelector(".navbar");

    menu.addEventListener("click", function () {
        console.log("Menu icon clicked"); // Vérifie si la fonction est appelée
        navbar.classList.toggle("active");
        console.log(navbar.classList.contains("active")); // Vérifie si la classe "active" est ajoutée ou retirée
    });

    window.addEventListener("scroll", () => {
        console.log("Window scrolled"); // Vérifie si l'événement de défilement est détecté
        navbar.classList.remove("active");
        console.log(navbar.classList.contains("active")); // Vérifie si la classe "active" est retirée lors du défilement
    });
});


/* Evenement d appropos */
document.addEventListener("DOMContentLoaded", function() {
    // Récupérer le bouton "Learn More" de la section Home
    const learnMoreHomeBtn = document.getElementById("learnmore");

    // Ajouter un gestionnaire d'événement de clic au bouton "Learn More" de la section Home
    learnMoreHomeBtn.addEventListener("click", function(event) {
        // Empêcher le comportement par défaut du lien
        event.preventDefault();

        // Récupérer la position de la section "About Us"
        const aboutSection = document.getElementById("about");
        const aboutSectionTop = aboutSection.offsetTop;

        // Faire défiler la page jusqu'à la section "About Us"
        window.scrollTo({
            top: aboutSectionTop,
            behavior: "smooth" // Défilement en douceur
        });
    });
});


/* Js pour les sous categories du menus */
document.addEventListener("DOMContentLoaded", function() {
    // Récupérer le lien "Categories" et la liste déroulante des catégories
    const categoriesLink = document.getElementById("categories-link");
    const categoriesDropdown = document.getElementById("categories-dropdown");

    // Ajouter un gestionnaire d'événement de clic au lien "Categories"
    categoriesLink.addEventListener("click", function(event) {
        // Empêcher le comportement par défaut du lien
        event.preventDefault();

        // Afficher ou masquer la liste déroulante des catégories
        categoriesDropdown.style.display = categoriesDropdown.style.display === "none" ? "block" : "none";
    });
});



/* Gestion des lien pour le container de chaque category dans la navbar */ 
const liensCategories = document.querySelectorAll('.category-link');

liensCategories.forEach(lien => {
  lien.addEventListener('click', evenement => {
    evenement.preventDefault();

    const nomCategorie = evenement.target.textContent;

    // Affiche le conteneur correspondant à la catégorie
    const conteneurCategorie = document.querySelector(`#${nomCategorie}`);
    conteneurCategorie.classList.remove('d-none');
  });
});

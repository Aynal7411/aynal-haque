document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("mobile-menu-button");
    const menu = document.getElementById("mobile-menu");

    if (!button || !menu) return;

    button.addEventListener("click", () => {
        menu.classList.toggle("hidden");

        const expanded = button.getAttribute("aria-expanded") === "true";
        button.setAttribute("aria-expanded", (!expanded).toString());

        const icon = button.querySelector("i");

        if (menu.classList.contains("hidden")) {
            icon.className = "bi bi-list text-2xl";
        } else {
            icon.className = "bi bi-x-lg text-2xl";
        }
    });
});
const btn = document.getElementById("scrollTopBtn");

if (btn) {
    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            btn.classList.remove("hidden");
        } else {
            btn.classList.add("hidden");
        }
    });

    btn.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
}

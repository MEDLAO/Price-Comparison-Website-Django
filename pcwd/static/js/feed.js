document.addEventListener("DOMContentLoaded", () => {
    const postCards = document.querySelectorAll(".post-card");

    postCards.forEach((postCard) => {
        const postContent = postCard.querySelector(".post-content p:nth-child(2)"); // The content of the post

        postCard.addEventListener("click", () => {
            const contentWrapper = postCard.querySelector(".post-content");

            // Toggle the open class to show/hide content
            if (!contentWrapper.classList.contains("open")) {
                contentWrapper.classList.add("open"); // Add 'open' class

                // Reveal the post content when clicked
                postContent.style.display = "block";
            } else {
                contentWrapper.classList.remove("open"); // Remove 'open' class

                // Hide the post content again
                postContent.style.display = "none";
            }
        });
    });
});

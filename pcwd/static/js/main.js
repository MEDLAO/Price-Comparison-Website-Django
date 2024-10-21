document.addEventListener('DOMContentLoaded', () => {
    function truncateText(selector, maxLength) {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
            let text = element.innerText;
            if (text.length > maxLength) {
                element.innerText = text.substring(0, maxLength) + '...';
                if (document.documentElement.lang === 'ar') {
                    element.style.direction = 'rtl';
                } else {
                    element.style.direction = 'ltr';
                }
            }
        });
    }
    truncateText('.description', 32);

    const productCards = document.querySelectorAll('.product-card');

    productCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.querySelector('.product-image img').style.transform = 'scale(1.1)';
        });

        card.addEventListener('mouseleave', () => {
            if (!card.classList.contains('clicked')) {
                card.querySelector('.product-image img').style.transform = 'scale(1)';
            }
        });

        card.addEventListener('click', (event) => {
            const info = card.querySelector('.product-info');
            const button = card.querySelector('.visit-store-button');
            if (card.classList.contains('clicked')) {
                info.style.opacity = '0';
                button.classList.remove('show');
                card.classList.remove('clicked');
                card.querySelector('.product-image img').style.transform = 'scale(1)';
            } else {
                card.classList.add('clicked');
                info.style.opacity = '1';
                button.classList.add('show');
                card.querySelector('.product-image img').style.transform = 'scale(1.1)';
                button.addEventListener('click', (e) => {
                    e.stopPropagation();
                });
            }
        });
    });

    // Modal functionality
    const modals = document.querySelectorAll('.modal');
    const modalTriggers = document.querySelectorAll('.menu-item[data-modal]');

    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', (event) => {
            event.preventDefault();
            const modalId = trigger.getAttribute('data-modal');
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'block';
            }
        });
    });

    modals.forEach(modal => {
        const closeButton = modal.querySelector('.close');
        if (closeButton) {
            closeButton.addEventListener('click', () => {
                modal.style.display = 'none';
            });
        }

        window.addEventListener('click', (event) => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });

    // Update price output for range slider
    const priceRange = document.getElementById('priceRange');
    const priceOutput = document.getElementById('priceOutput');
    const currency = document.documentElement.lang === 'ar' ? 'ج.م' : 'EGP';

    if (priceRange && priceOutput) {
        priceRange.addEventListener('input', (event) => {
            const value = event.target.value;
            priceOutput.value = value + ' ' + currency;
            const percent = (value - priceRange.min) / (priceRange.max - priceRange.min) * 100;
            priceRange.style.background = `linear-gradient(to right, #01796F 0%, #01796F ${percent}%, #fff ${percent}%, #fff 100%)`;
        });
        // Set initial value with currency and background
        const initialValue = priceRange.value;
        priceOutput.value = initialValue + ' ' + currency;
        const initialPercent = (initialValue - priceRange.min) / (priceRange.max - priceRange.min) * 100;
        priceRange.style.background = `linear-gradient(to right, #01796F 0%, #01796F ${initialPercent}%, #fff ${initialPercent}%, #fff 100%)`;
    }
});

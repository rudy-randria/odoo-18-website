$(document).ready(function () {
    $('#searchInput').on('focus', function () {
        // Trouver le parent form de l'input en utilisant jQuery
        const form = $(this).closest('form');
        const button = form.find('button[type="submit"]');

        if (form.length) {
            // Appliquer box-sizing: border-box en JavaScript avec jQuery
            form.css('box-sizing', 'border-box');

            form.removeClass('custom-border');
            form.addClass('border-secondary');
        }

        if (button.length) {
            button.addClass('text-secondary');
        }
    });

    $('#searchInput').on('blur', function () {
        // Rétablir l'état initial lorsque l'input perd le focus
        const form = $(this).closest('form');
        const button = form.find('button[type="submit"]');

        if (form.length) {
            // Rétablir box-sizing à sa valeur initiale
            form.css('box-sizing', 'content-box'); // Ou la valeur par défaut si nécessaire

            form.removeClass('border-secondary');
            form.addClass('custom-border');
        }

        if (button.length) {
            button.removeClass('text-secondary');
        }
    });
});

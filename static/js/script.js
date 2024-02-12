$( document ).ready(function() {
    $('#modal-share-book').on('show.bs.modal', function (event) {
        var bookImageUrl = $(this).data('book-cover-img'); // Access the data attribute
        $("#share-url").val(bookImageUrl);
    });
    $("#copy-btn").on("click", function() {
        var shareUrlInput = document.getElementById("share-url");
        navigator.clipboard.writeText(shareUrlInput.value).then(function() {
            console.log('Copying to clipboard was successful!');
            // Provide user feedback that copying was successful.
        }, function(err) {
            console.error('Could not copy text: ', err);
            // Alert the user that copying failed.
        });
    });
});
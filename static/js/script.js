$(document).ready(function() {
    //Share the Book//

    /* insert URL into <input> */
    var bookUrl = $(location).attr("href");
    $("#share-btn").on("click", function() {
        $("#share-url").val(bookUrl);
    });
    /* copy value of <input> */
    $("#copy-btn").on("click", function() {
        var copyUrl = $("#share-url").val(bookUrl);
        copyUrl.select();
        document.execCommand("copy");
    });
})
$(".pub-filters-select") && M(), $(".js-cite-modal").click(function(c) {
    c.preventDefault();
    let a = $(this).attr("data-filename"),
        b = $("#modal");
    b.find(".modal-body code").load(a, function(d, c, b) {
        if (c == "error") {
            let a = "Error: ";
            $("#modal-error").html(a + b.status + " " + b.statusText)
        } else $(".js-download-cite").attr("href", a)
    }), b.modal("show")
}), $(".js-copy-cite").click(function(b) {
    b.preventDefault();
    let a = document.createRange(),
        c = document.querySelector("#modal .modal-body");
    a.selectNode(c), window.getSelection().addRange(a);
    try {
        document.execCommand("copy")
    } catch (a) {
        console.log("Error: citation copy failed.")
    }
    window.getSelection().removeRange(a)
}), N();

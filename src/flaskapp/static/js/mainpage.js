$('#search').keydown(function(e) {
    if (e.keyCode == 13) {
        console.log("!");
    }
});

$('.department').on({
    click: function () {
        let url = $(this).val();
        console.log(url);
        $(location).attr('href', '/major/'+url);
    }
});

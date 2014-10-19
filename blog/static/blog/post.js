$(function() {
    $(".fav").submit(function() {
        var url;
        url = $('.fav').prop('action');
        console.log(url);
        $.post(url, {}, function(data) {
            $('.fav').addClass('hide')
            $('.unfav').removeClass('hide')
        });
        return false;
    });
    $(".unfav").submit(function() {
        var url;
        url = $('.unfav').prop('action');
        console.log(url);
        $.post(url, {}, function(data) {
            $('.fav').removeClass('hide')
            $('.unfav').addClass('hide')
        });
        return false;
    });
})

$(document).ready(function () {
    $('input[name="username"]').keyup(function(){
        console.log("something has been typed in username field")
        var data = $(this).serialize()
        console.log(data)
        $.ajax({
            method: "POST", 
            url: "/username",
            data: data
        })
        .done(function(res){
            $('.availability').html(res) 
        })
    })
})
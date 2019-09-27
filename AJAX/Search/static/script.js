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

    $('input[name="name"]').keyup(function () {
        console.log("something has been typed in username field")
        var data = $(this).serialize()
        console.log(data)
        $.ajax({
            method: "GET",  
            url: "/usersearch",
            data: data
        })
        .done(function(res){
            $('.results').html(res) 
        })
    })
})
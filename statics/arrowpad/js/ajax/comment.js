function addComment(blogUrl) {
    console.log('yeah')
    const data = {
        'author' : document.getElementById("author").value,
        'email' : document.getElementById("email").value,
        'comment' : document.getElementById("comment").value,
        'url' : blogUrl
    }
    console.log(data)
    
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
            }
        }
    });
    // Sending data from validation
    $.ajax({
        url : '/blog/jx/add_comment/' ,
        type : "POST" ,
        data : {
            'getdata' : JSON.stringify(data)
        } ,
        dataType : 'json' ,
        success : function (res , status) {
            console.log(res.status);
            if (res.status == 200){
                console.log(res.msg);
            }if (res.status == 404) {
                console.log(res.msg);
            }
        } ,
        error : function () {
            console.log('er')
            
        } ,
    })
}